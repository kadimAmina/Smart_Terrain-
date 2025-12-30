import tkinter as tk
from tkinter import Listbox 
import os
import subprocess 

root = tk.Tk() 
root.title("Smart Goal")
root.geometry("400x400") 

score_label = tk.Label(root, text="Score: 0", font=("Arial", 16)) 
score_label.pack(pady=10) 
tk.Label(root, text="Goal videos").pack() 
lst = Listbox(root, width=45) 
lst.pack(pady=10) 

score_file = "SmartGoal/score.txt" 
goals_dir = "SmartGoal/goals" 
def refresh(): 
    # Read score 
    if os.path.exists(score_file): 
        with open(score_file, "r") as f: 
            score = f.read().strip() 
        score_label.config(text=f"Score: {score}")
    # Update video list 
    lst.delete(0, tk.END) 
    if os.path.exists(goals_dir): 
        for f in sorted(os.listdir(goals_dir)): 
            if f.endswith(".avi"): 
                lst.insert(tk.END, f) 
    root.after(1000, refresh) 

def play(): 
    sel = lst.curselection() 
    if sel: 
        subprocess.Popen(["vlc", f"{goals_dir}/{lst.get(sel)}"]) 
                                
tk.Button(root, text="Play video", command=play).pack(pady=10) 
refresh()
root.mainloop()