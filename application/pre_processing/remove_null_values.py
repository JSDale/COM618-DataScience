

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
    def drop_not_a_number(data_frame):
        return data_frame.dropna()
