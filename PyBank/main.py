# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:59:54 2019

@author: bonaw
"""

import os
import csv

total_months = 0
net_profit = 0
gr_inc = 0
gr_inc_mth = 0
gr_dec = 0
gr_dec_mth = 0
average = 0


# Set path for file
from os.path import expanduser
home = expanduser("~")
budget_csv = os.path.join(home,"Downloads","PyBank_budget_data.csv")

# Open the CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    row = next(csvreader)
 
    
    #Set counter for months and add total profit/loss for the entire period

    total_months += 1
    net_profit += int(row[1])

    
    for row in csvreader:  
        previous_row = int(row[1])         
        total_months += 1
        net_profit += int(row[1])

        
    #greatest increase     
        if int(row[1]) > gr_inc:
             gr_inc= int(row[1])
             gr_inc_mth = (row[0])
           
        if int(row[1]) < gr_dec:
             gr_dec= int(row[1])
             gr_dec_mth = (row[0])
             
        #average = sum(int(row[0]))
        #average = int(net_profit)/len(net_profit)
                
                
            
        
        
print(f"Total Months: {total_months}")     
print(f"Total: ${net_profit}")   
print(f"Average Change: $ ")
print(f"Greatest Increase in Profits: {gr_inc_mth}, ${gr_inc}")
print(f"Greatest Decrease in Prodits: {gr_dec_mth}, ${gr_dec}")

#Open writer mode and initize csv.writer

output_path = os.path.join(home,"Downloads","PyBank_budget_data_output.csv")    

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    #first row
    csvwriter.writerow(['Financial Analysis'])