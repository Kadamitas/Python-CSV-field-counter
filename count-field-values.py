#!/usr/bin/python3
import sys
import csv

#to make it read compatible
argc = len(sys.argv)
if(argc < 2):
    print("\nI guess no files were given, OOOF, so gib summmm (seperated by spaces) \n")
    files = input() #gets files
    files_array = files.split() #turns it into an array ignoring spaces
    argv = files_array #sets it to argv
else:
    argv = sys.argv


associative_array = {} #empty associative_array
exists = False
for i in argv:
    if(i == sys.argv[0]): 
        #this is so I don't read the first thing in argv, obviously this file isnt a csv file
        do_nothing = "nothing"
    else:
        with open (i) as csv_file: #This opens the csv file I guess
            reader = csv.reader(csv_file,delimiter=',') #as specified in the instructions
            line = 0 
            for row in reader: # goes through all the rows
                if(line == 0): #checks if on the first line of the file, the fields list
                    for j in row: #scans through the elments in rows
                        exists = False # 23-28to check if we haven't ran into this in another file
                        for k in associative_array:
                            if(k == j):
                                exists = True
                        if(exists == False):
                            associative_array[j] = 0 #this puts a count for the words
                    line +=1
                else:
                    for j in row: # goes through all the elements in the row
                        for k in associative_array: # scans all the elements in the associative_array
                            if(k == j): #if one of the fields exists, it adds to its count
                                associative_array[k] += 1
                    line+=1 # lets me know im not on the first line

for i in associative_array:
    print(i,associative_array[i]) #prints the array 

