# Pull CSV

import os
import csv
#budget_data = os.path.join('c:', 'Users', 'joelc', 'Documents', 'python-challenge' , 'PyBank', 'Resources', 'budget_data.csv')
budget_data = os.path.join('Resources', 'budget_data.csv')
#Total number of Months included in Data Set
 
# Months= ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
total=0
total_net=0
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",99999999999]


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header= next(csvreader)
    jan_data= next(csvreader)

    total=total+1
    total_net=total_net+int(jan_data[1])
    previous_net=int(jan_data[1])  

    for row in csvreader:
        total=total+1
        total_net=total_net+int(row[1])
        
        change= int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list= net_change_list+ [change]

        if change > greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]= row[0]

        if change < greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]= row[0]

average_change= round(sum(net_change_list)/len(net_change_list),2)

print(total)
print(total_net)
print(average_change)
print(greatest_increase[0], greatest_increase[1])
print(greatest_decrease[0], greatest_decrease[1])

    


    




