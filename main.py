from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from math import *

#creating main window.
root = Tk()
root.title("AREACALCULATOR")
root.configure(bg='cyan')
headers=Label(root, text='PLEASE CHOOSE THE SHAPE.', padx=100, pady=10, foreground='red', background='yellow', relief=RAISED ,bd=5).grid(row=0, column=0, columnspan=1)
type_shape1=Label(root, text="2D shapes:", padx=70, pady=10, font=('Helvetica',18,'bold'), bg='cyan', fg='black').grid(row=1, column=0)


def button_sqr():
    top = Toplevel()                        #creating a new window for square.
    top.title('SQUARE')
    header=Label(top, text='Calculating the area of square.')
    header.grid(row=0, column=0, columnspan=3)          #add sticky here.
    label1=Label(top, text='Enter the side of the square in cm below:')
    label1.grid(row=2, column=0)
    
    e=Entry(top, borderwidth='1')
    e.grid(row=2, column=1)
       
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/sqr.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        a=e.get()
        b=float(a)
        ar=b**2
        per=b*4
        c=str(round(ar,3))
        d=str(round(per,3))
        
        l1="The area of the square is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the square is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=4, column=0, columnspan=3)
        label02.grid(row=5, column=0, columnspan=3)
    
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=3,column=0, columnspan=3)

    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == True:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_rect():
    top = Toplevel()                        #creating a new window for rectangle.
    top.title('RECTANGLE')
    
    label1=Label(top, text='Calculating the area of rectangle.')
    label2=Label(top, text='Enter the length of the rectangle in cm below:')
    label3=Label(top, text='Enter the breadth of the rectangle in cm below:')
    label1.grid(row=0, column=0, columnspan=3)          #add sticky here.
    label2.grid(row=1, column=0, sticky=W)
    label3.grid(row=2, column=0, sticky=W)
    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    e2=Entry(top, borderwidth='1')
    e2.grid(row=2, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/rectangle.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        l=e1.get()
        l1=float(l)
        b=e2.get()
        b1=float(b)
        ar=b1*l1
        per=2*(l1+b1)
        c=str(round(ar,3))
        d=str(round(per,3))
        
        l1="The area of the rectangle is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the rectangle is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=4, column=0, columnspan=3)
        label02.grid(row=5, column=0, columnspan=3)
    
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=3,column=0, columnspan=3)

    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_tri():
    top = Toplevel()                        #creating a new window for triangle.
    top.title('TRIANGLE')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of triangle.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the HEIGHT of the triangle in cm below:')
    label2=Label(top, text='Enter the BASE of the triangle in cm below:')
    label3=Label(top, text='Enter the 1st side of the triangle in cm below:')
    label4=Label(top, text='Enter the 2nd side of the triangle in cm below:')
    label5=Label(top, text='Enter the 3rd side of the triangle in cm below:')
    label1.grid(row=1, column=0, sticky=W)
    label2.grid(row=2, column=0, sticky=W)
    label3.grid(row=3, column=0, sticky=W)
    label4.grid(row=4, column=0, sticky=W)
    label5.grid(row=5, column=0, sticky=W)
    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e2=Entry(top, borderwidth='1')
    e3=Entry(top, borderwidth='1')
    e4=Entry(top, borderwidth='1')
    e5=Entry(top, borderwidth='1')
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/tri.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        #height.
        h=e1.get()
        h1=float(h)
        #base.
        b=e2.get()
        b1=float(b)
        #sides 1,2,3.
        s1=e3.get()
        S1=float(s1)
        s2=e4.get()
        S2=float(s2)
        s3=e5.get()
        S3=float(s3)

        #calculating area.
        ar=(0.5)*(b1*h1)
        c=str(round(ar,3))
        #calculating perimeter.
        per=(S1+S2+S3)
        d=str(round(per,3))
        
        l1="The area of the triangle is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the triangle is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()
        

def button_crcl():
    top = Toplevel()                        #creating a new window.
    top.title('CIRCLE')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of circle.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the RADIUS of the circle in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/circ.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #radius.
        r=e1.get()
        r1=float(r)
        #calculating area.
        ar=pi*(r1**2)
        c=str(round(ar,3))
        #calculating circumference.
        per=2*pi*r1
        d=str(round(per,3))
        
        l1="The area of the circle is "+c+' cm\u00b2'+'.'
        l2="The circumference of the circle is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_semicrcl():
    top = Toplevel()                        #creating a new window.
    top.title('SEMI-CIRCLE')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of semi-circle.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the RADIUS of the semi-circle in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/semcrc.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #radius.
        r=e1.get()
        r1=float(r)
        #calculating area.
        ar=pi*(r1**2)*(0.5)
        c=str(round(ar,3))
        #calculating circumference.
        per=(pi*r1)+(2*r1)
        d=str(round(per,3))
        
        l1="The area of the semi-circle is "+c+' cm\u00b2'+'.'
        l2="The circumference of the semi-circle is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_pent():
    top = Toplevel()                        #creating a new window.
    top.title('PENTAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of pentagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of pentagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/pent.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=(0.25)*(sqrt(5*(5+2*sqrt(5))))*(s1**2)
        c=str(round(ar,3))
        #calculating circumference.
        per=5*s1
        d=str(round(per,3))
        
        l1="The area of the pentagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the pentagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_hexa():
    top = Toplevel()                        #creating a new window.
    top.title('HEXAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of hexagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of hexagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/hex.png'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=(0.5)*(3*(sqrt(3)))*(s1**2)
        c=str(round(ar,3))
        #calculating circumference.
        per=6*s1
        d=str(round(per,3))
        
        l1="The area of the hexaagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the hexagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_hepta():
    top = Toplevel()                        #creating a new window.
    top.title('HEPTAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of heptagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of heptagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/hept.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=(7/4)*(s1**2)*((cos(pi/7)/(sin(pi/7))))
        c=str(round(ar,3))
        #calculating circumference.
        per=7*s1
        d=str(round(per,3))
        
        l1="The area of the heptagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the heptagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation popup.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_octa():
    top = Toplevel()                        #creating a new window.
    top.title('OCTAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of octagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of octagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/oct.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=2*(1+sqrt(2))*(s1**2)
        c=str(round(ar,3))
        #calculating circumference.
        per=8*s1
        d=str(round(per,3))
        
        l1="The area of the octagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the octagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_nona():
    top = Toplevel()                        #creating a new window.
    top.title('NONAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of nonagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of nonagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/nano.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)

    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=(9/4)*(s1**2)*((cos(pi/9)/(sin(pi/9))))
        c=str(round(ar,3))
        #calculating circumference.
        per=9*s1
        d=str(round(per,3))
        
        l1="The area of the nonagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the nonagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_deca():
    top = Toplevel()                        #creating a new window.
    top.title('DECAGON')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of decagon.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter length of the side of decagon in cm below:')
    label1.grid(row=1, column=0, sticky=W)

    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e1.grid(row=1, column=1)
    
    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/deca.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)

    def button_ar():
        #side length.
        s=e1.get()
        s1=float(s)
        #calculating area.
        ar=(2.5)*(s1**2)*(sqrt(5+2*(sqrt(5))))
        c=str(round(ar,3))
        #calculating circumference.
        per=10*s1
        d=str(round(per,3))
        
        l1="The area of the decagon is "+c+' cm\u00b2'+'.'
        l2="The circumference of the decagon is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_rhomb():
    top = Toplevel()                        #creating a new window.
    top.title('RHOMBUS')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of rhombus.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the 1st diagonal of rhombus in cm below:')
    label2=Label(top, text='Enter the 2nd of rhombus in cm below:')
    label3=Label(top, text='Enter the length of the side of rhombus in cm below:')
    label1.grid(row=1, column=0, sticky=W)
    label2.grid(row=2, column=0, sticky=W)
    label3.grid(row=3, column=0, sticky=W)
   
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e2=Entry(top, borderwidth='1')
    e3=Entry(top, borderwidth='1')
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/rhom.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        #1st diagonal.
        d=e1.get()
        d1=float(d)
        #2nd diagonal.
        D=e2.get()
        D1=float(D)
        #sides 1,2,3.
        s1=e3.get()
        S1=float(s1)

        #calculating area.
        ar=(D1*d1)/2
        c=str(round(ar,3))
        #calculating perimeter.
        per=(4*S1)
        d=str(round(per,3))
        
        l1="The area of the rhombus is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the rhombus is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=8, column=0, columnspan=3)
        label02.grid(row=9, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=7,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_paralgrm():
    top = Toplevel()                        #creating a new window for triangle.
    top.title('PARALLELOGRAM')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of parallelogram.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the HEIGHT of the parallelogram in cm below:')
    label2=Label(top, text='Enter the BASE of the parallelogram in cm below:')
    label3=Label(top, text='Enter the length of the side adjacent to base of parallelogram in cm below:')
    label1.grid(row=1, column=0, sticky=W)
    label2.grid(row=2, column=0, sticky=W)
    label3.grid(row=3, column=0, sticky=W)
    
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e2=Entry(top, borderwidth='1')
    e3=Entry(top, borderwidth='1')
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/prlgram.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        #height.
        h=e1.get()
        h1=float(h)
        #base.
        b=e2.get()
        b1=float(b)
        #adjacent side.
        s=e3.get()
        s1=float(s)
        
        #calculating area.
        ar=(b1*h1)
        c=str(round(ar,3))
        #calculating perimeter.
        per=2*(s1+b1)
        d=str(round(per,3))
        
        l1="The area of the parallelogram is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the parallelogram is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=7, column=0, columnspan=3)
        label02.grid(row=8, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=6,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_kite():
    top = Toplevel()                        #creating a new window.
    top.title('KITE')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of kite.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the 1st diagonal of kite in cm below:')
    label2=Label(top, text='Enter the 2nd diagonal of kite in cm below:')
    label3=Label(top, text='Enter the length of shorter side of kite in cm below:')
    label4=Label(top, text='Enter the length of longer side of kite in cm below:')
    label1.grid(row=1, column=0, sticky=W)
    label2.grid(row=2, column=0, sticky=W)
    label3.grid(row=3, column=0, sticky=W)
    label4.grid(row=4, column=0, sticky=W)
   
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e2=Entry(top, borderwidth='1')
    e3=Entry(top, borderwidth='1')
    e4=Entry(top, borderwidth='1')
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/kite.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        #1st diagonal.
        d=e1.get()
        d1=float(d)
        #2nd diagonal.
        D=e2.get()
        D1=float(D)
        #sides 1 & 2.
        s1=e3.get()
        S1=float(s1)
        s2=e4.get()
        S2=float(s2)

        #calculating area.
        ar=(D1*d1)/2
        c=str(round(ar,3))
        #calculating perimeter.
        per=(S1+S2)*2
        d=str(round(per,3))
        
        l1="The area of the kite is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the kite is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=8, column=0, columnspan=3)
        label02.grid(row=9, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=7,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


def button_trapezoid():
    top = Toplevel()                        #creating a new window.
    top.title('TRAPEZOID')             #adding title for the sub-window.
    
    header=Label(top, text='Calculating the area of trapezoid.')               #main header for sub-window.
    header.grid(row=0, column=0, columnspan=3)

    label1=Label(top, text='Enter the HEIGHT of trapezoid in cm below:')
    label2=Label(top, text='Enter the 1st || side of trapezoid in cm below:')
    label3=Label(top, text='Enter the 2nd || side of trapezoid in cm below:')
    label4=Label(top, text='Enter the 3rd side of trapezoid in cm below:')
    label5=Label(top, text='Enter the 4th side of trapezoid in cm below:')
    label1.grid(row=1, column=0, sticky=W)
    label2.grid(row=2, column=0, sticky=W)
    label3.grid(row=3, column=0, sticky=W)
    label4.grid(row=4, column=0, sticky=W)
    label5.grid(row=5, column=0, sticky=W)
   
    e1=Entry(top, borderwidth='1')             #entry box for entering the values.
    e2=Entry(top, borderwidth='1')
    e3=Entry(top, borderwidth='1')
    e4=Entry(top, borderwidth='1')
    e5=Entry(top, borderwidth='1')
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)

    i1=ImageTk.PhotoImage(Image.open('/Users/sathvikrshetty/Downloads/trap.jpg'))
    i_label=Label(top, image=i1)
    i_label.grid(row=90, column=0)
    
    def button_ar():
        
        #height.
        h=e1.get()
        h1=float(h)
        #sides 1,2,3.
        s1=e2.get()
        s2=e3.get()
        s3=e4.get()
        s4=e5.get()
        S1=float(s1)
        S2=float(s2)
        S3=float(s3)
        S4=float(s4)

        #calculating area.
        ar=((S1+S2)*h1)/2
        c=str(round(ar,3))
        #calculating perimeter.
        per=(S1+S2+S3+S4)
        d=str(round(per,3))
        
        l1="The area of the trapezoid is "+c+' cm\u00b2'+'.'
        l2="The Perimeter of the trapezoid is "+d+' cm.'
        
        label01=Label(top, text=l1)
        label02=Label(top, text=l2)
        label01.grid(row=8, column=0, columnspan=3)
        label02.grid(row=9, column=0, columnspan=3)
    #creating a button to proceed with the process.
    button_ar=Button(top, text='CLICK FOR THE RESULT!!!', command=button_ar).grid(row=7,column=0, columnspan=3)

    #creating an confirmation box.
    def popup():
        a = messagebox.askyesno('askyesno', 'Do You Want To Quit?')
        Label(top, text=a).grid(row=0, column=0)
        if a == 1:
           top.quit()
        else:
           pass
    Button(top, text='QUIT', command = popup).grid(row=99, column=99)

    top.mainloop()


#adding buttons.
button_sqr=Button(root, text='SQUARE', padx=42, pady=3, activebackground='grey', command=button_sqr).grid(row=2, column=0)
button_rect=Button(root, text='RECTANGLE', padx=30, pady=3, activebackground='grey',command=button_rect).grid(row=3, column=0)
button_tri=Button(root, text='TRIANGLE', padx=37, pady=3, activebackground='grey',command=button_tri).grid(row=4, column=0)
button_crcl=Button(root, text='CIRCLE', padx=46, pady=3, activebackground='grey',command=button_crcl).grid(row=5, column=0)
button_semicrcl=Button(root, text='SEMI-CIRCLE', padx=28, pady=3, activebackground='grey',command=button_semicrcl).grid(row=6, column=0)
button_pent=Button(root, text='PENTAGON', padx=33, pady=3, activebackground='grey',command=button_pent).grid(row=7, column=0)
button_hexa=Button(root, text='HEXAGON', padx=37, pady=3, activebackground='grey',command=button_hexa).grid(row=8, column=0)
button_hepta=Button(root, text='HEPTAGON', padx=33, pady=3, activebackground='grey',command=button_hepta).grid(row=9, column=0)
button_octa=Button(root, text='OCTAGON', padx=36, pady=3, activebackground='grey',command=button_octa).grid(row=10, column=0)
button_nona=Button(root, text='NONAGON', padx=35, pady=3, activebackground='grey',command=button_nona).grid(row=11, column=0)
button_deca=Button(root, text='DECAGON', padx=36, pady=3, activebackground='grey',command=button_deca).grid(row=12, column=0)
button_rhomb=Button(root, text='RHOMBUS', padx=36, pady=3, activebackground='grey',command=button_rhomb).grid(row=13, column=0)
button_paralgrm=Button(root, text='PARALLELOGRAM', padx=13, pady=3, activebackground='grey',command=button_paralgrm).grid(row=14, column=0)
button_kite=Button(root, text='KITE', padx=55, pady=3,activebackground='grey', command=button_kite).grid(row=15, column=0)
button_trapezoid=Button(root, text='TRAPEZOID', padx=33, pady=3, activebackground='grey',command=button_trapezoid).grid(row=16, column=0)

#opening the window.
root.mainloop()