import numpy as np
from math import sqrt

TRAINING_FILE = "./train.csv"
TEST_FILE = "./test.csv"

def readFile(fileName):
	fileContent = ""
	try:
		fileObj = open(fileName, 'r')
		fileContent = fileObj.read()
		fileObj.close()
	except:
		fileContent = ""
	return fileContent

def parseFileContent(fileContent):
	trainSet = list()
	resultSet = list()
	try:
		response = fileContent.split("\n")
		response = response[1:-1] # avoid last line \n\n
		lineCount = len(response)
		for ind in range(lineCount):
			response[ind] = response[ind].split(",")
			## data type conversion
			trainSet.append(list(map(float, response[ind][:-1])))
			resultSet.append(response[ind][-1])

	except Exception as e:
		print(e)
		trainSet = []
		resultSet = []
	return [trainSet, resultSet]



training_content = readFile(TRAINING_FILE)
train_set, result_set= parseFileContent(training_content)

# print(train_set)


## 1. SEPRATE BY CLASS
## store as dict, key->class, val=[dataset]

def seprate_by_class(train_set, result_set):
	response = dict()
	dataset_len = len(result_set)
	for i in range(dataset_len):
		if result_set[i] not in response:
			response[result_set[i]] = [ train_set[i] ]
		else:
			response[result_set[i]].append(train_set[i])
	return response

seprated_dataset = seprate_by_class(train_set, result_set)

## UTIL FXN 1.MEAN, 2.STANDARD_DEVIATION

def mean(arr):
	return sum(arr)/float(len(arr))

def variance(arr):
	average = mean(arr)
	variance = sum([(x-average)**2 for x in arr]) / float(len(arr))
	return variance


def get_stats_by_class(seprated_dataset):
	response = dict()
	for obj in seprated_dataset.keys():
		data = seprated_dataset[obj]
		par_count = len(data[0]) # parameter count
		
		## mean and vaieance of each Xi in training set
		mean_list = [ [] for i in range(par_count) ]
		variance_list = [ [] for i in range(par_count) ]
		for ind in range(par_count):
			for indy in range(len(data)):
				mean_list[ind].append(data[indy][ind])
				variance_list[ind].append(data[indy][ind])
		for i in range(par_count):
			mean_list[i] = mean(mean_list[i])
			variance_list[i] = variance(variance_list[i])
		
		## [mean_list, variance_list, prior] -> 0.33 prior given.
		response[obj] = [mean_list, variance_list, 0.33]
	return response

class_stats = get_stats_by_class(seprated_dataset)

# print(len(class_stats))
# for i in class_stats:
# 	print(i)
# 	print(class_stats[i])
				
def getPxy(x, mean, variance):
	"""
	x: float
	mean: mean of class Y
	variance: variance of class Y
	returns P(x|Y=k)
	"""
	exp = 2.718281828
	pi = 3.141592654
	
	val = (exp ** ( ((x-mean)**2)/(-2*variance) )) / ( (2*pi*variance)**0.5 )
	return val

def getProb(inp_list, class_stats):
	"""
	inp_list: list of x's of len 4 in our case
	class_stats: training data
	returns: prob of each class
	"""
	response = dict()
	var_count = len(inp_list)
	for obj in class_stats.keys():
		response[obj] = 1
		for ind in range(var_count):
			response[obj] *= getPxy(inp_list[ind], class_stats[obj][0][ind],class_stats[obj][1][ind])
		response[obj] *= class_stats[obj][2] # prior : 0.33
	return response

### testing and checking

totalCOunt = 0
correct = 0

## testing on trainig set
test_content = readFile(TRAINING_FILE)
test_set, test_result_set= parseFileContent(test_content)
totalCOunt = len(test_set)
correct = 0
for i in range(len(test_set)):
	# print(test_set[i], test_result_set[i])
	# print(f"expected: {test_result_set[i]}")
	resp = getProb(test_set[i], class_stats)
	result = ""
	res_prob = 0
	for obj in resp.keys():
		# print(f"{obj}: {resp[obj]}")
		if (resp[obj] > res_prob):
			res_prob = resp[obj]
			result = obj
	# print(f"Response: {result}")
	if (result == test_result_set[i] ):
		correct+=1
	# print("=================")

print("*******************************")
print(f"train test stats: {correct}/{totalCOunt}")
print("*******************************")


## testiing on testset
test_content = readFile(TEST_FILE)
test_set, test_result_set= parseFileContent(test_content)
totalCOunt = len(test_set)
correct = 0
for i in range(len(test_set)):
	# print(test_set[i], test_result_set[i])
	# print(f"expected: {test_result_set[i]}")
	resp = getProb(test_set[i], class_stats)
	result = ""
	res_prob = 0
	for obj in resp.keys():
		# print(f"{obj}: {resp[obj]}")
		if (resp[obj] > res_prob):
			res_prob = resp[obj]
			result = obj
	# print(f"Response: {result}")
	if (result == test_result_set[i] ):
		correct+=1
	# print("=================")

print("*******************************")
print(f"test stats: {correct}/{totalCOunt}")
print("*******************************")
