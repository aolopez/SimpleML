'''
Pipeline Validation Splitting related tests
'''

__author__ = 'Elisha Yadgaran'


import unittest
import numpy as np
from simpleml.pipelines.validation_split_mixins import SplitMixin, NoSplitMixin,\
    RandomSplitMixin, ExplicitSplitMixin, ChronologicalSplitMixin, KFoldSplitMixin


class MockDataset(object):
    X = np.random.rand(10, 10)
    y = np.random.rand(10, 1)


class MockBasePipeline(object):
    dataset = MockDataset()


class SplitMixinTests(unittest.TestCase):
    pass


class NoSplitMixinTests(unittest.TestCase):
    def test_same_split_always_returned(self):
        '''
        Calling defaultdict with a singleton value should always return the
        same object
        '''


class RandomSplitMixinTests(unittest.TestCase):
    pass


class ExplicitSplitMixinTests(unittest.TestCase):
    pass


class ChronologicalSplitMixinTests(unittest.TestCase):
    pass


class KFoldSplitMixinTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
