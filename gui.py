import tkinter as tk
class APP:
    def _init_(self,master):
        frame=tk.Frame(master)
        frame.pack()
        
        self.hi_there=tk.Button(frame,text="戳一下"，command=self.say_hi)
        self.hi_there.pack()
        
    def say_hi(self):
        print("原谅我这一生放荡不羁爱自由")

root=tk.Tk()
app=APP(root)
root.mainloop()
