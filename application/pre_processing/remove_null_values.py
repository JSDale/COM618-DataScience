import numpy as np


class RemoveNullValues:

    @staticmethod
    def contains_nulls(data_frame):
        return data_frame.isnull().values.any()

    @staticmethod
    def replace_not_a_number_with_mean(data_frame):
        if data_frame.isnull().values.any():
            mean = data_frame.mean()
            data_frame.fillna(value=mean, inplace=True)
        return data_frame

    @staticmethod
    def drop_not_a_number(data_frame):
        return data_frame.dropna()
