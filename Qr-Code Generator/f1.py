from tkinter import *
from tkinter import messagebox, Toplevel
import pyqrcode as p
import os
import png

root = Tk()
root.geometry('570x400')
root.title('MY Qr_code!!')
root.configure(bg='green')

#Functions to be executed on clicking buttons
def generate_qr():
    Qr_Name = Qr_Name_Entry_Box.get()
    Qr_Id = Qr_Id_Entry_Box.get()
    Qr_Message = Qr_Message_Entry_Box.get()
    Message_Qr = 'Name : ' + Qr_Name + '\n' + 'Id : ' + Qr_Id + '\n' + 'Message : ' + Qr_Message
    url = p.create(Message_Qr)
    pp = r'C:\Users\Dell\Desktop\qr1'
    cc = '{}\{}{}.png'.format(pp, Qr_Id, Qr_Name)
    ll = os.listdir(pp)
    if ('{}{}.png'.format(Qr_Id, Qr_Name) in ll):
        messagebox.showinfo('Notification', 'Please choose another id or name..')
    else:
        url.png(cc, scale=8)
        mm = 'Your Qr Code is Saved as : ' + Qr_Id + Qr_Name + '.png'
        Qr_Notification_Message_label.configure(text=mm)
        res = messagebox.askyesno('Notification', 'Qr Code is Generated.If You Want to see It then Yes :')
        if (res == True):
            top = Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img = PhotoImage(file=cc)
            label1 = Label(top, image=img, bg='white')
            label1.place(x=10, y=10)
            top.mainloop()

def clear_id_name():
    Qr_Id_Entry_Box.delete(0, 'end')
    Qr_Message_Entry_Box.delete(0, 'end')
    Qr_Name_Entry_Box.delete(0, 'end')
    Qr_Notification_Message_label.configure(text='')

#Labels to display text
Qr_Id_label = Label(master=root, text='Enter Your Id : ', bg='powder blue', fg='red', width=20, height=2,
                    font=('times', 12, 'italic bold'))
Qr_Id_label.place(x=10, y=20)

Qr_Name_label = Label(master=root, text='Enter Your Name : ', bg='powder blue', fg='red', width=20, height=2,
                      font=('times', 12, 'italic bold'))
Qr_Name_label.place(x=10, y=80)

Qr_Message_label = Label(master=root, text='Enter Your Message : ', bg='powder blue', fg='red', width=20, height=2,
                         font=('times', 12, 'italic bold'))
Qr_Message_label.place(x=10, y=140)

Qr_Notification_label = Label(master=root, text='Notification : ', bg='powder blue', fg='red', width=10, height=2,
                              font=('times', 15, 'bold underline'))
Qr_Notification_label.place(x=10, y=350)

Qr_Notification_Message_label = Label(master=root, text='', bg='powder blue', fg='red', width=30, height=2,
                                      font=('times', 15, 'bold'))
Qr_Notification_Message_label.place(x=200, y=350)

####  Entry Boxes to input values from user
Qr_Id_Entry_Box = Entry(master=root, width=25, bd=5, bg='pink', font=('times', 17, 'italic bold'))
Qr_Id_Entry_Box.place(x=250, y=20)

Qr_Name_Entry_Box = Entry(master=root, width=25, bd=5, bg='pink', font=('times', 17, 'italic bold'))
Qr_Name_Entry_Box.place(x=250, y=80)

Qr_Message_Entry_Box = Entry(master=root, width=25, bd=5, bg='pink', font=('times', 17, 'italic bold'))
Qr_Message_Entry_Box.place(x=250, y=140)

#creating Buttons
generate_button = Button(master=root, text='Generate', width=15, font=('times', 10, 'bold'), bd=10, command=generate_qr,
                         activebackground='blue', bg='powder blue', compound=RIGHT)
generate_button.place(x=10, y=250)

Clear_Button = Button(master=root, text='Clear', width=30, font=('times', 10, 'bold'), bd=10, command=clear_id_name,
                      activebackground='blue', bg='powder blue', compound=RIGHT)
Clear_Button.place(x=210, y=250)

#functions for HoverEffects
def Generate_ButtonEnter(e):
    generate_button['bg'] = 'purple2'


def Generate_ButtonLeave(e):
    generate_button['bg'] = 'powder blue'


def Clear_Id_Name_ButtonEnter(e):
    Clear_Button['bg'] = 'purple2'


def Clear_Id_Name_ButtonLeave(e):
    Clear_Button['bg'] = 'powder blue'

##calling hoverEffect functions
generate_button.bind('<Enter>', Generate_ButtonEnter)
generate_button.bind('<Leave>', Generate_ButtonLeave)

Clear_Button.bind('<Enter>', Clear_Id_Name_ButtonEnter)
Clear_Button.bind('<Leave>', Clear_Id_Name_ButtonLeave)

root.mainloop()
