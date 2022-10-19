from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.models import Sequential

class Model_Factory():
    def __init__(self):
        pass
    def create_model(self, config, n_features):
        model = None
        if config.type  == 'LSTM':
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
    
        if config.type  == 'CNN-LSTM':
            model = Sequential()
            model.add(Conv1D(filters=64,
                             kernel_size=3,
                             activation='relu',
                             input_shape=(None, n_features)))
            model.add(Conv1D(filters=64,
                             kernel_size=3,
                             activation='relu'))
            model.add(MaxPooling1D(pool_size=2))
            model.add(Flatten())
            model.add(RepeatVector(n_outputs))
            model.add(LSTM(200, activation='relu',
                           return_sequences=True))
            model.add(Dropout(config.dropout))

            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
        return model