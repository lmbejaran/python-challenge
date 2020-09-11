# Dependecies
import os
import csv

data = {}
net =0
min = 0
max = 0
# Path
budget_csv = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("..", "output", "butget_analysis.txt")
change = 0 
with open(budget_csv,newline ="") as file :
    filereader = csv.reader(file)
    next(filereader)
    previous_row = None
    for row in filereader : 
        data[row[0]] = row[1]
        net = net + int(row[1])
        if previous_row == None:
            previous_row =row[1]
        else:
            difference = int(row[1])-int(previous_row)
            if difference<min:
                min = difference
                date_min =row[0]
            if difference>max:
                max = difference
                date_max = row[0]
            previous_row = row[1]
            change = change+difference
       
    average = round(change/(len(data)-1),2)
    print('Financial Analysis')
    print('-----------------------------')
    print('Total months: ',len(data))
    print('Total' '$',net)
    
 
    print("Average Change: $",average)
    print('Greatest Increase in Profits: '+date_max+' ($'+str(max)+')')
    print('Greatest Decrease in Profits: '+date_min+' ($'+str(min)+')')

 
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)







    
