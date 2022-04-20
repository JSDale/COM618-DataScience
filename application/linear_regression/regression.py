import matplotlib.pyplot as plt
import statsmodels.api as sm


class LinearRegression:

    @staticmethod
    def create_scatter_graph(data_frame, save_path):
        print('regressing...')
        plt.scatter(data_frame['Deaths'], data_frame['Downloads'])
        plt.title('Downloads against Deaths')
        plt.ylabel('Downloads')
        plt.xlabel('Deaths')
        plt.savefig(save_path)

    @staticmethod
    def apply(data_frame):
        y = data_frame['Deaths']
        x = data_frame['Downloads']
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        print(model.summary())
