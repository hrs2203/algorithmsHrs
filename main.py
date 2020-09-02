import sys
searchedWord = set() # words that have appeared previously
countSheet = dict() ## dict to store word count

specialChar = { '"', '.', ',', '”',  '“' }

try:
  e = 101+int(sys.argv[1])
  e = min(281,e)
except:
  e = 281

start=101
end = e

print(f"start={start}, end={end}")

print("search start [", end="")

# print(start,end)
sampleChild = [0 for i in range(end-start)]
for fileCount in range(start, end):
  fileName = f"{fileCount}.txt"
  
  if (fileCount%2==0):
    print("=", end="")

  fileObject = open(f'./th-dataset/{fileName}', "r")
  fileConent = fileObject.read()
  fileObject.close()

  tempFile = ""
  # for i in fileConent:
  #   tempFile += lambda specialChar.__contains__(i): expression
  for i in fileConent:
    if not specialChar.__contains__(i):
      tempFile += i
    else:
      tempFile += " "

  fileConent = tempFile.lower().split()

  for word in fileConent:
    if searchedWord.__contains__(word):
      countSheet[word][fileCount - 101] += 1
    else:
      countSheet[word] = sampleChild.copy()
      countSheet[word][fileCount - 101] = 1
      searchedWord.add(word)

dataset = dict()

print(']')
print(f"Words Found: {searchedWord.__len__()}")

wordSet = countSheet.keys()
for word in wordSet:
  # print(word)
  indx = countSheet[word]
  tempVal = []
  for i in range(end-start):
    if (indx[i]!=0):
      tempVal.append([countSheet[word][i],i]) # [count, index]
      nInd = len(tempVal)-1
      while(nInd > 0 and tempVal[nInd][0] > tempVal[nInd-1][0]):
        cc = tempVal[nInd]
        tempVal[nInd] = tempVal[nInd-1]
        tempVal[nInd-1] = cc
        nInd -= 1

      # dataset[word] = tempVal ## for test
      dataset[word] = [ x[1]+start for x in tempVal ] # store indexes only, not frequency

wordSet = list(dataset.keys())


# outputting in sv file
outputFile = open("output.csv", "w")
for word in wordSet:
  line = ""
  indexes = dataset[word]
  line = f"{word},"
  for i in indexes:
    line+=f"{i},"
  line+="\n"
  # print(line)
  outputFile.write(line)

outputFile.close()


# for i in wordSet:
#   print(f"{i}: {dataset[i]}")

# print("or")
# for i in dataset["or"]:
#   print(i, end=",")
# print()

#for word in searchedWord:
#  print(f"{word} : {countSheet[word]}")
