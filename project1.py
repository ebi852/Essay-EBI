import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets,linear_model,metrics
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import datasets
from tkinter import*
main=pd.read_csv(r"C:\Users\ebi\Desktop\uuu.csv")
main.drop(columns=['Sample code number'],inplace=True)
main.drop_duplicates()
b=set(main['Class'])
add=dict()
s=0
for s,i in enumerate(b):
    add.update({i:s})
    s+=1
main.replace(add,inplace=True)
main['Bare Nuclei'] = pd.to_numeric(main['Bare Nuclei'], errors='coerce')
main.drop_duplicates(inplace=True)
main.dropna(inplace=True)
main.reset_index(inplace=True,drop=True)
x=main.iloc[:,:-1]
y=main.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
reg =KNeighborsClassifier(n_neighbors=7,metric='euclidean',weights='uniform')
reg.fit(X_train, y_train)
root = Tk()
root.title('ebi')
root.geometry("400x500")
root.config(bg='gray25')
l = Label(root, text='ضخامت :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
l.place(x=20, y=20)
o = Label(root, text='یکنواختی اندازه سلول :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
o.place(x=20, y=50)
z = Label(root, text='یکنواختی شکل سلول :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
z.place(x=35, y=80)
pas = Label(root, text='چسبندگی حاشیه ای :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
pas.place(x=35, y=110)
pas = Label(root, text='اندازه سلول EPITHEL :',font=('b nazanin',16,'bold'), bg='gray25', fg='snow')
pas.place(x=35, y=150)
pas3 = Label(root, text='هسته لخت  :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
pas3.place(x=35, y=180)
pas55 = Label(root, text='کروماتین :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
pas55.place(x=35, y=210)
pas33 = Label(root, text='هستک های طبیعی :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
pas33.place(x=35, y=240)
pas44 = Label(root, text='میتوز :',font=('b nazanin',20,'bold'), bg='gray25', fg='snow')
pas44.place(x=35, y=270)
e = Spinbox(root, bd=3, from_=1, to_=10)  
e.place(x=120, y=25)
k = Spinbox(root, bd=3, from_=1, to_=10)
k.place(x=240, y=55)
i = Spinbox(root, bd=3, from_=1, to_=10)
i.place(x=250, y=85)
s = Spinbox(root, bd=3, from_=0, to_=10)
s.place(x=170, y=215)
t = Spinbox(root, bd=3, from_=0, to_=10)
t.place(x=220, y=250)
c = Spinbox(root, bd=3, from_=0, to_=10)
c.place(x=140, y=280)
w = Spinbox(root, bd=3, from_=1, to_=10)
w.place(x=245, y=120)
w3 = Spinbox(root, bd=3, from_=0, to_=10)
w3.place(x=245, y=155)
w4 =Spinbox(root, bd=3, from_=0, to_=10)
w4.place(x=165, y=185)
u = StringVar()
u.set(None)
def read():
    data1=[int(e.get()),int(k.get()),int(i.get()),int(w.get()),int(w3.get()),int(w4.get()),int(s.get()),int(t.get()),int(c.get())]
    p=reg.predict([data1])
    z2 = Label(root, text=('result:',p),font=('b nazanin',20,'bold'), bg='gray25', fg='red')
    z2.place(x=150, y=300)
kk = Button(root, width=5, height=3, bg='black', fg='snow', text='check', command=read)
kk.place(x=300, y=300)
root.mainloop()
