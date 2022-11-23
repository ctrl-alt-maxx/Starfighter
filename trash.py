
import tkinter as tk 



#my_w = tk.Tk()
#my_w.geometry("615x400")  # width and height 
#def my_callback(event):
#     l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))

#l1=tk.Label(my_w,text='to Display',bg='yellow',font=30)
#l1.pack(padx=10,pady=10)
#my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed move
#my_w.mainloop()
   

root = tk.Tk()
root.geometry("615x400")

#def motion(event):
    #x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
#    l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))

#l1=tk.Label(root,text='just move',bg='yellow',font=30)
#l1.pack(padx=10,pady=10)

#root.bind('<Motion>', motion)

   
labelPoints = tk.Label(root, text="Points: ", font = 30, padx=10, pady=10)
labelPoints.place(relx=0.0, rely=0.0, anchor='nw')
   
root.mainloop()
