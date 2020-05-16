import requests as req
import calendar, datetime

# https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber>

def timestamp_range(month):
    def days_in_month(dt):
        return calendar.monthrange(dt.year, dt.month)[1]
    t1 = datetime.datetime.strptime(month, "%m-%Y")
    t2 = t1 + datetime.timedelta(days_in_month(t1))
    return [int(t1.timestamp() * 1000), int(t2.timestamp() * 1000)]

def getData(status):
	allData = []
	page = 1
	url = (f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={status}&page={page}')
	resp = req.get(url).json()
	totalPage = resp['total_pages']

	for page in range(1,totalPage+1):
		url = (f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={status}&page={page}')
		resp = req.get(url).json()
		for res in resp['data']:
			newData = dict(
				status = res["status"],
				timestamp = res["timestamp"],
				rootThreshold = res["operatingParams"]["rootThreshold"]
			)
			allData.append( newData )

	return allData

def filterData(status, threshold, timeRange):
	allData = getData("STOPPED")
	result = []
	for item in allData:
		if (item['rootThreshold'] > threshold) and ( item['timestamp']>=timeRange[0] ) and ( item['timestamp']<=timeRange[1] ):
			result.append(item)
	return result

def main():
	status = str(input())
	threshold = int(input())
	timestamp = str(input())
	timeRange = timestamp_range(timestamp)
	allData = filterData("STOPPED", 45, timeRange)
	print( len(allData) )



if __name__ == '__main__':
	main()