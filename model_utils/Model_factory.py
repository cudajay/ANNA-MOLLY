from keras.layers import LSTM
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.models import Sequential

class Model_Factory():
    def __init__(self):
        pass
    def create_model(self, config, n_features):
        model = None
        if config.type  == 'lstm':
            model = Sequential()

            model.add(LSTM(
                config.layers[0],
                input_shape=(None, n_features),
                return_sequences=True))
            model.add(Dropout(config.dropout))

            model.add(LSTM(
                config.layers[1],
                return_sequences=False))
            model.add(Dropout(config.dropout))

            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
    
        elif config.type  == 'cnn':
            model = Sequential()
            model.add(Conv1D(filters=64,
                             kernel_size=3,
                             activation='relu',
                             input_shape=(None, n_features)))
            model.add(Conv1D(filters=64,
                             kernel_size=3,
                             activation='relu'))
            model.add(Dropout(config.dropout))
            model.add(Dense(
                25))
            model.add(LSTM(
                cfg.layers[1],
                return_sequences=False))
            model.add(Dropout(cfg.dropout))

            model.add(Dense(
                cfg.n_predictions))
            model.add(Activation('linear'))
            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
        else:
            print("No model configuration found "*20)
            assert(False)
        return model
