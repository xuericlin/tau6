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
            guiref.label.set("Recording! Please wait...\n\n")
            guiref.button.set("...")
            fs = 44100  # Sample rate
            seconds = 60  # Duration of recording
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            guiref.label.set("Analyzing your recording...\n\n")
            write('output.wav', fs, myrecording)
            m = "output"
            p =r"C:\Users\katey\Desktop\6.835\FinalProject\tau6"
            try:
                mysr = my.myspsr(m,p)
                sr = "your rate of speech: " + mysr +" syllables/sec"
                mysr = int(mysr)
                if mysr <2:
                    sradv = "You're speaking rather slowly.\nSpeed up a bit to speak more fluidly."
                elif mysr >3:
                    sradv = "You're going a bit quickly.\nSlow down a bit to be more understandable."
                else:
                    sradv = "Nice pace!\nSpeaking more measuredly can show determination, while speaking more quickly can show passion."
            except:
                sr = "your rate of speech: n/a"
                sradv = "Try again.\nSpeaking more measuredly can show determination, while speaking more quickly can show passion."
            try:
                myar = my.myspatc(m,p)
                atc = "your rate of articulation: " +myar +" syllables/sec"
                myar = int(myar)
                if myar < 4:
                    aradv = "You're individual words are a bit slow.\nYou can speed up for easier processing."
                elif myar >5:
                    aradv = "You're individual words are a bit fast.\nSlow down and enunciate bettter for improved understanding."
                else:
                    aradv = "What clear articulation!\nYou have very understandable enunciation."
            except:
                atc = "your rate of articulation: n/a"
                aradv = "Try again.\nClear articulation and enunciation will help people understand your speech much better."
#            try:
#                paus = "number of pauses during speech: " +my.mysppaus(m,p)
#            except:
#                paus = "number of pauses: n/a"
            try:
                mybal = my.myspbala(m,p)
                bala = "your ratio of time speaking to pausing: " + mybal
                mybal = float(mybal)
                if mybal <.6:
                    baladv = "You're pausing quite a bit during your speech.\nPausing less can still give your speech weight, while also soundling less choppy."
                elif mybal>.8:
                    baladv = "You're barely pauing at all while speaking.\nTakes some breathes for air in order to let you audience process your words."
                else:
                    baladv = "Nice balance of pausing to speaking.\nTaking your time with your words increases their weight, while still following the thread of your intentions."
            except:
                bala = "your ratio of speech to pauses: n/a"
                baladv = "Try again. Taking your time with your words increases their weight, while still following the thread of your intentions."
            sr+="\n Obama state adress: 2 syl/sec\nweather report: 3 syl/sec\nfootball pep talk: 3 syl/sec"
            atc+="\n Obama state adress: 4 syl/sec\nweather report: 4 syl/sec\nfootball pep talk: 5 syl/sec"
            bala+="\n Obama state adress: .6 \nweather report: .8\nfootball pep talk: .6"
            analysis = sr+"\n\n"+sradv+"\n\n"+atc+"\n\n"+aradv+"\n\n"+bala+"\n\n"+baladv+"\n\nPress the record button to try again."
            guiref.label.set(analysis)
            guiref.button.set("Record")
            

def gui(root, queue):
    label = tk.StringVar()
    label.set("Waiting for sound recording\n\n")
    button = tk.StringVar()
    button.set("Record")

    root.title("TAU6")

    tk.Button(root, font=("Helvetica", 12), textvariable=button, command=lambda : queue.put(Messages.RECORD)).pack()
    tk.Label(root, font=("Helvetica", 13), textvariable=label).pack()
    
    return SimpleNamespace(label=label, button=button)
    

if __name__ == '__main__':
    q = Queue()
    root = tk.Tk()
    guiref = gui(root,q)
    model = SimpleNamespace() #The data managed by your application
    t = threading.Thread(target=updatecycle, args=(guiref, model, q,))
    t.daemon = True #daemonize it, so it will die when the program stops
    t.start()
    tk.mainloop()


    
