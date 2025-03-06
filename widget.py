#! /usr/bin/python3 
import os
import tkinter as tk

 
def toggle_terminal():
    status = os.popen("wmctrl -l | grep Alacritty").read()
    if status:
        os.system("wmctrl -r Alacritty -b toggle,hidden")
    else:
        os.system("alacritty -e bash -c 'python3 /home/leugim/Documentos/GitHub/DynamicAssist/test.py' &")
        os.system("sleep 1 && wmctrl -r Alacritty -e 0,1300,750,400,300")

url = 'http://localhost:5005/webhooks/rest/webhook'

root = tk.Tk()
root.geometry("50x50+970+718") # Define posição
root.overrideredirect(True)  # Remove bordas
root.attributes("-topmost", True)  # Mantém no topo

btn = tk.Button(root, text="●", font=("Arial", 18), command=toggle_terminal, bg="black", fg="white", relief="flat")
btn.pack(fill=tk.BOTH, expand=True)

root.mainloop()