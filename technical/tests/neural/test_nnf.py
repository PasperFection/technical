from tensorflow.examples.tutorials.mnist import input_data

from technical.exchange import historical_data
from technical.neural import nnf, mnnf
from technical.util import ticker_history_to_dataframe
from technical.util import compute_interval, ticker_history_to_dataframe
from technical.history import load_data


def test_nnf():
    print("populate intial data set")
    ticker = historical_data("USDT", "BTC", "15m",days=1)

    dataframe = ticker_history_to_dataframe(ticker)

    training_data = ticker_history_to_dataframe(load_data("btc/usdt", "15m",days=100))

    #
    print("execute neural network")
    result = nnf(dataframe, training_data, epoch=10, features=["close"],input_len_for_prediction=5)
    # result = nnf(dataframe, training_data, epoch=1000, features=["open"])
    # result = nnf(dataframe, training_data, epoch=1000, features=["high"])
    # result = nnf(dataframe, training_data, epoch=1000, features=["low"])


def test_mnnf():
    print("populate intial data set")
    dataframe = ticker_history_to_dataframe(historical_data("USDT", "BTC", "15m",days=1))
    training_data = ticker_history_to_dataframe(load_data("btc/usdt", "15m", days=1))
    training_data = ticker_history_to_dataframe(load_data("btc/usdt", "15m", days=1))

    mnnf(dataframe, training_data, features=['close'], epoch=1000)
