TRAINING_FILE = "./train.csv"
TEST_FILE = "./test.csv"

def readFile(fileName):
	"""read file from disk and put it in cacher as raw string"""
	fileContent = ""
	try:
		fileObj = open(fileName, 'r')
		fileContent = fileObj.read()
		fileObj.close()
	except:
		fileContent = ""
	return fileContent

def parseFileContent(fileContent):
	"""
	parses csv file content and returns 2 array
	trainSet : input var array
	resultSet : correct response
	"""
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
		# print(e)
		trainSet = []
		resultSet = []
	return [trainSet, resultSet]


def mean(arr):
	"""
	mean of array on int/float
	"""
	return sum(arr)/float(len(arr))

def variance(arr):
	"""
	variance of array on int/float
	"""
	average = mean(arr)
	variance = sum([(x-average)**2 for x in arr]) / float(len(arr))
	return variance

def seprate_by_class(train_set, result_set):
	"""
	divides the whole dataset by class
	response -> 
		key: className,
		value: 2d array with each vector as input from trainig data
	"""
	response = dict()
	dataset_len = len(result_set)
	for i in range(dataset_len):
		if result_set[i] not in response:
			response[result_set[i]] = [ train_set[i] ]
		else:
			response[result_set[i]].append(train_set[i])
	return response

def get_stats_by_class(seprated_dataset):
	"""
	return mean and variance of each feature for each class
	response:
		key: className
		value: [ mean_list, variance_list, prior ]
		mean_list: [ mean of each var from all input vector ]
		variance_list: [ variance of each var from all input vector ]
		prior: 1/3, given in the question sheet
	"""
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

def test_trained_model(FILE_NAME, class_stats):
	"""
	FILE_NAME: CSV FILE NAME to test from
	class_stats: response from fxn get_stats_by_class() to access the data classwise
	prints: test stats: {correct}/{totalCount}, correct out of total input size
	"""
	test_content = readFile(FILE_NAME)
	test_set, test_result_set= parseFileContent(test_content)
	totalCount = len(test_set)
	correct = 0

	for i in range(len(test_set)):
		resp = getProb(test_set[i], class_stats)
		result = ""
		res_prob = 0
		for obj in resp.keys():
			if (resp[obj] > res_prob):
				res_prob = resp[obj]
				result = obj
		if (result == test_result_set[i] ):
			correct+=1
		# else:
		#   print(f"expected: {test_result_set[i]}")
		#   for obj in resp.keys():
		#     print(f"{obj}: {resp[obj]}")
		#   print(f"Response: {result}")
		#   print("=================")

	print("**************************************")
	print(f"test stats: {correct}/{totalCount}")
	print("**************************************")



if __name__ == "__main__":
	
	training_content = readFile(TRAINING_FILE)
	train_set, result_set = parseFileContent(training_content)
	seprated_dataset = seprate_by_class(train_set, result_set)
	class_stats = get_stats_by_class(seprated_dataset)

	# test on given test set
	test_trained_model(TEST_FILE, class_stats)

	# test on given training set
	test_trained_model(TRAINING_FILE, class_stats)
	