'File Handling'


'> Opening and Closing Files'
#absolute path
#relative path

#open(path,mode)
file = open("file.txt",'r') #read
file.read() #reads entire content
file.readlines() #reads and returns all lines as a list
file.close()


file = open("file.txt",'w') #write
file.write("New Content ") #Overwrites file with new content
file.writelines(["line1","line2","line3"]) #Overwrites file lines using a list of string
file.close()

open("file.txt", 'a') #append
file.write("New content added to the end of the file")
file.close()
#close files after working with them

#Using Context Managers (with statment)
#automatically closes files
with open("file.txt","r") as file:
    print( file.read() )


'Error Handling'
' it is important to handle errors with files'



