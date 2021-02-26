"""Neural network model."""

from typing import Sequence

import numpy as np


class NeuralNetwork:
    """A multi-layer fully-connected neural network. The net has an input
    dimension of N, a hidden layer dimension of H, and performs classification
    over C classes. We train the network with a cross-entropy loss function and
    L2 regularization on the weight matrices.

    The network uses a nonlinearity after each fully connected layer except for
    the last. The outputs of the last fully-connected layer are passed through
    a softmax, and become the scores for each class."""

    def __init__(
        self,
        input_size: int,
        hidden_sizes: Sequence[int],
        output_size: int,
        num_layers: int,
    ):
        """Initialize the model. Weights are initialized to small random values
        and biases are initialized to zero. Weights and biases are stored in
        the variable self.params, which is a dictionary with the following
        keys:

        W1: 1st layer weights; has shape (D, H_1)
        b1: 1st layer biases; has shape (H_1,)
        ...
        Wk: kth layer weights; has shape (H_{k-1}, C)
        bk: kth layer biases; has shape (C,)

        Parameters:
            input_size: The dimension D of the input data
            hidden_size: List [H1,..., Hk] with the number of neurons Hi in the
                hidden layer i
            output_size: The number of classes C
            num_layers: Number of fully connected layers in the neural network
        """
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        self.num_layers = num_layers

        assert len(hidden_sizes) == (num_layers - 1)
        sizes = [input_size] + hidden_sizes + [output_size]

        self.params = {}
        for i in range(1, num_layers + 1):
            self.params["W" + str(i)] = np.random.randn(
                sizes[i - 1], sizes[i]
            ) / np.sqrt(sizes[i - 1])
            self.params["b" + str(i)] = np.zeros(sizes[i])
            # self.params[f"b{i}"] = self.params[f"b{i}"].reshape(self.params[f"b{i}"].shape[0],1)

    def __str__(self):
        object_info = [
            f"input_size: {self.input_size}",
            f"hidden_sizes: {self.hidden_sizes}",
            f"output_size: {self.output_size}",
            f"num_layers: {self.num_layers}",
            f"params: {self.params.keys()}",
            f"layerShapes: { [ [i, self.params[i].shape] for i in self.params ]}"
        ]
        return "\n".join(object_info)

    def linear(self, W: np.ndarray, X: np.ndarray, b: np.ndarray) -> np.ndarray:
        """Fully connected (linear) layer.

        Parameters:
            W: the weight matrix
            X: the input data
            b: the bias

        Returns:
            the output
        """
        # TODO: implement me :

        return np.dot(X, W) + b

    def relu(self, X: np.ndarray) -> np.ndarray:
        """Rectified Linear Unit (ReLU).

        Parameters:
            X: the input data

        Returns:
            the output
        """
        # TODO: implement me :
        return np.maximum(X, 0)

    def softmax(self, X: np.ndarray) -> np.ndarray:
        """The softmax function.

        Parameters:
            X: the input data

        Returns:
            the output
        """
        # TODO: implement me :
        allExp = np.exp(X)
        totalSum = np.sum(allExp, axis=1)
        totalSum = totalSum.reshape(totalSum.shape[0], 1)
        return allExp / totalSum

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Compute the scores for each class for all of the data samples.

        Hint: this function is also used for prediction.

        Parameters:
            X: Input data of shape (N, D). Each X[i] is a training or
                testing sample

        Returns:
            Matrix of shape (N, C) where scores[i, c] is the score for class
                c on input X[i] outputted from the last layer of your network
        """
        self.outputs = {"h0": X}
        # TODO: implement me. You'll want to store the output of each layer in
        # self.outputs as it will be used during back-propagation. You can use
        # the same keys as self.params. You can use functions like
        # self.linear, self.relu, and self.softmax in here.

        ## RELU for inner layers -> self.num_layers-1 .
        for layer in range(1, self.num_layers):
            self.outputs[f"h{layer}"] = self.relu(
                self.linear(
                    self.params[f"W{layer}"],
                    self.outputs[f"h{layer-1}"],
                    self.params[f"b{layer}"],
                )
            )

        ## Softmax for output layer.
        self.outputs[f"h{self.num_layers}"] = self.softmax(
            self.linear(
                self.params[f"W{self.num_layers}"],
                self.outputs[f"h{self.num_layers-1}"],
                self.params[f"b{self.num_layers}"],
            )
        )

        return self.outputs[f"h{self.num_layers}"]

    def getPred(self, pred: np.ndarray) -> np.ndarray:
        # TODO: Optimize me.
        """ CUSTOM CLASS: List of index of class with highest score """
        outputClass = []
        for l in pred:
            i = 0
            for j in range(len(l)):
                if l[j] > l[i]:
                    i = j
            outputClass.append(i)
        return np.array(outputClass)

    def crossEntropyLoss(self, Y: np.ndarray, y: np.ndarray) -> float:
        """
        Y: real Values
        y: predicted Values from gradient
        """
        # TODO: implement Me
        # formula used: (1/n)*(sum( y*ln(p)+( (1-y)*ln(1-p) ) ))

        count = len(Y)

        oneHotY = np.zeros(y.shape)
        for i in range(count):
            oneHotY[i][Y[i]]=1.0

        totalLoss = -1*np.sum(
            np.sum( oneHotY*np.log(y) + ((1-oneHotY)*np.log(1-y)), axis=1 )/self.output_size
        )/count

        return totalLoss

    def backward(
        self, X: np.ndarray, y: np.ndarray, lr: float, reg: float = 0.0
    ) -> float:
        """Perform back-propagation and update the parameters using the
        gradients.

        Parameters:
            X: Input data of shape (N, D). Each X[i] is a training sample
            y: Vector of training labels. y[i] is the label for X[i], and each
                y[i] is an integer in the range 0 <= y[i] < C
            lr: Learning rate
            reg: Regularization strength

        Returns:
            Total loss for this batch of training samples
        """
        self.gradients = {}
        loss = 0.0

        forwardPass = self.forward(X)
        loss = self.crossEntropyLoss(y, forwardPass)

        count = len(y)
        oneHotY = np.zeros(forwardPass.shape)
        for i in range(count):
            oneHotY[i][y[i]]=1.0


        oneHotY = oneHotY.T
        forwardPass = forwardPass.T

        # print()
        # print(f"oneHotY.shape: {oneHotY.shape}")
        # print(f"forwardPass.shape: {forwardPass.shape}")

        dl = np.sum( ((oneHotY/forwardPass)+((1-oneHotY)/(1-forwardPass))) * ( forwardPass*(1-forwardPass) ) , axis=1)
        
        prev_inpSm = np.sum(self.outputs[f"h{self.num_layers-1}"].T, axis=1)
        prev_inpSm = prev_inpSm.reshape(prev_inpSm.shape[0],1)

        # print()
        # print(f"dl.shape: {dl.shape}")
        # print(f"prev_inpSm.shape: {prev_inpSm.shape}")

        self.gradients[f"dw{self.num_layers}"] = np.dot(prev_inpSm, dl.reshape(1,dl.shape[0]))
        self.gradients[f"db{self.num_layers}"] = dl

        # print(f'dw: {self.gradients[f"dw{self.num_layers}"].shape}')
        # print(f'db: {self.gradients[f"db{self.num_layers}"].shape}')

        self.params[f"W{self.num_layers}"] -= lr*self.gradients[f"dw{self.num_layers}"]
        self.params[f"b{self.num_layers}"] -= lr*self.gradients[f"db{self.num_layers}"]
        

        for i in range(1, self.num_layers):
            # print(f"{self.num_layers-i} started ...")
            prev_inpSm = np.sum(self.outputs[f"h{self.num_layers-i-1}"].T, axis=1)
            prev_inpSm = prev_inpSm.reshape(prev_inpSm.shape[0],1)
            # print(f"prev_inpSm.shape: {prev_inpSm.shape}")
            dl = (
                np.sum( self.gradients[f"dw{self.num_layers-i+1}"], axis=1) * 
                np.sum( np.maximum(self.outputs[f"h{self.num_layers-i}"].T, 0), axis=1 )
            )
            # print(f'dl: {dl.shape}')

            self.gradients[f"dw{self.num_layers-i}"] = np.dot(prev_inpSm, dl.reshape(1,dl.shape[0]))
            self.gradients[f"db{self.num_layers-i}"] = dl

            self.params[f"W{self.num_layers-i}"] -= lr*self.gradients[f"dw{self.num_layers-i}"]
            self.params[f"b{self.num_layers-i}"] -= lr*self.gradients[f"db{self.num_layers-i}"]

            # print(f"{self.num_layers-i} done ...")
            
            

        # Calculate gradient and make adjustements.

        # self.gradient[f"h{self.num_layers}"] = 

        # TODO: implement me. You'll want to store the gradient of each layer
        # in self.gradients if you want to be able to debug your gradients
        # later. You can use the same keys as self.params. You can add
        # functions like self.linear_grad, self.relu_grad, and
        # self.softmax_grad if it helps organize your code.
        return loss
