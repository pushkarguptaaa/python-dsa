# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")

print(arr)

avgTemp= sum(arr[0:7])/len(arr[0:7])
print(avgTemp)

maxTemp= max(arr[0:10])
print(maxTemp)

weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")

print(weather_dict)

print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

with open("poem.txt","r") as f:
    for line in f:
        print(line)

word_count = {}
with open("poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1

print(word_count)
