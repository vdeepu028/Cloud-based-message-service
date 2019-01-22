import tkinter
import tkinter.messagebox
import tkinter.ttk
import http.client

class form1:
    def add(self):
        if self.tb1.get()=="" or self.tb2.get()=="" :
            tkinter.messagebox.showinfo(" "," ALL FIELDS ARE MANDATORY")
            self.win.lift()
        else:
            obj=open("message_project1.txt","a")
            gpname=self.tb1.get()
            descript=self.tb2.get()
            obj.write(gpname)
            obj.write("\n")
            obj.write(descript)
            obj.write("\n*********\n")
            obj.close()
            tkinter.messagebox.showinfo(" ","  Attempt Successfull")
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.title(" ")
        self.win.geometry("400x250")
        
        self.lb1=tkinter.Label(self.win,text="Group Name")
        self.tb1=tkinter.Entry(self.win)
        self.lb2=tkinter.Label(self.win,text="Description")
        self.tb2=tkinter.Entry(self.win)
        
        self.bt1=tkinter.Button(self.win,text="Submit",command=self.add)
        self.lb1.grid(row=0,column=0)
        self.tb1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.tb2.grid(row=1,column=1)
        
        self.bt1.grid(row=2,column=1)
        self.win.mainloop()
#-------------------------------------
def test():
    x=form1()
#----------------------------------------
class form2:
    def __init__(self):
        self.win2=tkinter.Tk()
        self.win2.lift()
        self.win2.title(" RECORD ")
        self.t=tkinter.ttk.Treeview(self.win2,columns=("group","description",))
        self.t.column("#0",width=0)
        self.t.heading("group",text="GROUP NAME")
        self.t.heading("description",text="DESCRIPTION")
        self.rd=open("message_project1.txt","r")
        self.i=0
        while True:
            self.gp=self.rd.readline()
            if self.gp=="":
                break
            self.descript=self.rd.readline()
            self.sep=self.rd.readline()
            self.t.insert("",self.i,values=(self.gp,self.descript))
            self.i=self.i+1
        self.t.pack(side="left")
        self.scrollbar = tkinter.ttk.Scrollbar(self.win2, orient="vertical", command=self.t.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.t.configure(yscrollcommand=self.scrollbar.set)
        self.win2.mainloop()
#--------------------------------------
def test2():
    y=form2()

#------------------------
class form3:
    def insert(self):
        if self.textbox2.get()!="" and self.textbox2.get().isnumeric()==True and len(self.textbox2.get())==10:
            
            wr=open("phones.txt","a")
            wr.write(self.cb1.get())
            wr.write(self.textbox1.get())
            wr.write("\n")
            wr.write(self.textbox2.get())
            wr.write("\n*****\n")
            wr.close()
            tkinter.messagebox.showinfo("","Member Added Sucessfully")
        else:
            tkinter.messagebox.showinfo("","INCORRECT PHONE NUMBER")
            
        
        
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.lift()
        self.win.geometry("300x200")

        self.lb=tkinter.Label(self.win,text="Enter Group Name")

        list1=[]

        fileopen=open("message_project1.txt","r")

        i=0

        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()

        


        
        self.cb1=tkinter.ttk.Combobox(self.win,values=tuple(list1))

        self.lb1=tkinter.Label(self.win,text="Enter Name")
        self.textbox1=tkinter.Entry(self.win)
        self.lb2=tkinter.Label(self.win,text="Enter Mobile Number")
        self.textbox2=tkinter.Entry(self.win)

        self.bt1=tkinter.Button(self.win,text="Add New Member",command=self.insert)

        self.lb.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

        self.lb1.grid(row=1,column=0)
        self.textbox1.grid(row=1,column=1)
        
        self.lb2.grid(row=2,column=0)
        self.textbox2.grid(row=2,column=1)


        self.bt1.grid(row=3,column=1)



        self.win.mainloop()
#-------------------------------------------------------------
class form4:
    def conv(self,n):
        k=n[0:10]
        return k
    
    def insert(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


        
        rd=open("phones.txt","r")
        i=0
        while True:
            line=rd.readline()
            if line=="":
                break
            line1=rd.readline()
            line2=rd.readline()
            line3=rd.readline()
            if line==self.cb1.get():
                self.tree.insert("",i,values=((i+1),line,line1,line2))
                i=i+1
    
                
    def covertmob(self):
        s=self.msgtextbox.get()
        list2=s.split(" ")
        a=""
        for x in list2:
            a=a+x+"%20"
            
        for child in self.tree.get_children():
            temp=self.tree.item(child)["values"]
            num=str(temp[3])
            print(num)
            conn=http.client.HTTPConnection("server1.vmm.education")
            conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?username=YOUR USERNAME&password=YOUR PASSWORD&message="+a+"&phone_numbers="+num+"")
            response=conn.getresponse()
            print(response.read())
    
       
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.lift()
        self.win.geometry()


        self.frame1=tkinter.Frame(self.win)
        self.frame2=tkinter.Frame(self.win)

        self.lb1=tkinter.Label(self.frame1,text="Select Group ")

        list1=[]

        fileopen=open("message_project1.txt","r")

        i=0

        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()

        


        
        self.cb1=tkinter.ttk.Combobox(self.frame1,values=tuple(list1))


       

        self.bt1=tkinter.Button(self.frame1,text=" VIEW ",bg="lightgrey",command=self.insert)

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

     

        self.bt1.grid(row=0,column=3)

        self.frame1.pack()

        self.tree=tkinter.ttk.Treeview(self.win,columns=("srno","groupname","membernm","members"))
        self.tree.column("#0",width=0)
        self.tree.heading("srno",text="Serial Number")
        self.tree.heading("groupname",text="Group Name")
        self.tree.heading("membernm",text="NAME")
        self.tree.heading("members",text="Mobile Number")
        self.tree.pack()
        self.mlab=tkinter.Label(self.frame2,text=" ENTER MESSAGE")
        self.msgtextbox=tkinter.Entry(self.frame2)
        self.sbt1=tkinter.Button(self.frame2,text=" SEND",bg="lightgrey",command=self.covertmob)
        self.mlab.grid(row=0,column=0)
        self.msgtextbox.grid(row=0,column=1)
        self.sbt1.grid(row=1,column=1)
        self.frame2.pack()


        self.win.mainloop()

#--------------------------------------------------------------
def showphones():
    x=form4()
#-----------------------

        
def showinsert_data():
    x=form3()

root=tkinter.Tk()
root.geometry("500x500")
root.config(bg="bisque")
mymenu=tkinter.Menu(root)
root.config(menu=mymenu)
submenu1=tkinter.Menu(mymenu)
submenu1=tkinter.Menu(mymenu,tearoff=False)
mymenu.add_cascade(label="GROUP MANAGEMENT",menu=submenu1)
submenu1.add_command(label="ADD GROUP",command=test)
submenu1.add_command(label="VIEW GROUPS",command=test2)
submenu1.add_command(label="ADD CONTACTS",command=showinsert_data)
submenu1.add_command(label="VIEW CONTACTS",command=showphones)
label1=tkinter.Label(root,text=" BEATENEST ",bg="mint cream",fg="black",font="HELVETICA 26")
label1.pack()
root.config(bg="bisque")
pic=tkinter.PhotoImage(file="message.gif")
lbpic=tkinter.Label(root,image=pic,bg="bisque")
lbpic.pack()
label2=tkinter.Label(root,text=" MESSENGER ",bg="mint cream",fg="black",font="HELVETICA 28")
label2.pack()



root.mainloop()
                           





    







