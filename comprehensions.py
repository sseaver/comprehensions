def remove_vowels():
    sentence = "List Comprehensions are the Greatest!"
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = [letters for letters in sentence if letters not in vowels]
    return "".join(no_vowels)
print ("========Vowels Removed=======")
print (remove_vowels())

###############################################
with open("data_file.txt") as data:
    data = data.readlines()
data_sets = []
for items in data:
    items = items.replace("\n", "")
    items = items.split(",")
    data_sets.append(items)

def water_temps():
    target_column = [row[4] for row in data_sets]
    target_column.pop(0)
    target_column = [float(item) for item in target_column]
    return target_column
print ("-----Water temperatures-----")
print(water_temps())

def celcius_to_fahrenheit(celc):
    temp = [int(temperature * (9 / 5) + 32) for temperature in celc]
    return temp
target_column = water_temps()
print ("***Celcius to Fahrenheit***")
print (celcius_to_fahrenheit(target_column))

dates = [row[5] for row in data_sets]
dates.pop(0)
dates = [(item) for item in dates]

waves = [row[1] for row in data_sets]
waves.pop(0)
waves = [float(item) for item in waves]

my_dict = dict(zip(dates, waves))
print ("~~~Dictionary of dates and waves~~~")
print (my_dict)
