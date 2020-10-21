#Final_Project
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


class Inventory: #define a new class
    Numberlist=[] # this is the Inventory property that used to store the data
    def __init__(self,root): # define the initial state when the program is excuted
        # the blank frame which included all the buttons, labels and textfield
        mainframe = ttk.Frame(root,relief=SUNKEN, padding="5 5 5 5")
        mainframe.grid(row=0,column=0,sticky=(N,E,W,S))
        mainframe.grid_rowconfigure(0,weight=5)
        mainframe.grid_columnconfigure(0,weight=5)
        # Labels for five attributes associated with one specified item
        # Text fields for five attributes associated with one specified item
        ItemNumber = ttk.Label(mainframe,text="编号")
        ItemNumber.grid(row=0,column=0,sticky=W)
        NUM = Text(mainframe,width=15,height=2,bg='lightGrey',fg='black')
        NUM.grid(row=0,column=1,sticky=W)
        Quantity = ttk.Label(mainframe,text="数量")
        Quantity.grid(row=1,column=0,sticky=W)
        QUA = Text(mainframe,width=15,height=2,bg='lightGrey',fg='black')
        QUA.grid(row=1,column=1,sticky=W)
        ItemName = ttk.Label(mainframe,text="名字")
        ItemName.grid(row=2,column=0,sticky=W)
        NAME = Text(mainframe,width=15,height=2,bg='lightGrey',fg='black')
        NAME.grid(row=2,column=1,sticky=W)
        ItemLocation = ttk.Label(mainframe,text="产地")
        ItemLocation.grid(row=3,column=0,sticky=W)
        LOCA = Text(mainframe,width=15,height=2,bg='lightGrey',fg='black')
        LOCA.grid(row=3,column=1,sticky=W)
        ItemDescri=ttk.Label(mainframe,text="描述")
        ItemDescri.grid(row=4,column=0,sticky=W)
        DES = Text(mainframe,width=40,height=3,bg='lightGrey',fg='black')
        DES.grid(row=4,column=1,columnspan=2,sticky=W)
        # All buttons with different function which are placed in the mainframe
        # All buttons with name are gridded in right place.
        New = ttk.Button(mainframe, text = '添加',command=lambda:self.addInfo(NUM,QUA,NAME,LOCA,DES))
        New.grid(row=0,column=2,pady=5)
        Delete = ttk.Button(mainframe, text = '删除',command=lambda:self.DelInfo(NUM,QUA,NAME,LOCA,DES))
        Delete.grid(row=1,column=2,pady=5)
        Search = ttk.Button(mainframe, text = '查询',command=lambda:self.searchItem(NUM,QUA,NAME,LOCA,DES))
        Search.grid(row=2,column=2,pady=5)
        Update = ttk.Button(mainframe, text = '更新',command=lambda:self.Update(NUM,QUA,NAME,LOCA,DES))
        Update.grid(row=0,column=3,pady=5)
        Load = ttk.Button(mainframe, text = '导入',command=lambda:self.LoadFile(NUM,QUA,NAME,LOCA,DES))
        Load.grid(row=1,column=3,pady=5)
        Save = ttk.Button(mainframe, text = '保存',command=lambda:self.SaveFile())
        Save.grid(row=2,column=3,pady=5)
        #additonal function buttons
        #Show button is associated with a function that will show out all the inventory information with widget
        #Clear button is used to clear out the information in text field
        Show = ttk.Button(mainframe, text = '展示库存',command=lambda:self.showall())
        Show.grid(row=3,column=3,pady=5)
        Clear = ttk.Button(mainframe, text = '清除',command=lambda:self.cleartext(NUM,QUA,NAME,LOCA,DES))
        Clear.grid(row=3,column=2,pady=5)



    # this method is used for another method, merge_sort.
    # This method will sort two lists in increasing rank based on the first number in the list.
    def merge_base(self,a,b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0][0] < b[0][0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    # merge_sort will sort many lists in a increasing rank based on the first number in a list.
    # using the divide and conquer to solve the problem
    def merge_sort(self,data): 
        if len(data) == 0 or len(data)==1:
            return data
        else:
            m = len(data)//2
            a = self.merge_sort(data[:m])
            b = self.merge_sort(data[m:])
            return self.merge_base(a,b)

    #This "check" method is used to check if the item Number is existed in the Inventory List.
    def check(self,blist,a):
        for i in blist:
            if a == i[0]:
                return False #if the item is existed, it will return False
        return True # if the item is not existed, it will return True

    
    # this is the command function associated with the "New" button
    def addInfo(self,text1,text2,text3,text4,text5):
        try:
            #get the values that the user enter in the text field
            a = text1.get(1.0,END)[:-1]
            if a == '':
                raise TypeError #The itemNumber text field cannot be empty
            k = int(a)
            b = text2.get(1.0,END)[:-1]
            c = text3.get(1.0,END)[:-1]
            d = text4.get(1.0,END)[:-1]
            e = text5.get(1.0,END)[:-1]
            if self.check(self.Numberlist,k):#using the "check" method above
                if a == '' or b =='' or c=='' or d=='' or e=='':
                    messagebox.showerror('Error','Please enter information into all the text field')
                elif int(b)==ValueError:
                    raise ValueError
                else:
                    self.Numberlist.append([k,b,c,d,e])# "check" return True that means the item is not existed then user can add in the inventory list
                    self.Numberlist=self.merge_sort(self.Numberlist) #using merge_sort to sort the inventory list in increasing order
                    #clear all the values in five text fields.
                    self.cleartext(text1,text2,text3,text4,text5)
            else: # "check" return False that mean the item is existed then a messagebox will warn the user.
                messagebox.showinfo('Already Existed','The item is already existed. You can update the information using the update button.')
        except TypeError:
            messagebox.showerror('Error','Item Number text field can not be empty.')
        except ValueError: # the user can only enter number into ItemNumber and ItemQuantity text fields, or a messagebox will warn the user
            messagebox.showerror('Error','You can only enter number in ItemNumber and ItemQuantity text field.')


    #BinarySearch method, which is used for the "Search" button ,"Delete" button and "Update" button.
    #this method search the position of the target by entering ItemNumber
    #BinarySearch is more efficient than linear search.
    def BinarySearch(self,blist, num):
        lower = 0
        upper = len(blist)
        while lower < upper:   
            mid = lower + (upper - lower) // 2
            searchItem = blist[mid][0]
            if num == searchItem:
                return mid 
            elif num > searchItem:
                if lower == mid:   
                    break   
                lower = mid
            elif num < searchItem:
                upper = mid
        return -1 #if the item can not be searched, it will return -1

    #this is the method associated with the "Delete" button.
    def DelInfo(self,text1,text2,text3,text4,text5):
        try:
            if messagebox.askokcancel("Delete", "Confirm to delete, please."):#when the user clicker the Delete button, it will show up a messagebox for user to confirm. If the user click "ok", it will return the true value,so the following command line will be executed.
                a = text1.get(1.0,END)[:-1]
                if a == '':
                    raise TypeError
                k = int(a)
                pos = self.BinarySearch(self.Numberlist,k)
                if pos == -1:# using binarySearch to get the position but return -1 means that Item is not existed.
                    messagebox.showinfo('Error','Item is not existed.')#show up a messagebox to inform the user.
                    #clear the text fields
                    self.cleartext(text1,text2,text3,text4,text5)
                else:# the item is existed.
                    self.Numberlist=self.Numberlist[:pos]+self.Numberlist[pos+1:]#clear the information of that item
                    self.cleartext(text1,text2,text3,text4,text5)
                    messagebox.showinfo('successful',"The item is deleted.")
            else:#user click the cancel button, then the selected item will not be deleted.
                pass
        except TypeError:
            messagebox.showerror('Error','Item Number text field can not be empty.')
        except ValueError:# the user can only enter number into ItemNumber and ItemQuantity text fields, or a messagebox will warn the user
            messagebox.showerror('Error','Please enter the correct number in Item Number text field')

    #this is the method assoicated with the Update button
    def Update(self,text1,text2,text3,text4,text5):
        try:
            #get the information in the text field
            a = text1.get(1.0,END)[:-1]
            if a == '':
                raise TypeError
            k = int(a)
            b = text2.get(1.0,END)[:-1]
            c = text3.get(1.0,END)[:-1]
            d = text4.get(1.0,END)[:-1]
            e = text5.get(1.0,END)[:-1]
            pos = self.BinarySearch(self.Numberlist,k)
            if pos == -1: # item is not in the inventory list, then user can not update.
                messagebox.showinfo('Not Existed','Item is not existed. You can not update the information.')
            else:
                # if the text field has information then, it will update and store in the inventory list
                # if the text field is empty, the information in the inventory list will not be changed
                if b!='':
                        if int(b) == ValueError:# the ItemQuantity only can be number
                            raise ValueError #if the information in ItemQuantity Text field is not a number, it will raise exception
                        else:
                            self.Numberlist[pos][1]=b
                if c !='':
                    self.Numberlist[pos][2]=c
                if d !='':
                    self.Numberlist[pos][3]=d
                if e !='':
                    self.Numberlist[pos][4]=e
            # Delete all the information in the text field
            self.cleartext(text1,text2,text3,text4,text5)
        except TypeError:
            messagebox.showerror('Error','Item Number text field can not be empty.')
        except ValueError:
            messagebox.showerror('Error','You can only enter number in ItemNumber and ItemQuantity text field.')

    
    #this is the method associated with the Search button.
    def searchItem(self,text1,text2,text3,text4,text5):
        try:
            a = text1.get(1.0,END)[:-1]
            if a =='':
                raise TypeError
            itemnum = int(a)#get the itemNumber that the user wants to search
            pos = self.BinarySearch(self.Numberlist,itemnum)#search the position in the inventory list
            self.cleartext(text1,text2,text3,text4,text5)
            if pos == -1:#item can not be found
                messagebox.showinfo('Not Existed','Item is not existed.')
            else:
                #insert information of a specified item into the corresponding text fields.
                self.insertAllInfo(text1,text2,text3,text4,text5,pos)
        except TypeError:
            messagebox.showerror('Error','Item Number text field can not be empty.')
        except ValueError: # user enter the wrong ItemNumber
            messagebox.showerror('Error','You can only enter number in ItemNumber and ItemQuantity text field.')

    

    #this method associated with the Load Button.
    #used to load a file in a compute into this program
    def LoadFile(self,text1,text2,text3,text4,text5):
        try:
            filename = askopenfilename() # ask the user to choose the file they want to open;get the name of the selected file
            file = open(filename,'r')# open and read the file
            lines = file.readlines()#files is a list contain all lines in the file
            l = []
            for i in lines:
                a = i[:-1]# in order to get rid of "\n"
                l += [a.split(",")] # split the information in each line by a comma
            for j in l:
                j[0]=int(j[0])# convert the string of itemNumber to integer
            self.Numberlist=l #store the data into the inventory list in the program
            file.close() #close the file
            self.Numberlist=self.merge_sort(self.Numberlist)#sort the itemNumber in increasing order
            pos = 0
            self.insertAllInfo(text1,text2,text3,text4,text5,pos)
        except UnicodeDecodeError:# if the user open a wrong formatted file, it will show warning to the user.
            messagebox.showerror('Error','The loaded file is not correct format')
        except FileNotFoundError: # the user clicker does not want to open. the fiel and click cancel
            pass
        

    #this method associated with the Save Button
    #used to save the inventory list into a file in the computer
    def SaveFile(self):
        try:
            k = len(self.Numberlist)
            filename=askopenfilename() #ask the user to select a file to store the data in
            file = open(filename,"w") # open the selected file and then it can write data into it
            
            for i in self.Numberlist: # i represent each item
                for j in i:# j represent five information of one item
                    if j != i[-1]:#
                        if type(j)!=str:
                            file.write(str(j)+',')
                        else:
                            file.write(j+',')
                    else:
                        if type(j)!=str:
                            file.write(str(j))
                        else:
                            file.write(j)
                file.write('\n')#finish writing one item information then write the next item in the next line
            file.close() # close the file
        except FileNotFoundError: # the user does not want to save and click cancel
            pass

    #this method is used to add a scroller to the inventory display.
    def __yscrollHandler(self,*L):
        op, howMany = L[0], L[1]
        if op == 'scroll':
            units = L[2]
            entry.yview_scroll(howMany, units)
        elif op == 'moveto': 
            entry.yview_moveto(howMany)

    #associated with the "Show Inventory" button
    #display all the information of all items in the inventory
    def showall(self):
        inventory = Tk()#make a new widget
        InvFrame = ttk.Frame(inventory,relief=SUNKEN, padding="5 5 5 5")
        InvFrame.grid(row=0,column=0,sticky=(N,E,W,S))
        InvFrame.grid_rowconfigure(0,weight=5)
        InvFrame.grid_columnconfigure(0,weight=5)
        ybar = ttk.Scrollbar(InvFrame,command=self.__yscrollHandler)#make a scroller bar
        display = Text(InvFrame,width=70,height=20,bg='lightGrey',fg='black',yscrollcommand=ybar)
        display.grid(row=0,column=0,sticky=W)
        #let the show in the display Text in a right format
        for i in self.Numberlist:
            for j in i:
                if j != i[-1]:
                    if type(j)!=str:
                        display.insert(INSERT,str(j)+',')
                    else:
                        display.insert(INSERT,j+',')
                else:
                    if type(j)!=str:
                        display.insert(INSERT,str(j))
                    else:
                        display.insert(INSERT,j)
            display.insert(INSERT,'\n')
        ybar.grid(row=0,column=1,sticky=(N,S))
        ybar.configure(command = display.yview)
        display['yscrollcommand'] = ybar.set
        inventory.title("Inventory")

    #this method is used to insert the item information in five text fields from the database.
    def insertAllInfo(self,text1,text2,text3,text4,text5,pos):
        text1.insert(INSERT,self.Numberlist[pos][0])
        text2.insert(INSERT,self.Numberlist[pos][1])
        text3.insert(INSERT,self.Numberlist[pos][2])
        text4.insert(INSERT,self.Numberlist[pos][3])
        text5.insert(INSERT,self.Numberlist[pos][4])


    #this method is used to clear out all information in five text fields.
    def cleartext(self,text1,text2,text3,text4,text5):
        text1.delete(0.0,END)
        text2.delete(0.0,END)
        text3.delete(0.0,END)
        text4.delete(0.0,END)
        text5.delete(0.0,END)
                        
                                
            

def main():
    root=Tk() 
    Inventory(root)
    root.title("Inventory Management")
    root.mainloop()

if __name__==main():
    main()

