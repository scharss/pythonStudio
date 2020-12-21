import matplotlib.pyplot as plt
years = [1983, 1984, 1985, 1986, 1987]
total_populations = [8939007, 8954518, 8960387, 8956741, 8943721]

plt.plot(years, total_populations)
plt.title("Year vs Population in Bulgaria")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()
#*****************************************
numbers = [0.1, 0.5, 1, 1.5, 2, 4, 5.5, 6, 8, 9]
plt.hist(numbers, bins = 3)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()
#*****************************************
temp = [30, 32, 33, 28.5, 35, 29, 29]
ice_creams_count = [100, 115, 115, 75, 125, 79, 89]
plt.scatter(temp, ice_creams_count)
plt.title("Temperature vs. Sold ice creams")
plt.xlabel("Temperature")
plt.ylabel("Sold ice creams count")
plt.show()
#*******************************
values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]
plt.boxplot(values)
plt.yticks(range(1, 22))
plt.ylabel("Value")
plt.show()
#*********************
labels = ["JavaScript", "Java", "Python", "C#"]
usage = [69.8, 45.3, 38.8, 34.4]
# Generating the y positions. Later, we'll use them to replace them with labels.
y_positions = range(len(labels))
# Creating our bar plot
plt.bar(y_positions, usage)
plt.xticks(y_positions, labels)
plt.ylabel("Usage (%)")
plt.title("Programming language usage")
plt.show()
#*****************************
sizes = [25, 20, 45, 10]
labels = ["Cats", "Dogs", "Tigers", "Goats"]
plt.pie(sizes, labels = labels, autopct = "%.2f")
plt.axes().set_aspect("equal")
plt.show()