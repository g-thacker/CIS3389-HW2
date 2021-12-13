print("####################################################")
print("#FILENAME:\t\ta2p4.py\t\t\t   #")
print("#ASSIGNMENT:\t\tHomework Assignment 2 Pt. 4#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tMonday, 30.March 2020\t   #")
print("####################################################\n")


import re, os, csv

path = "./p4/"

outfile = open("p4output.csv", "w", newline = "")
writer = csv.writer(outfile)
in_files = os.listdir(path)

writer.writerow(["FileName","Substring"])
for file in in_files:
    this_path = os.path.join(path, file)
    this_file = open(this_path, "r")
    contents = this_file.read()
    if "lives" in contents:
        writer.writerow([file, contents.partition("lives")[2]])
    elif "live" in contents:
        writer.writerow([file, contents.partition("live")[2]])

print('[Data written to "p4output.csv"]')
