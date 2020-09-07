import numpy as np

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
	response = list()
	try:
		response = fileContent.split("\n")
		response = response[:-1] # avoid last line \n\n
		lineCount = len(response)
		for ind in range(lineCount):
			response[ind] = response[ind].split(",")
			## data type conversion
			response[ind][:-1] = list(map(float, response[ind][:-1]))

		for i in response:
			print(i)
		print(len(response))

	except Exception as e:
		print(e)
		response = []
	return response



training_content = readFile(TEST_FILE)
trainse_set = parseFileContent(training_content)

