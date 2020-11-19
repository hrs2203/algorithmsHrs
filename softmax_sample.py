import numpy as np
import csv
import matplotlib.pyplot as plt


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
    """get the output class index

    Args:
        hypothesis_output (list): as said

    Returns:
        int: index of output class
    """
    max_index = 0
    max_val = hypothesis_output[max_index]
    for i in range(len(hypothesis_output)):
        if hypothesis_output[i] >= max_val:
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


def indicator_fxn(y, k):
    """ int(y===k) """
    return int(y == k)


def get_gradient(x, q, y):
    correction = np.zeros(q.shape)
    dataCount = x.shape[0]
    parameterCount = x.shape[1]
    outputCount = q.shape[0]

    for index in range(dataCount):
        x_temp = x[index]
        new_hypo = hypothesis_softmax(x_temp, q)
        temp_output = getIndex(new_hypo)
        temp_hypo = np.zeros(new_hypo.shape)
        for ind in range(outputCount):
            if ind == temp_output:
                temp_hypo[ind] = 1 - new_hypo[ind]
            else:
                temp_hypo[ind] = -new_hypo[ind]

        for i in range(outputCount):
            correction[i] += x_temp * temp_hypo[i]

    correction /= dataCount

    return correction


if __name__ == "__main__":
    # print("DEFAULT")

    # read file
    x, y = parseCsv(readFile(TRAINING_FILE))

    # set variables
    sampleSize, parameterCount = x.shape
    outputCount = len(set(y))
    alpha = 0.001
    y = y.reshape((y.shape[0], 1))

    # set theta ( we use q )
    q = np.random.rand(outputCount, parameterCount)

    # testing
    print("============= pre training =========== ")
    # y_res = hypothesis_softmax(x[0], q)
    # ============== calc cost ===============
    completeLoss = cost_fxn(x, y, q)
    print(f"cost: {completeLoss}")
    # =============== accuracy ===============
    correctCount = 0
    for ind in range(sampleSize):
        correctCount += int(getIndex(hypothesis_softmax(x[ind], q)) == y[ind][0])
    print(f"accuracy: {(correctCount / sampleSize)* 100}")
    # ========================================

    # grad = get_gradient(x,q,y)
    # print(grad.shape)
    # print(q.shape)

    tempCost = []

    count = 500
    print("========== training start ============ ")
    while count > 0:
        count -= 1
        # print(count, end=",")
        #  ========= start training =============
        temp_grad = get_gradient(x, q, y)
        print(f"{count},{temp_grad.shape}")
        q = q - (alpha * temp_grad)
        tempCost.append(cost_fxn(x, y, q))

        #  =========  end training  =============
    print("\n============ training end ============ ")

    print("============ post training =========== ")
    # y_res = hypothesis_softmax(x, q)
    # ============== calc cost ===============
    completeLoss = cost_fxn(x, y, q)
    print(f"cost: {completeLoss}")
    # =============== accuracy ===============
    correctCount = 0
    for ind in range(sampleSize):
        correctCount += int(getIndex(hypothesis_softmax(x[ind], q)) == y[ind][0])
    print(f"accuracy: {(correctCount / sampleSize)* 100}")
    # ========================================
    print("====================================== ")
    plt.plot(tempCost)
    plt.show()

