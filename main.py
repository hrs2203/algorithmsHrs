import sys, time
searchedWord = set() # words that have appeared previously
countSheet = dict() ## dict to store word count

specialChar = { '"', '.', ',', '”',  '“', "'" }

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

# ordering doc ids
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
      
      # [count, index]
      dataset[word] = [ [x[0],x[1]+start] for x in tempVal ] # store indexes only, not frequency

wordSet = list(dataset.keys())

# startTime = time.time()
# # outputting in sv file
# outputFile = open("output.csv", "w")
# for word in wordSet:
#   line = ""
#   indexes = dataset[word]
#   line = f"{word},"
#   for i in indexes:
#     line+=f"{i},"
#   line+="\n"
#   # print(line)
#   outputFile.write(line)

# outputFile.close()
# endTime = time.time()
# print(f"save time {endTime-startTime}")

# New output format
# Stuart (8) ==> {165=2, 189=1, 248=2, 249=1, 180=1, 108=1, 280=1, 252=1}
# Raju (3) ==> {198=1, 118=1, 183=1}
# informal (1) ==> {192=1}
# Pooja (2) ==> {279=1, 269=1}
# rival (7) ==> {211=1, 169=1, 237=2, 194=1, 151=2, 250=1, 251=1}
# Valencia (3) ==> {201=1, 203=1, 105=1}

startTime = time.time()
# outputting in sv file
outputFile = open("output.csv", "w")
for word in wordSet:
  line = ""
  indexes = dataset[word]
  line = f"{word} ({len(indexes)}) ==> "
  line += "{"
  for i in indexes:
    line+=f" {i[1]}={i[0]},"
  line+="}\n"
  # print(line)
  outputFile.write(line)

outputFile.close()
endTime = time.time()
print(f"save time {endTime-startTime}")

# for i in wordSet:
#   print(f"{i}: {dataset[i]}")

# print("or")
# for i in dataset["or"]:
#   print(i, end=",")
# print()

#for word in searchedWord:
#  print(f"{word} : {countSheet[word]}")
