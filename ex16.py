#Reading and writing files

from sys import argv

script, filename = argv

print (f"We're going to erase {filename}")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN")

input("?")

print ("Opening the file....")
target = open(filename, 'w')

print ("truncating the file.****Goodbye!!!")
target.truncate()

print ("Now I'm going to ask you for four lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
line4 = input("Line 4: ")

print ("I'm going to write these to file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)

print ("And finally, we close it!!!")
target.close()
