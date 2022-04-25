import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

from pre_processing import remove_null_values as processor


class LinearRegression:
    @staticmethod
    def create_scatter_graph(data_frame, save_path):
        data_frame = processor.RemoveNullValues.drop_not_a_number(data_frame)
        y = data_frame['Deaths']
        x = data_frame['Downloads']
        plt.scatter(x, y)
        plt.title('Does cumulative app downloads reduce covid-deaths?')
        plt.ylabel('Deaths')
        plt.xlabel('Cumulative Downloads')
        plt.savefig(save_path)

        a, b = np.polyfit(x.values, y.values, 1)
        plt.plot(x, a*x+b)
        plt.savefig(f'{save_path}_line_best_fit.png')

    @staticmethod
    def apply(data_frame):
        # for i in range(len(data_frame['Week starting'])):
        #     print(data_frame['Week starting'][i])
        #     print(data_frame['Week ending'][i])
        data_frame = processor.RemoveNullValues.drop_not_a_number(data_frame)
        y = data_frame['Deaths']
        x = data_frame['Downloads']
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        print(model.summary())
