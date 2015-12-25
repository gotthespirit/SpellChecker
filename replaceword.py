#from sugg.py import *
#from pyprofn1.py import *
import shutil
def replaceword(a,b):
    file = open("input.txt","r")
    text = file.read()
    list = text.split(" ")
    file.close()
    file = open("input1.txt","w")
    for i in list:
        if i==a:
            file.write(b + " ")
        else:
            file.write(i + " ")
    file.close()
    shutil.move("input1.txt","input.txt")
if __name__=="__main__":
    replaceword("cor","cot")
