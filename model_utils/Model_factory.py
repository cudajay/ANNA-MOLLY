from keras.layers import LSTM
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.models import Sequential

from keras.layers import LSTM, Input, Concatenate, Reshape
from keras.layers import TimeDistributed
from keras.layers.core import Dense, Activation, Dropout, Flatten, RepeatVector
from keras.layers.convolutional import Conv1D, Conv2D
from keras.layers.convolutional import MaxPooling1D
from keras.models import Sequential, Model

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
    
        elif config.type  == 'cnn-1h':
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
                config.layers[1],
                return_sequences=False))
            model.add(Dropout(config.dropout))

            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
            model.add(Dense(
                config.n_predictions))
            model.add(Activation('linear'))
        elif config.type  == 'cnn-mh':
            il = Input(shape = (config.l_s,n_features))
            head_list = []
            nHeads = 5
            for i in range(nHeads):
                conv_layer_head = Conv1D(filters=10, kernel_size=3, activation='relu')(il)
                conv_layer_head_2 = Conv1D(filters=10, kernel_size=3, activation='relu')(conv_layer_head)
                conv_layer_flatten = Flatten()(conv_layer_head_2)
                head_list.append(conv_layer_flatten)
            concat_cnn = Concatenate(axis=1)(head_list)
            reshape = Reshape((head_list[0].shape[-1], nHeads))(concat_cnn)
            lstm = LSTM(config.layers[1],return_sequences=False)(reshape)
            do = Dropout(config.dropout)(lstm)
            dense1 = Dense(
                    config.n_predictions)(do)
            act1 = Activation('linear')(dense1)
            dense2 = Dense(config.n_predictions)(act1)
            act2 = Activation('linear')(dense1)
            model = Model(inputs=il, outputs=act2)
        else:
            print("No model configuration found "*20)
            assert(False)
        return model
