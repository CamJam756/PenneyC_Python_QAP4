# Comment like a pro.
# Date Written: March 26th, 2023
# Author: Cameron Penney

# Import matplotlib library as plt.
import matplotlib.pyplot as plt

# Creates an empty list called Y_Values.
Y_Values = []

# Ask the user for total sales for each month of the year.
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']\

# Tells the user what the program is.
print()
print("==================================")
print("----Total sales for each month----")
print("==================================")

# Create loop to gather all sales for each month and add them to Y_Values.
for month in Months:
    while True:
        print()
        try:
            Sales = float(input(f"Enter total sales for {month}: "))
            if Sales < 0:
                print()
                print("Sales amount must not be a negative number - please reenter")
        except:
            print()
            print("Invalid input - please enter a number")
        else:
            Y_Values.append(Sales)
            break

# Creates a list of month names to use as x-axis labels.
X_Values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Creates a figure and axis object.
fig, ax = plt.subplots()

# Create a bar plot with Y_Values and the list of abbreviated months as the X-Axis.
ax.bar(X_Values, Y_Values)

# Set the title and axis labels.
ax.set_title('Total Sales by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Total Sales ($)')

# Show the plot.
plt.show()