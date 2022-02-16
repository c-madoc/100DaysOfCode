import pandas
# data = pandas.read_csv("weather_data.csv")
#
# temps = data['temp'].to_list()
#
# print(data.temp.mean())
# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_in_f = (int(monday.temp) * 1.8) + 32
#
# print(f"C: {int(monday.temp)}\nF:{monday_temp_in_f}")

# Get the entire dataset into a Pandas Dataframe
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the different data points for what we are looking for
gray = data[data['Primary Fur Color'] == "Gray"]
red = data[data['Primary Fur Color'] == "Cinnamon"]
black = data[data['Primary Fur Color'] == "Black"]

# Build dict of colors and count
data_dict = {
    "Fur Color": ['gray', 'red', 'black'],
    "Count": [len(gray), len(red), len(black)]
}

# Create a new dataframe with from the dict
new_data = pandas.DataFrame(data_dict)

# Save a new csv file with the data we collected
new_data.to_csv("squirrel_count.csv")