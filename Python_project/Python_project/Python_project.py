import soundfile as sf
#soundfile needs "numpy"
import sounddevice as sd
import tkinter as tk

import tkinter.filedialog as tkf

root = tk.Tk()
#root.geometry("300x200")
root.title("Music player")

def select_file():
    path = tkf.askopenfilename(initialdir =".",title = "choose your file",filetypes =(("wav files","*.wav"),("all files","*.*")))
    path_entry.delete(0,tk.END) #update the entry
    path_entry.insert(0, path)

def select_file1():
    path = tkf.askopenfilename(initialdir =".",title = "choose your file",filetypes =(("wav files","*.wav"),("all files","*.*")))
    path_entry1.delete(0,tk.END)
    path_entry1.insert(0, path)

def select_file2():
    path = tkf.askopenfilename(initialdir =".",title = "choose your file",filetypes =(("wav files","*.wav"),("all files","*.*")))
    path_entry2.delete(0,tk.END)
    path_entry2.insert(0, path)

def play_music(event=None):
    sd.default.device = None,'cable input (vb-audio virtual c, mme' #choose virtual cable as output
    path = path_entry.get()
    print(sd.query_devices())
    data, rate = sf.read(path) #read the wav file into a numpy array and save in data
    sd.play(data) #play the music
    

def play_music1(event=None):
    sd.default.device = None,'cable input (vb-audio virtual c, mme'
    path = path_entry1.get()
    print(sd.query_devices())
    data, rate = sf.read(path)
    
    sd.play(data)

def play_music2(event=None):
    sd.default.device = None,'cable input (vb-audio virtual c, mme'
    path = path_entry2.get()
    print(sd.query_devices())
    data, rate = sf.read(path)
    sd.play(data)

def stop_music(event = None):
    sd.stop()
    sd.default.reset()


path_label = tk.Label(root, text = "F1  File Path: ")
path_entry = tk.Entry(root, text = "")
path_button = tk.Button(root, text = "Browse", command = select_file)
play_buttom = tk.Button(root, text = "play", command = play_music)

root.bind_all("<KeyPress-F1>", play_music) #binding key

path_label.grid(row = 0, column = 0)
path_entry.grid(row = 0,column = 1)
path_button.grid(row = 0,column = 2)
play_buttom.grid(row = 0,column = 3)




path_label1 = tk.Label(root, text = "F2  File Path: ")
path_entry1 = tk.Entry(root, text = "")
path_button1 = tk.Button(root, text = "Browse", command = select_file1)
play_buttom1 = tk.Button(root, text = "play", command = play_music1)
root.bind_all("<KeyPress-F2>", play_music)

path_label1.grid(row = 1, column = 0)
path_entry1.grid(row = 1,column = 1)
path_button1.grid(row = 1,column = 2)
play_buttom1.grid(row = 1,column = 3)



path_label2 = tk.Label(root, text = "F3  File Path: ")
path_entry2 = tk.Entry(root, text = "")
path_button2 = tk.Button(root, text = "Browse", command = select_file2)
play_buttom2 = tk.Button(root, text = "play", command = play_music2)
root.bind_all("<KeyPress-F3>", play_music)



path_label2.grid(row = 2, column = 0)
path_entry2.grid(row = 2,column = 1)
path_button2.grid(row = 2,column = 2)
play_buttom2.grid(row = 2,column = 3)

stop_label = tk.Label(root, text = "Press F4 to stop playing")
stop_buttom = tk.Button(root, text = "stop", command = stop_music)
root.bind_all("<KeyPress-F4>",stop_music)
stop_buttom.grid(row = 3, column = 1)
stop_label.grid(row = 3, column = 0)

root.mainloop()
