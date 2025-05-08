# Imports the modules that support arguments being passed by the user
from sys import argv 

# listed variables that can be passed as arguments
script, filename = argv

#Variable 'txt' = the function open with filename passed to it
txt = open(filename)

#Print the name of the file choosen/created
print (f"Here's your file {filename}:")
#Print the 'txt' variable after you pass it to the read function
print (txt.read())

#Ask the user to type the file name again but ask then for 'input' instead of argv arguments
print ("Type the filename again:")
file_again = input("> ")

#Create variable txt_again ad pass that variable to print and .read
txt_again = open(file_again)
print (txt_again.read())

# Close the file using the close() method on the file object
file_again.close()
