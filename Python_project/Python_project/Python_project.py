import soundfile as sf
#soundfile needs "numpy"
import sounddevice as sd
import tkinter as tk

import tkinter.filedialog as tkf

root = tk.Tk()
root.geometry("300x200")
root.title("Music player")

def select_file():
    path = tkf.askopenfilename(initialdir =".",title = "choose your file",filetypes =(("wav files","*.wav"),("all files","*.*")))
    path_entry.delete(0,tk.END)
    path_entry.insert(0, path)

def play_music():
    path = path_entry.get()
    print(path)
    data, rate = sf.read(path)
    sd.default.device = None,6
    print(sd.query_devices())
    sd.play(data)

path_label = tk.Label(root, text = "File Path: ")
path_entry = tk.Entry(root, text = "")
path_button = tk.Button(root, text = "Browse", command = select_file)
play_buttom = tk.Button(root, text = "play", command = play_music)

path_label.pack(side = tk.LEFT)
path_entry.pack(side = tk.LEFT)
path_button.pack(side = tk.LEFT)
play_buttom.pack(side = tk.LEFT)


root.mainloop()
