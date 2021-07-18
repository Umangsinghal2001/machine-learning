import tkinter as tk

app=tk.Tk()
app.geometry("500x550")
app.title("basic calculator")

result=tk.Variable(app)

tk.Label(app,justify='right',font=('Arial',18,'bold'),textvariable=result).place(x=200,y=50,width=100,height=50)

def operator(e):
      exp=str(result.get())
      if e=="=":
          result.set(eval(exp))
      else:    
       exp=exp+e
       result.set(exp)

tk.Button(app,text='+',width=2,command=lambda :operator('+')).place(x=450,y=100,)
tk.Button(app,text='-',width=2,command=lambda :operator('-')).place(x=450,y=200)
tk.Button(app,text='x',width=2,command=lambda :operator('*')).place(x=450,y=300)
tk.Button(app,text='/',width=2,command=lambda :operator('/')).place(x=450,y=400)
tk.Button(app,text='1',width=2,command=lambda :operator('1')).place(x=150,y=100)
tk.Button(app,text='2',width=2,command=lambda :operator('2')).place(x=250,y=100)
tk.Button(app,text='3',width=2,command=lambda :operator('3')).place(x=350,y=100)
tk.Button(app,text='4',width=2,command=lambda :operator('4')).place(x=150,y=200)
tk.Button(app,text='5',width=2,command=lambda :operator('5')).place(x=250,y=200)
tk.Button(app,text='6',width=2,command=lambda :operator('6')).place(x=350,y=200)
tk.Button(app,text='7',width=2,command=lambda :operator('7')).place(x=150,y=300)
tk.Button(app,text='8',width=2,command=lambda :operator('8')).place(x=250,y=300)
tk.Button(app,text='9',width=2,command=lambda :operator('9')).place(x=350,y=300)
tk.Button(app,text='0',width=2,command=lambda :operator('0')).place(x=250,y=400)
tk.Button(app,text='=',width=2,command=lambda :operator('=')).place(x=350,y=400)
tk.Button(app,text='.',width=2,command=lambda :operator('.')).place(x=150,y=400)
tk.Button(app,text='clr',width=2,command=lambda :result.set("")).place(x=50,y=300)



tk.mainloop()

