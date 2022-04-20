import matplotlib.pyplot as plt
import statsmodels.api as sm

from pre_processing import remove_null_values as processor


class LinearRegression:

    @staticmethod
    def create_scatter_graph(data_frame, save_path):
        data_frame = processor.RemoveNullValues.drop_not_a_number(data_frame)
        plt.scatter(data_frame['Deaths'], data_frame['Downloads'])
        plt.title('Downloads against Deaths')
        plt.ylabel('Downloads')
        plt.xlabel('Deaths')
        plt.savefig(save_path)

    @staticmethod
    def apply(data_frame):
        for i in range(len(data_frame['Week starting'])):
            print(data_frame['Week starting'][i])
            print(data_frame['Week ending'][i])
        data_frame = processor.RemoveNullValues.drop_not_a_number(data_frame)
        y = data_frame['Deaths']
        x = data_frame['Downloads']
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        print(model.summary())
