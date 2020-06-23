#####################################################
### hier entsteht mein eigener Passwort-Generator ###
###                    Hufi                       ###
###                 21/06/2020                    ###
#####################################################

######################################################################
                         ### IMPORTE ###

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import pyperclip


######################################################################
                           ### GUI ###

root = tkinter.Tk()
root.title("Password Generator")
root.geometry("600x150")
root.iconbitmap("images/PassGen Icon.ico")
root.configure(bg="grey")


######################################################################
                         ### BILDER ###

generateImg = Image.open("images/generateButton.png")
resGenImg = generateImg.resize((90, 30),Image.ANTIALIAS)
resizedGenerate = ImageTk.PhotoImage(resGenImg)

zwischenImg = Image.open("images/zwischenablageButton.png")
resZwiImg = zwischenImg.resize((90, 30), Image.ANTIALIAS)
resizedZwi = ImageTk.PhotoImage(resZwiImg)

beendenImg = Image.open("images/beendenButton.png")
resBeeImg = beendenImg.resize ((90, 30), Image.ANTIALIAS)
resizedBee = ImageTk.PhotoImage(resBeeImg)


######################################################################
                        ### VARIABLEN ###

uppercase_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
zahlen_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sonderzeichen_list = ["#", "+", "*", "~", "?", "&", "%", "$", "§", "!", "@", ">", "<", ",", ".", ";", ":", "_", "-"]

### diese Vars ermöglichen die Inbetriebnahme der Radiobuttons und Checkboxes
uppercasecheckvar = BooleanVar()
lowercasecheckvar = BooleanVar() #Boolean, also True/False-Werte
SZvar = BooleanVar()
zahlencheckvar = BooleanVar()
stellenvariable = IntVar() #Intvar, um 8, 10 oder 12 einzutragen und damit die Längedes PWs festzusetzen.

password = "-" ##variable,um Passwort als String zu setzen, Bindestrich wird nachher gelöscht.

######################################################################
                    ### FUNKTIONEN  FÜR BUTTONS ###


def generate():
    pw_ausgabe.delete(0, 40)
    laengebestimmen()
    pw_ausgabe.insert(0, password1)
    labelgen()

def zwischenablage():
    finalPW = pw_ausgabe.get()
    pyperclip.copy(finalPW)
    spam = pyperclip.paste()
    labelzwi()

######################################################################
                  ### BUTTONS, LABELS & FELDER ###

passlabel = Label(root, text="Ihr Passwort:", bg="grey").grid(row=0, column=0)

pw_ausgabe = Entry(root, width=20, font=("Times New Roman", 18))
pw_ausgabe.grid(row=0, column=1, columnspan=2)

generateButton = Button(root, bg="grey", image=resizedGenerate, command=generate).grid(row=0, column=4)
zwischenablageButton = Button(root, bg="grey", image=resizedZwi, command=zwischenablage).grid(row=1, column=4)
beendenButton = Button(root, image=resizedBee, bg="grey", command=quit).grid(row=2, column=4)

achterradio = Radiobutton(root, text="8 Stellen", bg="grey", variable=stellenvariable, value=8).grid(row=1, column=0)
zehnerradio = Radiobutton(root, text="10 Stellen", bg="grey", variable=stellenvariable, value=10).grid(row=1, column=1)
zwoelferradio = Radiobutton(root, text="12 Stellen", bg="grey", variable=stellenvariable, value=12).grid(row=1, column=2)


lowercasecheck = Checkbutton(root,text = "inkl. Kleinbuchstaben", bg="grey", variable=lowercasecheckvar).grid(row=2, column=0)
uppercasecheck = Checkbutton(root,text = "inkl. Großbuchstaben", bg="grey", variable=uppercasecheckvar).grid(row=2, column=1)
sonderzeichencheck = Checkbutton(root, text = "inkl. Sonderzeichen", bg="grey", variable=SZvar).grid(row=2, column=2)
zahlencheck = Checkbutton(root,text = "inkl. Zahlen", bg="grey", variable=zahlencheckvar).grid(row=2, column=3)

######################################################################
                         ### FUNKTIONEN ###

### dieser Block ermöglicht, die Listen je nach Auswahl zusammenzuführen.
def dazutun():
    global uppercasecheckvar, lowercasecheckvar, SZvar, zahlencheckvar, zahlen_list, sonderzeichen_list, uppercase_list, lowercase_list
    if uppercasecheckvar.get() == True and lowercasecheckvar.get() == False and SZvar.get() == False and zahlencheckvar.get() == False:
        passlist = uppercase_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == True and SZvar.get() == False and zahlencheckvar.get() == False:
        passlist = uppercase_list + lowercase_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == True and SZvar.get() == True and zahlencheckvar.get() == False:
        passlist = uppercase_list + lowercase_list + sonderzeichen_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == True and SZvar.get() == False and zahlencheckvar.get() == True:
        passlist = uppercase_list + lowercase_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == False and SZvar.get() == True and zahlencheckvar.get() == False:
        passlist = sonderzeichen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == True and SZvar.get() == True and zahlencheckvar.get() == False:
        passlist = lowercase_list + sonderzeichen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == True and SZvar.get() == True and zahlencheckvar.get() == True:
        passlist = lowercase_list + sonderzeichen_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == True and SZvar.get() == False and zahlencheckvar.get() == True:
        passlist = lowercase_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == True and SZvar.get() == False and zahlencheckvar.get() == False:
        passlist = lowercase_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == True and SZvar.get() == True and zahlencheckvar.get() == True:
        passlist = uppercase_list + lowercase_list + sonderzeichen_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == False and SZvar.get() == False and zahlencheckvar.get() == True:
        passlist = zahlen_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == False and SZvar.get() == True and zahlencheckvar.get() == False:
        passlist = uppercase_list + sonderzeichen_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == False and SZvar.get() == True and zahlencheckvar.get() == True:
        passlist = uppercase_list + sonderzeichen_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == False and lowercasecheckvar.get() == False and SZvar.get() == True and zahlencheckvar.get() == True:
        passlist =  sonderzeichen_list + zahlen_list
        return passlist
    elif uppercasecheckvar.get() == True and lowercasecheckvar.get() == False and SZvar.get() == False and zahlencheckvar.get() == True:
        passlist =  uppercase_list + zahlen_list
        return passlist

### dieser Block ermöglicht, das Passwort in der gewünschten Länge zu erstellen. eigentlich HAUPTFUNKTION
def laengebestimmen():
    global password, password1
    passlist= dazutun()
    for x in range(0, stellenvariable.get()):
        password += random.choice(passlist)
        password1 = password[-stellenvariable.get():]

### mit den nächsten 2 Funktionen werden jeweils die Labels generiert, die nach Druck des jeweiligen Buttons ausgegeben werden.
def labelgen():
    Ausgabe = Label(root, text="Bitte vergiss nicht, dein Passwort sicher aufzubewahren!", font=("Helvetica 11 bold") , fg="firebrick",bg="grey")
    Ausgabe.grid(row=3, column=0, columnspan=4)

def labelzwi():
    gespeichertMsg = Label(root, text="Dein Passwort ist in der Zwischenablage.", font=("Helvetica 9"), fg="white", bg="grey")
    gespeichertMsg.grid(row=4, column=0, columnspan=4)

######################################################################
                     ### TATSÄCHLICHER RUN ###

root.mainloop()