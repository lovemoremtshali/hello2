import csv

with open("times.txt", "r") as file:
    data = file.read()
    data = data.replace("[","").replace("]","").split(", ")
    data = [float(i) for i in data]
my = [[i+1, data[i]] for i in range(len(data))]
header=["Rectangle","Time"]
with open('output3.csv', 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    
    writer.writerow(header)
    
    # Write the data to the CSV file
    for row in my:
        writer.writerow(row)