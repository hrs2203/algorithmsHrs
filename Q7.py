import requests as req

# https://jsonmock.hackerrank.com/api/article_users?page=1

def getData():
	allData = []
	page = 1
	url = (f'https://jsonmock.hackerrank.com/api/article_users?page={page}')
	resp = req.get(url).json()
	totalPage = resp['total_pages']

	for page in range(1,totalPage+1):
		url = (f'https://jsonmock.hackerrank.com/api/article_users?page={page}')
		resp = req.get(url).json()
		for res in resp['data']:
			newData = dict(
				username = res["username"],
				submission_count = res["submission_count"]
			)
			allData.append( newData )

	return allData

def getList(threshold):
	data = getData()
	result = []
	for item in data:
		if ( item['submission_count'] > threshold ):
			result.append(item['username'])
	return result

def main():
	threshold = int(input())
	result = getList(threshold)
	for i in result:
		print(i)

if __name__ == '__main__':
	main()
