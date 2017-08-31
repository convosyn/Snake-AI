import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical

class AIModel:
	def __init__(self, model_name = "train_model.h5", use_prev_model = False, train_data_file = None):
		self.use_prev_model = False
		self.model_name = model_name
		self.train_data_file = train_data_file

	def __model_configure(self):
		self.model = Sequential()
		self.model.add(Dense(self.input_dim, activation = 'relu', input_shape = self.input_dim, kernel_initializer = 'normal'))
		#self.model.add(Dense(self.input_dim, activation = 'relu', kernel_initializer = 'normal'))
		self.model.add(Dense(self.output_dim, activation = 'softmax', kernel_initializer = 'normal'))
		self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
		print("Saving Model Before training ...")
		self.model.save('trained_model.h5')

	def train(self, in_dim = 0, out_dim = 0, epochs = 200):
		if in_dim == 0 or out_dim == 0:
			raise ValueError("dimensions not specified")
		train_data = np.loadtxt(self.train_data_file)
		X_train, Y_train = train_data[:, 1:], train_data[:, 0]
		Y_hot_encode = to_categorical(Y_train, num_classes = 5)
		self.input_dim, self.output_dim = in_dim, out_dim
		self.__model_configure()
		print("training")
		self.model.fit(X_train, Y_hot_encode, epochs = 100, batch_size = 50, shuffle = False)

		#----complete from here-----
		#TODO:
		# 1. complete the training method
		# 2. write code for testing/predictions data
