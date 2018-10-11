# Plotting module for approximation/prediction
import matplotlib.pyplot as plt


def plot_data(x, reference, predictions, models):
    plt.scatter(x, reference, s=1, marker=',', color='black', label='Reference Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Approximation/prediction model comparison')

    for model, prediction in zip(models, predictions):
        plt.plot(x, prediction, label=str(model.kernel))

    labels = x[:10]
    plt.xticks(range(0, len(x), 10), labels, rotation='vertical')

    plt.legend()
    plt.show()
