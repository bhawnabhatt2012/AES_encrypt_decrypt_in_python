import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from tkinter import *

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]

class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self,frame):
        textPad = Frame(frame)
        self.text = Text(textPad,height=20,width=40)
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        return

root = Tk()
btn1 = Button(root,text = 'Load Text File',command = )
btn1.pack(side=TOP)
row1 = Frame(root)
lab1 = Label(row1,text='Path')
ent1 = Entry(row1)
row1.pack(side=TOP,expand=YES,fill=X)
lab1.pack(side=LEFT)
ent1.pack(side=RIGHT,expand=YES,fill=X)

btn2 = Button(root,text = 'Encrypt File',command = )
btn2.pack(side=TOP)
row2 = Frame(root)
lab2 = Label(row2,text='Enter password')
ent2 = Entry(row2)
row2.pack(side=TOP,expand=YES,fill=X)
lab2.pack(side=LEFT)
ent2.pack(side=RIGHT,expand=YES,fill=X)

btn3 = Button(root,text = 'Decrypt File',command = )
btn3.pack(side=TOP)
row3 = Frame(root)
lab3 = Label(row3,text='Enter password')
ent3 = Entry(row3)
row3.pack(side=TOP,expand=YES,fill=X)
lab3.pack(side=LEFT)
ent3.pack(side=RIGHT,expand=YES,fill=X)

scrolledText=scrollTxtArea(root)
root.title('TextPad with a Vertical Scroll Bar')

exit_btn = Button(root,text='QUIT',command=root.quit)
exit_btn.pack(side=TOP)
root.mainloop()


