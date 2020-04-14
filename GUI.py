from tkinter import *
import sounddevice as sd
from scipy.io.wavfile import write
import myspsolution as my

window = Tk()

window.title("TAU6")
window.geometry("500x200")

fs = 44100  # Sample rate
seconds = 15  # Duration of recording

def record():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)
    m = "output"
    p =r"C:\Users\katey\Desktop\6.835\FinalProject"
    try:
        sr = "rate of speech: " + my.myspsr(m,p)
    except:
        sr = "rate of speech: n/a"
    try:
        atc = "rate of articulation: " +my.myspatc(m,p)
    except:
        atc = "rate of articulation: n/a"
    try:
        paus = "number of pauses: " +my.mysppaus(m,p)
    except:
        paus = "number of pauses: n/a"
    try:
        bala = "ratio of speach to pauses: " +my.myspbala(m,p)
    except:
        bala = "ratio of speech to pauses: n/a"
    lbl['text'] =sr+"\n"+atc+"\n"+paus+"\n"+bala
    btn['text']="Record"
    return
    

def clicked():

    btn['text']="Recording"
    lbl['text'] = "..."
    record()
    return

btn = Button(window, text="Record", command=clicked)

btn.grid(column=1, row=0)

lbl = Label(window, text="Waiting for sound recording")

lbl.grid(column=0, row=1)



window.mainloop()
