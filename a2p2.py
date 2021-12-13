print("####################################################")
print("#FILENAME:\t\ta2p2.py\t\t\t   #")
print("#ASSIGNMENT:\t\tHomework Assignment 2 Pt. 2#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tMonday, 30.March 2020\t   #")
print("####################################################\n")

dic1 = {'L1':['NY','CT','NH','MA'], 'L2':['TX','NM'], 'L3':['CA','WA','AZ'], 'L4':['ND','SD','WY','ID'], 'L5':['UT'], 'L6':['MN','WI','KY']}

outfile = open("p2output.txt", "w")

for key, value in dic1.items():
    print(key, ":Number of states -- ", len([item for item in value]), sep="")
    print(key, ":Number of states -- ", len([item for item in value]), sep="", file=outfile)
