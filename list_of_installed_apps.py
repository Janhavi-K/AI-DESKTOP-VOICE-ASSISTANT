import winreg
import tkinter
from tkinter import StringVar, ttk
import os
import tkinter.filedialog
import sqlite3
from tkinter import messagebox

def start():
    listt=list()
    root = tkinter.Tk()
    root.configure(background='white')
    root.geometry('850x400')
    root.title("Add App Path")
    root.configure(background="#ffb3ff")

    vari=StringVar()
    conn=sqlite3.Connection("Database333.db")
    if os.stat("Database333.db").st_size == 0:
                    conn.execute("create table path(APPS char(20) ,APPS_PATH varchar(50));")

    def foo(hive, flag):
        aReg = winreg.ConnectRegistry(None, hive)
        aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                            0, winreg.KEY_READ | flag)

        count_subkey = winreg.QueryInfoKey(aKey)[0]

        software_list = []
        for i in range(count_subkey):
            software = {}
            try:
                asubkey_name = winreg.EnumKey(aKey, i)
                asubkey = winreg.OpenKey(aKey, asubkey_name)
                software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]
            except EnvironmentError:
                continue
            software_list.append(software)
            listt.append(str(software['name']))

        return software_list

    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
    for software in software_list:
        #print('Name=%s' % software['name'])
        listt.append(software['name'])

    print('Number of installed apps: %s' % len(software_list))
    print(len(listt))
    vari.set(listt[4])
    #lbl0=tkinter.Label(root,text="Add App Path",bg='cyan',fg='black',width=12,font=('Times New Roman',24)).place(x=300,y=40)
    apps_combo = ttk.Combobox(root, textvariable=vari,width=65,values=listt,height=10,font=("Times New Roman",14))
    lbl1=tkinter.Label(root,text="App Name",bg='black',fg='white',width=13,borderwidth=1,relief="solid",font=('Times New Roman',14)).place(x=15,y=110)
    lbl2=tkinter.Label(root,text="App Path",bg='black',fg='white',width=13,borderwidth=1,relief="solid",height=2,font=('Times New Roman',14)).place(x=15,y=140)

    def select():
            global booli
            booli=False
            conn=sqlite3.Connection("Database333.db")
            value = apps_combo.get()
            try:
                if path2=="" or value=="":
                    messagebox.showerror("Error", "Both the fileds are mandatory")
            except Exception as e:
                messagebox.showerror("Error","Both fields are mandatory")
            else:
                cur=conn.execute("select APPS,APPS_PATH from path")
                for j in cur:
                    print(j[0])
                    if value==j[0] or path2==j[1]:
                        booli=True
                    else:
                        booli=False
                        #messagebox.showwarning("Warning","App and path already exists")
                if booli==False:
                    conn.execute("insert into path (APPS, APPS_PATH) values(?,?)",(value,path2))
                    print(value)
                    print(path2)
                    messagebox.showinfo("Info", "Path Successfulley added")
                    conn.commit()
                else:
                    messagebox.showwarning("Warning","App and path already exists")


        
    def clear(txt):
        apps_combo.set('')
        txt=tkinter.Label(root,bg='white',width=55,borderwidth=1,relief="solid",height=2,font=('Times New Roman',12)).place(x=150,y=140)
        

    def getPath():
        global path2
        path1=tkinter.filedialog.askopenfilenames()
        path2=str(path1[0])
        txt=tkinter.Label(root,text=path2,bg='white',width=55,borderwidth=1,relief="solid",height=2,font=('Times New Roman',12)).place(x=150,y=140)

    apps_combo.place(x=155,y=110)
    txt=tkinter.Label(root,bg='white',width=55,borderwidth=1,relief="solid",height=2,font=('Times New Roman',12))
    B = tkinter.Button(root, text ="Browse", command = getPath,width=10,background="purple",foreground="white",cursor='hand2',font=("Times New Roman",14)).place(x=660,y=140)
    Bu2 = tkinter.Button(root, text ="Submit", command = select,borderwidth=1,background="purple",foreground="white",cursor='hand2',width=10,height=1,font=("Times New Roman",15)).place(x=280,y=300)
    bu3= tkinter.Button(root, text ="Reset", command = lambda:clear(txt),borderwidth=1,background="purple",cursor='hand2',foreground="white",width=10,height=1,font=("Times New Roman",15)).place(x=430,y=300)
    txt.place(x=155,y=140)
    tkinter.mainloop()



