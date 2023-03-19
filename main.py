import json

file = open("dados.json")

data = json.load(file)
listMonth = list()

for x in range(30):
    data_0 = data[x]
    listMonth.append(data_0)

smallerValue = 999999
smallerValueDay = 0
biggestValue = 0
biggestValueDay = 0
sumValue = 0
sumCount = 0
sumAverage = 0
countAboveAverage = 0


for x in range(30):
    if smallerValue > listMonth[x]["valor"] > 0:
        smallerValue = listMonth[x]["valor"]
        smallerValueDay = listMonth[x]["dia"]
    if listMonth[x]["valor"] > biggestValue:
        biggestValue = listMonth[x]["valor"]
        biggestValueDay = listMonth[x]["dia"]
    if listMonth[x]["valor"] > 0:
        sumValue += listMonth[x]["valor"]
        sumCount += 1
sumAverage = (sumValue / sumCount)

for x in range(30):
    if listMonth[x]["valor"] > sumAverage:
        countAboveAverage += 1

print(f"The biggest value is {biggestValue} on day {biggestValueDay}\n"
      f"The smallest value is {smallerValue} on day {smallerValueDay}\n"
      f"The amount of times where invoice is larger than the average is {countAboveAverage}")





file.close()