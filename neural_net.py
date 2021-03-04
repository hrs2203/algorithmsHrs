"""Neural network model."""

from typing import Sequence
import numpy as np

# ============ Util Fxn ===================

def cross_entropy_loss(y: np.ndarray, p: np.ndarray) -> float:
    """
    y: np.ndarray, OneHotY
    p: np.ndarray, prediction Matrix
    """
    return -1*np.mean(np.sum( y*np.log(p), axis=1))

def relu_activation(x: np.ndarray) -> np.ndarray:
    """ Relu Activation Function """
    return np.maximum(0, x)

def relu_gradient(x: np.ndarray) -> np.ndarray:
    """ Relu Gradient Calculator """
    return np.where( x>0, 1, 0 )

def softmax_activation(x: np.ndarray) -> np.ndarray:
    """ Softmax Activation Fxn """
    # expoVal = np.exp(x)
    expoVal = np.exp(x - np.max(x)) # Avoid Overflow
    expSum = np.sum(expoVal, axis=1, keepdims=True)
    return expoVal/ expSum

def softmax_gradient(x: np.ndarray) -> np.ndarray:
    """ Softmax Gradient Calculator """
    # TODO: ******** WRONG implimentation ********
    return x*(1-x)

def get_one_hot(x: np.ndarray, classCount: int) -> np.ndarray:
    assert(len(x.shape)==1)
    oneHot = np.zeros((*x.shape, classCount))
    oneHot[range(len(x)), x] = 1.0
    return oneHot

# =========================================


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

    def linear(self, W: np.ndarray, X: np.ndarray, b: np.ndarray) -> np.ndarray:
        """Fully connected (linear) layer.

        Parameters:
            W: the weight matrix
            X: the input data
            b: the bias

        Returns:
            the output
        """
        # TODO: implement me
        
        assert( len(X.shape)==2 )
        assert( X.shape[1]==W.shape[0] )

        return np.dot(X,W)+b

    def relu(self, X: np.ndarray) -> np.ndarray:
        """Rectified Linear Unit (ReLU).

        Parameters:
            X: the input data

        Returns:
            the output
        """
        # TODO: implement me
        return np.maximum(X, 0)

    def softmax(self, X: np.ndarray) -> np.ndarray:
        """The softmax function.

        Parameters:
            X: the input data

        Returns:
            the output
        """
        # TODO: implement me
        return softmax_activation(X)

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
        
        assert( len(X.shape)==2 )

        self.outputs = {"h0": X}
        # TODO: implement me. You'll want to store the output of each layer in
        # self.outputs as it will be used during back-propagation. You can use
        # the same keys as self.params. You can use functions like
        # self.linear, self.relu, and self.softmax in here.

        for layer in range(1, self.num_layers):
            self.outputs[f"h{layer}"] = self.relu(self.linear(
                self.params[f"W{layer}"],
                self.outputs[f"h{layer-1}"],
                self.params[f"b{layer}"],
            ))
        
        self.outputs[f"h{self.num_layers}"] = self.softmax(self.linear(
            self.params[f"W{self.num_layers}"],
            self.outputs[f"h{self.num_layers-1}"],
            self.params[f"b{self.num_layers}"],
        ))

        return self.outputs[f"h{self.num_layers}"]

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
        # TODO: implement me. You'll want to store the gradient of each layer
        # in self.gradients if you want to be able to debug your gradients
        # later. You can use the same keys as self.params. You can add
        # functions like self.linear_grad, self.relu_grad, and
        # self.softmax_grad if it helps organize your code.

        oneHoyY = get_one_hot(y, self.output_size)
        
        loss = cross_entropy_loss(oneHoyY, self.outputs[f"h{self.num_layers}"])

        # ============ Calculating Gradient ==================
        dl = self.outputs[f"h{self.num_layers}"] - oneHoyY
        # dl = dl.T.mean(axis=1, keepdims=True).T
        
        # print(f"dl{self.num_layers}: {dl.shape}")
        
        # self.gradients[f"dw{self.num_layers}"] = self.outputs[f"h{self.num_layers-1}"].T.dot(dl)
        prevInp = self.outputs[f"h{self.num_layers-1}"].T
        self.gradients[f"dw{self.num_layers}"] = prevInp.dot(dl)

        self.gradients[f"db{self.num_layers}"] = dl.T.mean(axis=1)

        dl = dl.T.mean(axis=1, keepdims=True).T
        
        # print()
        for layer in range(self.num_layers-1, 0, -1):

            presentInp = self.outputs[f"h{layer}"].T.mean(axis=1, keepdims=True).T

            dl = dl.T.dot(relu_gradient(presentInp))
            dl = dl.T.mean(axis=1, keepdims=True).T

            prevLayer = self.outputs[f"h{layer-1}"].T.mean(axis=1, keepdims=True)

            # print(f"dl{layer}: {dl.shape}")
            # print(f'prevLayer: {prevLayer.shape}')
            
            self.gradients[f"dw{layer}"] = prevLayer.dot(dl)
            
            # print(f'dw{layer}: {self.gradients[f"dw{layer}"].shape}')
            # print(f'W {layer}: {self.params[f"W{layer}"].shape}')
            
            self.gradients[f"db{layer}"] = dl.squeeze()
            
            # print(f'db{layer}: {self.gradients[f"db{layer}"].shape}')
            # print(f'B {layer}: {self.params[f"b{layer}"].shape}')
            # print()
        # ====================================================

        # =============== Updading Parameters ================
        for layer in range(1, self.num_layers+1):
            self.params[f"W{layer}"] -= lr*self.gradients[f"dw{layer}"]
            self.params[f"b{layer}"] -= lr*self.gradients[f"db{layer}"]
        # ====================================================

        return loss
