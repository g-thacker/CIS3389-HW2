print("####################################################")
print("#FILENAME:\t\ta2p1.py\t\t\t   #")
print("#ASSIGNMENT:\t\tHomework Assignment 2 Pt. 1#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tMonday, 30.March 2020\t   #")
print("####################################################\n")

given_string = "Sam works in a company abc in New York. He joined the company last year 2019. Before joining ABC, he used to work for a small firm in Arizona. He worked there from 2015 to 2018. Before moving to Arizona Sam used to live in South Dakota and he has been living there since 2000's."

outfile = open("p1output.txt", "w")

#1a
string_as_list = list(given_string.replace("."," ").replace("'"," ").replace(","," ").split(" "))
year_list = []
for i in range(0,len(string_as_list)):
    if string_as_list[i].isdigit():
        if len(string_as_list[i]) == 4:
            year_list.append(string_as_list[i])

print("1a:")
print(year_list)
# In the instructions it was unclear whether the output format for the textfile made use of multiple spaces or tabs. I'm hoping either would be fine, and went with tabs because I think they look cleaner (you can easily tell a tab is being used by glancing at the code, whereas it's difficult to judge how many spaces are being used)
print("a.\tThe list of years:", year_list, file=outfile)

#1b
count = 0
search_string = "abc"
count = given_string.lower().count("abc")

print("\n1b:")
print('Occurances of "abc" in string:', count)
print("Maximum year value in string:", max(year_list))
print("Minimum year value in string:", min(year_list))
print("b.\tCount: ", count, ", Maximum: ", max(year_list), ", Minimum: ", min(year_list), sep="", file=outfile)

#1c

new_string = given_string.replace("h","_")
print("\n1c:")
print(new_string)
print("c.\tThe new string:", new_string, file=outfile)
