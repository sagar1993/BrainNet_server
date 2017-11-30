import numpy as np
from pyedflib import EdfReader
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix


def featureVecs(out, sample_size):
    # sample_size = 120
    fVec = np.zeros((sample_size, 6), dtype=float)

    i = 0
    j = 0
    while i < len(out) and j < sample_size:
        fVec[j][:6] = out[i:i + 6]
        # print 'fVec : ', fVec[j][:5], out[i:i+5], i
        i = i + 6
        j = j + 1
    return fVec


def FeatureExt(signal, signal_len):
    # in seconds
    # signal_len = 120;
    # sample rate in HZ
    SR = 160;
    out = np.zeros((signal_len * 6), dtype=float);
    S_FFT = np.zeros((SR));

    for i in range(signal_len):
        offset = (i) * SR
        S_FFT[0:SR] = FFT(signal[offset:offset + SR])
        out[i * 6:(i * 6) + 5 + 1] = S_FFT[8:14]

    # plot_graph(out)
    featureVectors = featureVecs(out, signal_len)
    return featureVectors


def FFT(signal):
    L = len(signal)
    Y = np.fft.fft(signal, 1);
    # y = 2 * abs(Y(1:NFFT / 2 + 1));
    y = 2 * abs(Y);
    return y


def NaiveBayes(train_arr, test_arr, train_size, test_size):
    # sample_size = 120
    labels = np.ones((train_size + test_size), dtype=float)
    labels[train_size:train_size + test_size - 1] = 0

    ### Al data
    train_data = np.zeros((train_size + test_size, 6), dtype=float)
    train_data[0:train_size - 1][:] = train_arr[0:train_size - 1][:]
    train_data[train_size:train_size + test_size - 1][:] = test_arr[0:test_size - 1][:]

    gnb = GaussianNB()
    y_pred = gnb.fit(train_data, labels).predict(train_data)
    mat = confusion_matrix(labels, y_pred)
    # print 'Confusion Matrix: ', mat

    if (mat[0][0] > mat[0][1]) and (mat[1][1] > mat[1][0]):
        authenticated = 0
    else:
        authenticated = 1
    return authenticated


def get_feature(edf_file):
    reader = EdfReader(edf_file)
    n = reader.signals_in_file
    buffer = np.zeros((n, reader.getNSamples()[0]))
    for i in np.arange(n):
        buffer[i, :] = reader.readSignal(i)

    signal = list(buffer[0])

    signal_len = 64

    return FeatureExt(signal, signal_len)

def get_feature_signal(signal):

    signal_len = 64

    return FeatureExt(signal, signal_len)