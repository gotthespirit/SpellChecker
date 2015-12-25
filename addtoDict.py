import shutil
def addtoDict(a):
    f=0
    file = open("big.txt","a+")
    text = file.read()
    list = text.split("\n")
    file.close()
    file = open("test1.txt","w")
    for i in list:
        if(a<i and f==0):
            file.write(a)
            file.write("\n")
            f=1
        file.write(i)
        file.write("\n")
    file.close()
    shutil.move('test1.txt', 'big.txt')   
if __name__=="__main__":
    addtoDict("cot")
    
