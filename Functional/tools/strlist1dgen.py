import sys


def strlist1dgen(list_name,str):
    print(f"{list_name} = [", end = "")
    for i in range (0,len(str)):
        if i == len(str)-1:
            print(f'"{str[i]}"]')    
        else:
            print(f'"{str[i]}",', end = "")
    
    

if len(sys.argv) == 3:
    strlist1dgen(sys.argv[1],sys.argv[2])
else:
    print("Command must include 2 arguments: list_name and str")
    print("example: python strlist1dgen.py list1d abcdefg")

        