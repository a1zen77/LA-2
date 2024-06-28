# This simple python code reads data from a csv file and stores it in an array of tuples.  
# No external python library (eg. pandas) is required to read the csv file.

Array = []
f = open("data.csv","r")
for i in f.readlines():
    Array.append(i.strip().split(", "))
f.close()

print(Array)