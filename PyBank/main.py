# Pull CSV

import os
import csv
#budget_data = os.path.join('c:', 'Users', 'joelc', 'Documents', 'python-challenge' , 'PyBank', 'Resources', 'budget_data.csv')
budget_data = os.path.join('Resources', 'budget_data.csv')
#Total number of Months included in Data Set
 
Months= ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header= next(budget_data)
    

    total = 0

    for row in csvreader:
        if row[0]== Months['....']:
            total= total + 1
            Print (total)
        
         #sum of Prifit/Losses
        print (sum[row(1)])
         #average
        print(average[row(1)])


    




