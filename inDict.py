nolist = []
def returnwrong():
   file1 = open("input.txt", "r")
   text = file1.read()
   words = text.split()
   file2 = open("big.txt", "r")
   content = file2.read()
   Dict = content.split()
   nList = []
   for token in words:
       if token not in Dict: nList.append(token)
   return nList
if __name__=="__main__":
   returnwrong()
