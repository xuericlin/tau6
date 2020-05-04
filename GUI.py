import tkinter as tk
import sounddevice as sd
from scipy.io.wavfile import write
import myspsolution as my
from queue import Queue
from types import SimpleNamespace
from enum import Enum
import threading


class Messages(Enum):
    RECORD = 0


def updatecycle(guiref, model, queue):
    while True:
        msg = queue.get()
        if msg == Messages.RECORD:
            guiref.label.set("Recording")
            fs = 44100  # Sample rate
            seconds = 10  # Duration of recording
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            guiref.label.set("Analyzing recording")
            write('output.wav', fs, myrecording)
            m = "output"
            p =r"C:\Users\katey\Desktop\6.835\FinalProject\tau6"
            try:
                sr = "your rate of speech: " + my.myspsr(m,p) +" syllables/sec"
            except:
                sr = "your rate of speech: n/a"
            try:
                atc = "your rate of articulation: " +my.myspatc(m,p) +" syllables/sec"
            except:
                atc = "your rate of articulation: n/a"
##            try:
##                paus = "number of pauses during speech: " +my.mysppaus(m,p)
##            except:
##                paus = "number of pauses: n/a"
            try:
                bala = "your ratio of time speaking to pausing: " + my.myspbala(m,p)
            except:
                bala = "your ratio of speech to pauses: n/a"
            sr+="\n Obama state adress: 2 syl/sec\nWeather report: 3 syl/sec\nfootball pep talk: 3 syl/sec"
            atc+="\n Obama state adress: 4 syl/sec\nWeather report: 4 syl/sec\nfootball pep talk: 5 syl/sec"
            bala+="\n Obama state adress: .6 \nWeather report: .8\nfootball pep talk: .6"
            analysis = "\n\n"+sr+"\n\n"+atc+"\n\n"+bala
            guiref.label.set(analysis)
            

def gui(root, queue):
    label = tk.StringVar()
    label.set("Waiting for sound recording")
    recording = tk.BooleanVar()
    recording.set(False)

    root.title("TAU6")
    root.geometry("500x600")
    
    tk.Button(root, font=("Helvetica", 12), text="Record", command=lambda : queue.put(Messages.RECORD)).pack()
    tk.Label(root, font=("Helvetica", 12), textvariable=label).pack()
    
    return SimpleNamespace(label=label)
    

if __name__ == '__main__':
    q = Queue()
    root = tk.Tk()
    guiref = gui(root,q)
    model = SimpleNamespace() #The data managed by your application
    t = threading.Thread(target=updatecycle, args=(guiref, model, q,))
    t.daemon = True #daemonize it, so it will die when the program stops
    t.start()
    tk.mainloop()


    
