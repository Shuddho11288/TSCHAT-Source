import engine
import tkinter
import threading
import ctypes
import emojipopup
import time
import tkinter.messagebox as msgbox
import darkdetect
import tkinter.ttk as ttk
#from PIL import Image, ImageTk
#from plyer.utils import platform
#from plyer import notification


POS = (0,0)
MESSAGES_STRING = None
MODE = None
APP_CLOSED = False
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class App:
    def __init__(self) -> None:
        self.client = engine.Engine("sus")
        self.initialze_app()


    def initialze_app(self):
        self.app = tkinter.Tk("TS Chat")
        self.app.tk.call("source", "./Sun-Valley-ttk-theme-master/sun-valley.tcl")
        self.app.tk.call("set_theme", "light")

        self.app.title("TS Chat")
        self.app.geometry("760x780")
        self.app.minsize(760, 790)
        #self.app.maxsize(760, 790)
        self.app.iconbitmap("./Screenshot 2022-04-04 180515.ico")
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.attributes('-alpha',0.95)
        
        self.create_ui()
        self.load_ui()

    
    def create_ui(self):
        


        self.text = tkinter.Text(self.app, borderwidth=0, highlightthickness=0)
        self.name = ttk.Entry(self.app, width=80)
        self.text2 = ttk.Entry(self.app, width=53)
        self.text3 = ttk.Entry(self.app, width=58)
        self.label1 = ttk.Label(self.app,text="Enter your chat code(A new chat code will be created if the code is not found): ")
        self.label2 = ttk.Label(self.app,text="Enter your name:")
        self.text.configure(bg="#ffffff")
        self.buttonCode = ttk.Button(self.app,style="Accent.TButton",text="change  chat  code", command=lambda: threading.Thread(target=self.changecode).start())
        self.buttonSend = ttk.Button(self.app,style="Accent.TButton",text="Send Message",image=tkinter.PhotoImage(file = r"Screenshot 2022-04-24 095150.png"), command=lambda: self.sendmessage(self.name.get().strip('\n'),self.text2.get()))
        self.buttonemo = ttk.Button(self.app,style="Accent.TButton",text="😀",command=self.emopop)
        

    def load_ui(self):

        self.label2.grid(row=0,column=0,columnspan=3,padx=10,)
        self.name.grid(row=1,column=0, columnspan=3,padx=10,)
        self.label1.grid(row=2,column=0,columnspan=3,padx=10,)
        self.text3.grid(row=3,column=0,padx=10,columnspan=2)
        self.buttonCode.grid(row=3,column=2,padx=10,pady=10)
        self.text.grid(row=4,column=0,columnspan=3,padx=10,)
        self.buttonemo.grid(row=6,column=0,padx=10)
        self.text2.grid(row=6,column=1)
        self.buttonSend.grid(row=6,column=2,padx=5,pady=5)




    def run(self):
        global APP_CLOSED
        thd = threading.Thread(target=self.getmessage2)
        thd.start()
        threading.Thread(target=self.set_mode).start()
        self.app.mainloop()
        APP_CLOSED= True

    def emopop(self):
        f = emojipopup.EmojiPop(self.app,self.text2)
        f.place(x=10,y=550)

        

    def getmessage2(self):
        global POS, MESSAGES_STRING, APP_CLOSED
        while not APP_CLOSED:
            messages = self.client.get_all_messages()
            strng = ""
            for message in messages:
                strng += str(message[0])+": "+str(message[1])
                strng +="\n\n"
            if MESSAGES_STRING != strng:
                self.text.configure(state='normal')
                self.text.delete(1.0,tkinter.END)
                self.text.insert(tkinter.INSERT, strng)
                self.text.yview_pickplace("end")
                self.text.configure(state='disabled')
                if self.app.state()=="iconic":
                    print("lOL")
                    strnglista = strng.split("\n\n")[-2]
                    #self.notificate(self.text3.get(),strnglista)
            MESSAGES_STRING = strng
            
            
            time.sleep(1)
            

    def sendmessage(self, user:str,message:str):
        if user.strip() != "" and message.strip() != "":
            nthd = threading.Thread(target=lambda: self.client.send_message(user,message))
            nthd.start()
        
        else:
            print("Error")
            self.open_popup()

        #text.yview_pickplace("end")
        
        
    def changecode(self):
        strn = self.text3.get()
        
        print(strn)
        self.client.change_code(repr(strn))


    def set_mode(self):
        global MODE, APP_CLOSED
        
        while not APP_CLOSED:
            #print(darkdetect.theme())
            
            if MODE != darkdetect.theme().lower():
                if darkdetect.isDark():
                    
                    self.app.tk.call("set_theme","dark")
                    self.text.configure(bg="#000000")
                    
                    
                else:
                    
                    self.app.tk.call("set_theme","light")
                    
                    self.text.configure(bg="#ffffff")
                    

                
                MODE = darkdetect.theme().lower()
                time.sleep(1)

    def open_popup(self):
        msgbox.showerror("Invalid Name or Message","Please enter a valid name and a valid message!")
'''
    def notificate(self, group_name, last_message):
        notification.notify(
            title=group_name,
            message=last_message,
            app_name='TS Chat',
            app_icon='Screenshot 2022-04-04 180515.' + ('ico' if platform == 'win' else 'png')
        )
'''

app = App()
app.run()
