import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pre_processing import remove_null_values


class TestNullChecking(unittest.TestCase):

    def tests_returns_df_if_not_nulls(self):
        values = ['test', 'wibble', 'floob']
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        returned_df = checker.replace_not_a_number_with_mean(df)

        assert_frame_equal(df, returned_df)

    def tests_returns_new_df_if_nulls(self):
        values = [1, 2, None, 4]
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        returned_df = checker.replace_not_a_number_with_mean(df)
        self.assertFalse(assert_frame_equal(df, returned_df))

    def tests_does_not_drop(self):
        values = ['test', 'wibble', 'floob']
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        returned_df = checker.drop_not_a_number(df)

        assert_frame_equal(df, returned_df)

    def tests_drops(self):
        values = [1, 2, None, 4]
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        returned_df = checker.drop_not_a_number(df)
        self.assertFalse(checker.contains_nulls(returned_df))

    def tests_returns_true_if_null(self):
        values = ['test', 'wibble', 'floob', None]
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        has_nulls = checker.contains_nulls(df)

        self.assertTrue(has_nulls)

    def tests_returns_false(self):
        values = ['test', 'wibble', 'floob']
        df = pd.DataFrame(values)
        checker = remove_null_values.RemoveNullValues
        has_nulls = checker.contains_nulls(df)

        self.assertFalse(has_nulls)
