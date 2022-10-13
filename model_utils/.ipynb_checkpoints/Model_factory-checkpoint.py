from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout
from keras.models import Sequential

class Model_Factory():
    def __init__(self):
        pass
    def create_model(self, config):
        model = None
        if config.type  == 'LSTM':
            model = Sequential()

            model.add(LSTM(
                config.layers[0],
                input_shape=(None, 55),
                return_sequences=True))
            model.add(Dropout(config.dropout))

            model.add(LSTM(
                config.layers[1],
                return_sequences=False))
            model.add(Dropout(config.dropout))

            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
        return model