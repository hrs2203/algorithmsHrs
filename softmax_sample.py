import numpy as np
import csv

TRAINING_FILE = "./training1.csv"
TEST_FILE = "./test1.csv"


def readFile(fileNameArg: str) -> list:
    """read csv file

    Args:
        fileNameArg (str): file to read

    Returns:
        list: np.array( fileContent )
    """
    fileObject = open(fileNameArg, "r")
    fileContentTemp = fileObject.read()
    fileObject.close()
    fileContent = [item.split(",") for item in fileContentTemp.split("\n")]
    return fileContent[:-1]

def parseCsv(inpArray: list):
    """Parse Input

    Args:
        inpArray (list): output from @readFile

    Returns:
        X, Y: np.array(X), np.array(Y)
    """
    X = []
    Y = []
    for item in inpArray:
        X.append(item[:-1])
        Y.append(item[-1])
    return np.array(X, dtype='float64'), np.array(Y, dtype='float64')


def sigmoid(x: float) -> float:
    """sigmoid fxn

    Args:
        x (float): x

    Returns:
        float: sigmoid(x) : 1 / ( 1 + np.exp(-1*x) )
    """
    return 1 / (1 + np.exp(-1 * x))

def hypothesis_softmax(x: list,q: list) -> list:
    """hypothesis fxn for softmax

    Args:
        x (list): X : training data
        q (list): Q : theta

    Returns:
        list: Q.T * X
    """
    tempRes = []
    dataCount = x.shape[0]

    for index in range(dataCount):
        tempRes.append( np.dot(q[index], x[index].T) )

    tempRes /= np.sum(tempRes)

    return np.array(tempRes)


if __name__ == "__main__":
    # print("DEFAULT")
    # read file
    x, y = parseCsv(readFile(TRAINING_FILE))
    # set variables
    sampleSize, parameterCount = x.shape
    # set theta ( we use q )
    q = np.random.rand(sampleSize, parameterCount)

    # testing
    y_temp = hypothesis_softmax(x,q)
    print(y_temp.shape)

