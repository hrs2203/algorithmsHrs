from neural_net import NeuralNetwork
import pytest, json
import numpy as np

input_size = 4
hidden_size = 10
num_classes = 3
num_inputs = 50

epochs = 200
batch_size = 1
learning_rate = 1e-3
learning_rate_decay = 0.95
regularization = 5e-6

def init_toy_model(num_layers):
    np.random.seed(0)
    hidden_sizes = [hidden_size] * (num_layers - 1)
    return NeuralNetwork(input_size, hidden_sizes, num_classes, num_layers)

def operation(i):
	if i<10:
		return 0
	elif i<22:
		return 1
	return 2

def init_toy_data():
    np.random.seed(0)
    X = 10 * np.random.randn(num_inputs, input_size)
    # print(X.shape)
    y = np.array([ operation(i) for i in np.sum(X, axis=1) ])
    # print(y.shape)
    # print(y)
    return X, y


def loadDataToFile():
	fileObj = open("loadedData.json", "w")
	x,y = init_toy_data()
	dictObj = { "x": x.tolist(), "y": y.tolist() }
	json.dump(dictObj, fileObj, indent=4)
	fileObj.close()

def loadDataFromFile():
	fileObj = open("loadedData.json", "r")
	fileContent = json.load(fileObj)
	fileObj.close()
	return np.array(fileContent['x']), np.array(fileContent['y'])

def getAccuracy(Y, pred):
	count = len(Y)
	correct = 0
	for i in range(count):
		if Y[i]==pred[i]:
			correct+=1
	return correct/count


if __name__ == '__main__':
	# loadDataToFile()
	X,Y = loadDataFromFile()
	model = init_toy_model(3)
	# print(model)

	# ============ train test model ==============
	
	# Variables to store performance for each epoch
	train_loss = np.zeros(epochs)
	train_accuracy = np.zeros(epochs)

	for epoch in range(epochs):
		print(f"epoch {epoch} in progress...", end=" ")
		forwardPass = model.forward(X)
		pred = model.getPred(forwardPass)
		
		train_accuracy[epoch]= getAccuracy(Y, pred)
		print(f"Prediction Done...", end=" ")

		print(f"Training...", end=" ")
		# back prop using SGD
		tempLoss = model.backward(X, Y, learning_rate)
		train_loss[epoch]= tempLoss
		print(f"Done. Loss: {train_loss[epoch]}, accuray: {train_accuracy[epoch]}")

	print(train_loss)
	print(train_accuracy)








	
	