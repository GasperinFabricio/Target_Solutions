import json

file = open("faturamento.json")

data = json.load(file)

listIncome = list()
totalSum = 0


def percent(num_1, num_2):
    return (num_1 / num_2) * 100


for x in range(5):
    data_0 = data[x]
    listIncome.append(data_0)
for x in range(5):
    totalSum += listIncome[x]["faturamento"]

for x in range(5):
    print(f"{listIncome[x]['nome']} %{round(percent(listIncome[x]['faturamento'], totalSum))}\n")