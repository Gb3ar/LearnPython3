format = "{} {} {} {}"

print (format.format (1,2,3,4))
print (format.format ("one", "two", "three", "four"))
print (format.format (True, False, False, True))
print (format.format (format, format, format, format))
print (">>>>>>   Is there"
                "A reason" 
                "This is thoughing an error?" 
                "today")

print (format.format (
                "Is there", 
                "A reason", 
                "This is thoughing an error?", 
                "today")) 

print (">>>>>>")