# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26, 2019
@author: Mike
"""
import csv

input_filename = 'AllTheDataV0.csv'
output_filename = 'viagraV1.csv'

# An additional fiddle to the input file to make the code easy.
# I moved the column DECLIN to the first position for performance.
# It represents whether a clinical determination of dementia has been made.
DECLIN = 1

def update_csv(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)




for row in reader:
    if row[DECLIN] == -4

    # do nothing to this row 
    writer.writerow(row)
    else:
          
      """
      check the drugs listed in columns 76  to 114 
      if row[DRUGx] == 'SILDENAFIL' or 'TADALAFIL'  
      put FOUND-YES indicator in row[115] # we just happen to have an empty column
      write the row
      else
      put FOUND-NO indicator in row[115]
      write this row, get next
      """
      writer.writerow(row)

    


input_filename.close
output_fileout.close

