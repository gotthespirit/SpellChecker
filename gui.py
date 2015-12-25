from Tkinter import *
from sugg import *
from inDict import *
from addtoDict import *
from replaceword import *
window = Tk()
frame1 = Frame(window,width = 100,height = 100)
frame1.pack(side=TOP)
frame2 = Frame(window)
frame2.pack(side = BOTTOM)
class searchtext:
        def __init__(self,master):    
                self.entertext = Text(master,width=160,height=10)#creates an entry box
                self.entertext.pack(fill=X)   
                frame1 = Frame(master,width = 100,height = 100)#creates a frame in the window of height 100 and width 100
                frame1.pack(side=TOP)#packs frame in the left side of the window    
                #self.button1 = Button(frame1,text="Add to dictionary",command=self.printmessage)#creates a button inside frame1
               #self.button1.grid(row=0,column=1,padx=100,pady=4)
                self.button3 = Button(frame1,text="Submit",command=self.printmessage)#creates a button inside frame1
                self.button3.grid(row = 0,column = 2,padx = 100,pady = 4)
                self.button4 = Button(frame1,text = "Quit",command = quit)#creates a button inside frame1
                self.button4.grid(row = 0,column = 3,padx = 100,pady = 4)
        def printmessage(self):
                input = self.entertext.get("1.0",'end-1c')
                file = open("input.txt","w")
                file.write(input)
                file.close()
                nlist = returnwrong()
                print nlist
                c=0   
                var = [""]*20
                for i in nlist:
                        wW = wrongWord(i, "big.txt")
                        wW.readDict()
                        wW.sortLen()
                        suggestions = wW.suggWords()
                        suggestions.append("Add")
                        print suggestions
                        #for j in suggestions:
                         #       Button(frame1,text = j,command = replaceword(i,j)).pack()
                        var[c] = StringVar(frame1)
                        var[c].set(i) # initial value
                        option = apply(OptionMenu, (frame1, var[c]) + tuple(suggestions))
                        option.grid(row = 0, column = c)
                        c += 1
                        #button = Button(master, text="OK", command=ok)
                        #button.pack()
                def confirm():
                    for i in range(c):
                        if(var[i].get()!="Add"):
                            replaceword(nlist[i], var[i].get())
                        else:
                            addtoDict(str(nlist[i]))
                    file = open("input.txt", "r")
                    text = file.read()
                    cwords = Label(frame2, text = text)
                    cwords.pack()
                    file.close()
                ok = Button(frame1, text = "Confirm Changes", command = confirm)
                ok.grid(row = 0, column = c)

frame2.quit()
search = searchtext(window)
window.title("Spell Checker")
file = open("input.txt")
text = file.read()
print text
file.close()
window.mainloop()



