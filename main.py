from tkinter import *
import base64
import os

def decrypt():
     pass

def encrypt():
     password = code.get()
     if password == "1234":
          screen1 = Toplevel(screen)
          screen1.title("encryption")
          screen1.geometry("400x200")
          screen1.configure(bg="#ed3833")

          message=text1.get(1.0, END)
          encode_messege =message.encode("ascii")
          base64_bytes = base64.b64encode(encode_messege)
          encrypt=base64_bytes.decode("ascii")
          Label(screen1,text="ENCRYPT",font="arial",fg='white',bg=('#ed3833')).place(x=10,y=0)
          text2 = Text(screen1,bg = 'white',font = 'arial',wrap=WORD,bd =0,relief=GROOVE)
          text2.place(x=10,y=40,bg ='white',width=200,height=150)
          text2.insert(END,encrypt)




          

    
     

def main_screen():
     global text1,code,screen
     screen = Tk()
     screen.geometry("375x398")
     screen.title('TheAPP')
     Label(text="Enter text for encriptionand decryption",fg='black',font=("calbri",13)).place(x=10,y=10)
     text1 =Text(bg='white',font=("calbri",14),wrap=WORD,bd=0,relief=GROOVE)
     text1.place(x=10,y=50,width=355,height=100)
    
     Label(text="Enter password",fg='black',font=('calbri',13)).place(x=10,y=170)
     code = StringVar()
     Entry(textvariable=code,width=19,bd=0,show="*",font=('arial',25)).place(x=10,y=200)

     Button(text="ENCRYPT",height=2,width=23,bg="#ed3833",fg='white',bd=0,command=lambda:encrypt()).place(x=10,y=250)
     Button(text="DECRYPT",height=2,width=23,bg="#00bd56",fg='white',bd=0).place(x=200,y=250)
     Button(text="RESET",height=2,width=50,bg="#ed3833",fg='white',bd=0,command=lambda:reset()).place(x=10,y=300)


     screen.mainloop()
def reset():
    code.set("")
    text1.delete(1.0, END)

  
    
 
main_screen()
