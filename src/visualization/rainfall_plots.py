
import matplotlib.pyplot as plt

def rainfall_trend_plot(df):

    plt.figure()
    plt.plot(df['date'], df['rainfall_mm'])
    plt.title("Rainfall Time Series")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.show()
