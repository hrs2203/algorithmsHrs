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
    return np.array(X, dtype="float64"), np.array(Y, dtype="int")


def sigmoid(x: float) -> float:
    """sigmoid fxn

    Args:
        x (float): x

    Returns:
        float: sigmoid(x) : 1 / ( 1 + np.exp(-1*x) )
    """
    return 1 / (1 + np.exp(-1 * x))


def hypothesis_softmax(x: list, q: list) -> list:
    """hypothesis fxn for softmax

    Args:
        x (list): X : training data ( 1 X no of paramenters )
        q (list): Q : theta ( output count X no of paramenters )

    Returns:
        list: Q.T * X
    """
    tempRes = np.exp(np.dot(q, x.T))

    tempRes /= np.sum(tempRes)

    return np.array(tempRes)

def getIndex(hypothesis_output: list) -> int:
    """get the class index

    Args:
        hypothesis_output (list): as said

    Returns:
        int: index of output class
    """
    max_index = 0
    max_val = hypothesis_output[max_index]
    for i in range(len(hypothesis_output)):
        if ( hypothesis_output[i] >= max_val ):
            max_val = hypothesis_output[i]
            max_index = i
    return max_index


def cost_fxn(x: list, y: list, q: list) -> float:
    """cost fxn for softmax logistic regression

    Args:
        x (list): training
        y (list): training output
        q (list): theta

    Returns:
        float: cost of hypothesis
    """
    totalCost = 0

    itemCount = x.shape[0]
    for index in range(1):
        totalCost += np.log(hypothesis_softmax(x[index], q)[y[index][0]])

    return -1 * totalCost


if __name__ == "__main__":
    # print("DEFAULT")

    # read file
    x, y = parseCsv(readFile(TRAINING_FILE))

    # set variables
    sampleSize, parameterCount = x.shape
    outputCount = len(set(y))
    y = y.reshape((y.shape[0], 1))

    # set theta ( we use q )
    q = np.random.rand(outputCount, parameterCount)

    # testing
    print("============= pre training =========== ")
    # y_res = hypothesis_softmax(x[0], q)
    completeLoss = cost_fxn(x, y, q)
    print(f"cost: {completeLoss}")
    # =============== accuracy ===============
    correctCount = 0
    for ind in range(sampleSize):
        correctCount += int(getIndex( hypothesis_softmax( x[ind], q ) ) == y[ind][0])
    print(f"accuracy: {(correctCount / sampleSize)* 100}")
    # ========================================

    # count = 80
    # while count > 0:
    #     count -= 1
    #     #  ========= start training =============

    #     #  =========  end training  =============

    print("============ post training =========== ")
    # y_res = hypothesis_softmax(x, q)
    completeLoss = cost_fxn(x, y, q)
    print(f"cost: {completeLoss}")
    # =============== accuracy ===============
    correctCount = 0
    for ind in range(sampleSize):
        correctCount += int(getIndex( hypothesis_softmax( x[ind], q ) ) == y[ind][0])
    print(f"accuracy: {(correctCount / sampleSize)* 100}")
    print("====================================== ")
