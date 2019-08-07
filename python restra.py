from tkinter import *
class A():
    def __init__(self,root):
        #============Frame1==========
        self.f1=Frame(root,width=400,height=100,bg="black")
        self.f1.propagate(0)
        self.f1.pack()
        self.l1=Label(self.f1,text="PYTHON RESTRA",
                      font=("Arial",34,"bold"),
                      bg="black",
                      fg="white")
        self.l1.place(x=5,y=30)
        #=============canvas==========
        self.c=Canvas(root,width=400,height=3,bg="black")
        line=self.c.create_line(10,10,10,10,width=5)
        self.c.pack()
        #=============Frame2===========
        self.f2=Frame(root,width=400,height=460)
        self.f2.propagate(0)
        self.f2.pack()
        #==============label work=======
        self.l2=Label(self.f2,text="MENU",
                      font=("Arial",38,"bold"),
                      fg="black")
        self.l2.place(x=140,y=30)
        self.l3=Label(self.f2,text="ITEMS",
                      font=("Arial",16,"bold"))
        self.l3.place(x=55,y=110)
        self.l4=Label(self.f2,text="QUNTITY",
                      font=("Arial",16,"bold"))
        self.l4.place(x=248,y=110)
        self.l5=Label(self.f2,text="Total:-",
                      font=("Arial",28,"bold"))
        self.l5.place(x=20,y=400)
        #===========checkbox===========
        self.var1=IntVar()
        self.c1=Checkbutton(self.f2,text="Kali Tea",
                         font=("arial",20,"bold"),
                         variable=self.var1)
        self.c1.place(x=20,y=150)
        self.var2=IntVar()
        self.c2=Checkbutton(self.f2,text="Hari Tea",
                            font=("arial",20,"bold"),
                            variable=self.var2)
        self.c2.place(x=20,y=200)
        self.var3=IntVar()
        self.c3=Checkbutton(self.f2,text="Patato Pratha",
                            font=("arial",20,"bold"),
                            variable=self.var3)
        self.c3.place(x=20,y=250)
        self.var4=IntVar()
        self.c4=Checkbutton(self.f2,text="Piyaz Prizza",
                            font=("arial",20,"bold"),
                            variable=self.var4)
        self.c4.place(x=20,y=300)
        #==============Entry=============
        self.e1=Entry(self.f2,width=14,bd=2)
        self.e1.place(x=250,y=165)
        self.e2=Entry(self.f2,width=14,bd=2)
        self.e2.place(x=250,y=215)
        self.e3=Entry(self.f2,width=14,bd=2)
        self.e3.place(x=250,y=265)
        self.e4=Entry(self.f2,width=14,bd=2)
        self.e4.place(x=250,y=315)
        self.e5=Entry(self.f2,width=30,bd=5)
        self.e5.place(x=150,y=415)
        #=============Button============
        self.b1=Button(self.f2,text="Bill",width=25,height=2,bd=5,
                       command=self.total)
        self.b1.place(x=150,y=350)
        self.b2=Button(self.f2,text="Clear",width=15,height=2,bd=5,
                       command=self.cel)
        self.b2.place(x=20,y=350)

    def total(self):
        str1=self.var1.get()
        str2=self.var2.get()
        str3=self.var3.get()
        str4=self.var4.get()
        if str1==1:
            int1=int(self.e1.get())
            tot1=int1*30
        else:
            tot1=0
        if str2==1:
            int2=int(self.e2.get())
            tot2=int2*30
        else:
            tot2=0
        if str3==1:
            int3=int(self.e3.get())
            tot3=int3*50
        else:
            tot3=0
        if str4==1:
            int4=int(self.e4.get())
            tot4=int4*100
        else:
            tot4=0
        tot=tot1+tot2+tot3+tot4
        self.e5.delete(0,'end')
        self.e5.insert(END,int(tot))
    def cel(self):
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')
        self.e3.delete(0,'end')
        self.e4.delete(0,'end')
        self.e5.delete(0,'end')
        
        
root=Tk()
obj=A(root)
root.title("PYTHON RESTRA")
root.mainloop()
