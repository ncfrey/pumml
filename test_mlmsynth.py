import os
import unittest
import pandas as pd
import numpy as np

from monty.serialization import loadfn

from mlmsynth import PULearner

test_dir = "test_files"

class PULearnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.max_df_fname = os.path.join(test_dir, 'MAX_dataset.json')
        cls.mx_df_fname = os.path.join(test_dir, 'MX_dataset.json')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cv_baggingDT(self):
        pul = PULearner()
        pu_stats = pul.cv_baggingDT(pu_data=self.max_df_fname, repeats=10, bags=10, filename='stats.json')

        # Test that reasonable TPR accuracy is achieved
        accuracy = pu_stats['metrics'][0]
        self.assertGreater(accuracy, 0.50)

        # Test that 95% CI is reasonable
        lower_ci = pu_stats['metrics'][1]
        upper_ci = pu_stats['metrics'][2]
        self.assertLess(upper_ci - lower_ci, 0.50)


if __name__ == '__main__':
    unittest.main()


