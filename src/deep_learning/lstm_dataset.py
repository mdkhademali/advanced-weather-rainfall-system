
import numpy as np

def build_lstm_dataset(series, window=10):

    X=[]
    y=[]

    for i in range(len(series)-window):
        X.append(series[i:i+window])
        y.append(series[i+window])

    return np.array(X), np.array(y)
