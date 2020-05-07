import os
import unittest
import pandas as pd
import numpy as np

from monty.serialization import loadfn

from pumml.learners import PULearner, PUInteract

test_dir = "../test_files/"


class PULearnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.max_df_fname = os.path.join(test_dir, "MAX_dataset.json")
        cls.mx_df_fname = os.path.join(test_dir, "MX_dataset.json")
        cls.pul = PULearner()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cv_baggingDT(self):
        pu_stats = self.pul.cv_baggingDT(
            pu_data=self.max_df_fname, splits=10, repeats=3, bags=100
        )

        # Test that reasonable TPR accuracy is achieved
        accuracy = pu_stats["metrics"][0]
        self.assertGreater(accuracy, 0.50)

        # Test that 95% CI is reasonable
        lower_ci = pu_stats["metrics"][1]
        upper_ci = pu_stats["metrics"][2]
        self.assertLess(upper_ci - lower_ci, 0.50)


class PUInteractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.max_df_fname = os.path.join(test_dir, "MAX_dataset.json")
        cls.mx_df_fname = os.path.join(test_dir, "MX_dataset.json")
        cls.pul = PULearner()
        cls.pu_parent = cls.pul.cv_baggingDT(
            pu_data=cls.max_df_fname, splits=10, repeats=2, bags=10
        )
        cls.pu_child = cls.pul.cv_baggingDT(pu_data=cls.mx_df_fname, splits=10, repeats=2, bags=10)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clustering(self):
        pui = PUInteract(
            self.max_df_fname,
            self.pu_parent,
            self.mx_df_fname,
            self.pu_child,
            merge_on=("M", "X", "n"),
            feats=("a", "E_form", "E_coh", "synth_score"),
        )

        # Test that clustering and GMM are generating labels
        kmeans_output = pui.do_kmeans()
        self.assertEqual(len(kmeans_output["cluster_labels"]), 792)

        gmm_output = pui.do_gmixture()
        self.assertEqual(len(gmm_output["gmm_labels"]), 792)

        bgm_output = pui.do_bgm()
        self.assertEqual(len(bgm_output["bgm_labels"]), 792)


if __name__ == "__main__":
    unittest.main()
