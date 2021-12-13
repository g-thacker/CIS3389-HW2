print("####################################################")
print("#FILENAME:\t\ta2p3.py\t\t\t   #")
print("#ASSIGNMENT:\t\tHomework Assignment 2 Pt. 3#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tMonday, 30.March 2020\t   #")
print("####################################################\n")

a = {5:'New York',2:'Dallas',6:'San Marcos'}
b = {2:'Texas',4:'San Fransisco'}
c = {3:'Phoenix',1:'Arizona'}

new_dictionary = {}
for i in (a, b, c):
    new_dictionary.update(i)
print(new_dictionary,"\n")
# Making the assumption by "the second element" you mean the element associated with index 2 (proceded by the zeroth and first elements), rather than the element associated with index 1 (the "second" element using conventional counting)
print(new_dictionary[2],"\n")

for key in sorted(new_dictionary.keys(), reverse = True):
    print(key, ':', new_dictionary[key])
