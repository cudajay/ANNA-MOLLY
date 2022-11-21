from keras.layers import LSTM, Input, Concatenate, Reshape, GRU
from keras.layers import TimeDistributed
from keras.layers.core import Dense, Activation, Dropout, Flatten, RepeatVector
from keras.layers.convolutional import Conv1D, Conv2D
from keras.layers.convolutional import MaxPooling1D
from keras.models import Sequential, Model

def make_net(model, n_layers, hidden_units, output_units, net_type='GRU'):
    if net_type=='GRU':
        for i in range(n_layers):
            model.add(GRU(units=hidden_units,
                      return_sequences=True,
                      name=f'GRU_{i + 1}'))
    else:
        for i in range(n_layers):
            model.add(LSTM(units=hidden_units,
                      return_sequences=True,
                      name=f'LSTM_{i + 1}'))

    model.add(Dense(units=output_units,
                    activation='sigmoid',
                    name='OUT'))
    return model

class Supervisor(Model):
    def __init__(self, hidden_dim):
        self.hidden_dim=hidden_dim

    def build(self, input_shape):
        model = Sequential(name='Supervisor')
        model.add(Input(shape=input_shape))
        model = make_net(model,
                         n_layers=2,
                         hidden_units=self.hidden_dim,
                         output_units=self.hidden_dim)
        return model

class Generator(Model):
    def __init__(self, hidden_dim, net_type='GRU'):
        self.hidden_dim = hidden_dim
        self.net_type = net_type

    def build(self, input_shape):
        model = Sequential(name='Generator')
        model.add(Input(shape=input_shape))
        model = make_net(model,
                         n_layers=3,
                         hidden_units=self.hidden_dim,
                         output_units=self.hidden_dim,
                         net_type=self.net_type)
        return model

class Discriminator(Model):
    def __init__(self, hidden_dim, net_type='GRU'):
        self.hidden_dim = hidden_dim
        self.net_type=net_type

    def build(self, input_shape):
        model = Sequential(name='Discriminator')
        model = make_net(model,
                         n_layers=3,
                         hidden_units=self.hidden_dim,
                         output_units=1,
                         net_type=self.net_type)
        return model

class Recovery(Model):
    def __init__(self, hidden_dim, n_seq):
        self.hidden_dim=hidden_dim
        self.n_seq=n_seq
        return

    def build(self, input_shape):
        recovery = Sequential(name='Recovery')
        recovery.add(Input(shape=input_shape, name='EmbeddedData'))
        recovery = make_net(recovery,
                            n_layers=3,
                            hidden_units=self.hidden_dim,
                            output_units=self.n_seq)
        return recovery

class Embedder(Model):

    def __init__(self, hidden_dim):
        self.hidden_dim=hidden_dim
        return

    def build(self, input_shape):
        embedder = Sequential(name='Embedder')
        embedder.add(Input(shape=input_shape, name='Data'))
        embedder = make_net(embedder,
                            n_layers=3,
                            hidden_units=self.hidden_dim,
                            output_units=self.hidden_dim)
        return embedder

class Supervisor(Model):
    def __init__(self, hidden_dim):
        self.hidden_dim=hidden_dim

    def build(self, input_shape):
        model = Sequential(name='Supervisor')
        model.add(Input(shape=input_shape))
        model = make_net(model,
                         n_layers=2,
                         hidden_units=self.hidden_dim,
                         output_units=self.hidden_dim)
        return model