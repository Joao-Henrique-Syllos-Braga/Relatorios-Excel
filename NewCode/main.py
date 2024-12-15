from total_values import totalData
from setData import data
from printData import printData

data = data()
totalData(data)

first_line = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December", "Total"]
data.insert(0, first_line)

printData(data)