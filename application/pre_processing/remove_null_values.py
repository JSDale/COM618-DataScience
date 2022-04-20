

class RemoveNullValues:

    @staticmethod
    def contains_nulls(data_frame):
        for i in data_frame:
            if data_frame[i].isnull().values.any():
                return True

        return False

    @staticmethod
    def replace_not_a_number_with_mean(data_frame):
        for i in data_frame:
            if data_frame[i].isnull().values.any():
                mean = data_frame[i].mean()
                data_frame[i].fillna(mean)
        return data_frame

    @staticmethod
    def replace_not_a_number_with_median(data_frame):
        # this only works if there are not any consecutive NaNs
        for i in data_frame:
            if data_frame[i].isnull().values.any():
                a = data_frame[i-1]
                b = data_frame[i+1]
                median = ((a-b)/2)+b
                data_frame[i].fillna(median)
        return data_frame

    @staticmethod
    def drop_not_a_number(data_frame):
        return data_frame.dropna()
