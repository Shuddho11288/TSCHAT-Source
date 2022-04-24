import tkinter
import ctypes
import tkinter.ttk as ttk
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class EmojiPop(tkinter.Frame):
    def __init__(self,app,text3):
        super().__init__(app,width=100,height=50)
        
        self.text3 = text3
        self.config(bg="#e1fef8",padx=10,pady=10)

        bu = ttk.Button(self,text="Close",command=lambda: self.destroy(),width=22)
        bu.grid(row=0,column=0,columnspan=4)
        
        bu0 = ttk.Button(self,text=":)",command=lambda: self.inserttext(bu0.cget("text")),width=3)
        bu0.grid(row=1,column=0)


        bu1 = ttk.Button(self,text=":(",command=lambda: self.inserttext(bu1.cget("text")),width=3)
        bu1.grid(row=1,column=1)


        bu2 = ttk.Button(self,text=":D",command=lambda: self.inserttext(bu2.cget("text")),width=3)
        bu2.grid(row=1,column=2)


        bu3 = ttk.Button(self,text="-_-",command=lambda: self.inserttext(bu3.cget("text")),width=3)
        bu3.grid(row=1,column=3)


        bu4 = ttk.Button(self,text=":*",command=lambda: self.inserttext(bu4.cget("text")),width=3)
        bu4.grid(row=3,column=0)


        bu5 = ttk.Button(self,text="3:)",command=lambda: self.inserttext(bu5.cget("text")),width=3)
        bu5.grid(row=3,column=1)


        bu6 = ttk.Button(self,text="0:)",command=lambda: self.inserttext(bu6.cget("text")),width=3)
        bu6.grid(row=3,column=2)


        bu7 = ttk.Button(self,text=":3",command=lambda: self.inserttext(bu7.cget("text")),width=3)
        bu7.grid(row=3,column=3)


        bu8 = ttk.Button(self,text="0_0",command=lambda: self.inserttext(bu8.cget("text")),width=3)
        bu8.grid(row=2,column=0)


        bu9 = ttk.Button(self,text="<3",command=lambda: self.inserttext(bu9.cget("text")),width=3)
        bu9.grid(row=2,column=1)


        bu10 = ttk.Button(self,text=":|",command=lambda: self.inserttext(bu10.cget("text")),width=3)
        bu10.grid(row=2,column=2)


        bu11 = ttk.Button(self,text="B)",command=lambda: self.inserttext(bu11.cget("text")),width=3)
        bu11.grid(row=2,column=3)



        self.v = ttk.Scrollbar(self, orient='vertical')
    def inserttext(self,text):
        self.text3.insert("end",text)



