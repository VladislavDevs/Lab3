def min_breaks(n : int, m : int, result : int = 0):

    while m - 1 > 0:
        result += 1
        m -= 1

    if n - 1 > 0:
        result += 1
        n -= 1
        m = defaultM

    if m - 1 == 0 and n - 1 == 0:
        print(result)
    else:
        min_breaks(n,m,result)

memo = {}

params = input("Введите размеры шоколадки через запятую: ")
splitedParams = params.split(",")

memoData = input("Введите известные вам данные о шоколадках и насколько минимальных частей они делятся в формате - 1,1:0; : ")

if memoData != "":
    splitedMemo = memoData.split(";")

    for data in splitedMemo:
        chocolateData = data.split(':')

        if chocolateData[0] not in memo:
            memo[chocolateData[0]] = chocolateData[1]

if int(splitedParams[0]) > 0 and int(splitedParams[1]) > 0:
    if params not in memo:
        defaultM = int(splitedParams[1])
        min_breaks(int(splitedParams[0]), defaultM)
    else:
        print(memo[params])
else:
    print("Размеры шоколадки должны быть больше 0")