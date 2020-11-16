import os
import shutil
import pytest
import unittest
import pandas as pd
import numpy as np

from monty.serialization import loadfn

from pumml.pupredict import PUPredict

test_dir = os.path.join(os.path.dirname(__file__), "../../test_files/")

class PULearnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pup = PUPredict('fake_api_key')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pupredict(self):
        # TODO add tests
        self.pup
        assert os.path.isdir('Model_Data')
        assert os.path.exists('pupredict_data.tar.gz')

        shutil.rmtree('Model_Data')
        os.remove('pupredict_data.tar.gz')