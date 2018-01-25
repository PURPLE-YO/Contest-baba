import csv

cityDict = {}
with open('CityData.csv',newline='') as csvFile:
    cityReader = csv.reader(csvFile, delimiter=' ', quotechar='|')

    # Map city data as (cityID, tuple(x,y)) in dictionary

    for row in cityReader:
        print(row)
        item = row[0].split(',')
        try:
            newTuple = (int(item[1]), int(item[2]))
            cityDict[int(item[0])] = newTuple
        except ValueError:
            continue
    print(cityDict.items())







