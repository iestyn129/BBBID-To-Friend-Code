# imported for gui
import customtkinter as ctk
# imported for copying
import pyperclip
# imported for checking spaces
import re

import regex

# system for the mistakes that use light mode
ctk.set_appearance_mode("System")
# nice cool blue
ctk.set_default_color_theme("dark-blue")

# no shit dumbass
root = ctk.CTk()
# 🟦
root.geometry("256x256")
# edgy
root.title("FC-GEN")
# no resizing, it makes it look bad
root.resizable(False, False)


def get_friend_code(bbb_id: int) -> str:
    b = bbb_id * 11 // 14 % 14
    c = bbb_id * 11 % 14
    return str(bbb_id) + chr(ord("a") + b) + chr(ord("a") + c)


# thank you zewsic 💞


def copyfc():
    print("Copied " + fc.upper())
    pyperclip.copy(fc.upper())  # your only use in this world
    cbutton.configure(text="Copied!")
    print("-------------------")  # WALLED


def gen():
    # title2.configure(text="no fuck you")  # i miss this
    print("Gen Clicked")  # logging yay
    cbutton.configure(text="Copy")
    # are there any spaces?
    idspace = bool(re.search(r"\s", identry.get()))
    # odd way of doing but that's what stackoverflow says :shruggox:
    if identry.get().isupper() or identry.get().islower():
        title2.configure(text="ID Cannot Contain Letters")
        print("ID Has Letters")  # bills due
        print("-------------------")  # WALLED
    elif idspace:
        title2.configure(text="ID Cannot Contain Spaces")
        print("ID Has Spaces")  # what the fuck are you even typing
        print("-------------------")  # WALLED
    elif any(not c.isalnum() for c in identry.get()):
        title2.configure(text="ID Cannot Contain Special Chars")
        print("ID Has Special Chars")  # what the fuck are you even typing
        print("-------------------")  # WALLED
    elif len(identry.get()) == 0:
        title2.configure(text="ID Cannot Be Blank")
        print("ID Is Blank")  # id assume wubbox64 is short so...
        print("-------------------")  # WALLED
    elif len(identry.get()) < 8:
        title2.configure(text="ID Too Short")
        print("ID Is Too Short")  # id assume wubbox64 is short so...
        print("-------------------")  # WALLED
    elif len(identry.get()) > 10:
        title2.configure(text="ID Too Long")
        print("ID Is Too Long")  # just like my d-
        print("-------------------")  # WALLED
    else:
        bbb_id = int(identry.get())
        b = bbb_id * 11 // 14 % 14
        c = bbb_id * 11 % 14
        # thank you zewsic 💞
        global fc  # stop giving me that stupid yellow underline, it's all good
        fc = str(bbb_id) + chr(ord("a") + b) + chr(ord("a") + c)
        # checking if it's an old mobile code
        if len(fc) == 10:  # yknow what else is 10 long?
            title2.configure(text=(fc.upper() + " (Mobile)"))
            print("ID Is Old Mobile")  # blackberry
            cbutton.configure(state="normal")
        elif len(fc) == 11:  # yknow what else is 11 long?
            # mobile codes after 10 start with 1 so uhh yeah checking for that
            if fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
                print("ID Is New Mobile 11")
                cbutton.configure(state="normal")
            else:
                title2.configure(text="ID Invalid")  # *loud ass buzzer sound* WRONG
                print("ID Is Invalid")
        elif len(fc) == 12:  # hey 12 inches in a foot........ yknow what else-
            # steam ids start with 4 soooo... you get it
            if fc.startswith("4"):
                title2.configure(text=(fc.upper() + " (Steam)"))  # 💨
                print("ID Is Steam")  # fc = 💨
                cbutton.configure(state="normal")
            elif fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
                print("ID Is New Mobile 12")
                cbutton.configure(state="normal")
            else:
                title2.configure(text="ID Invalid")
                print("ID Is Invalid")  # *louder asser buzzerer sounder* WRONG AGAIN IDIOT
        else:
            # title2.configure(text=(fc.upper() + " wait fuck what"))
            title2.configure(text="ID Invalid")
            print("ID Is Invalid")  # *louderer asserer buzzererer sounderer* WRONG A-FUCKING-GAIN YOU IDIOT

        print("-------------------")  # WALLED


frame = ctk.CTkFrame(master=root)  # frame = clean
frame.pack(pady=10, padx=10, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="BBB ID To Friend Code", font=("Nunito", 14))  # what it is         soul brother
title.pack(pady=10, padx=5)

identry = ctk.CTkEntry(master=frame, placeholder_text="Insert Friend Code", font=("Nunito", 14))  # ebtry
identry.pack(pady=10, padx=5)

button = ctk.CTkButton(master=frame, text="Generate", command=gen, font=("Nunito", 14))  # yay button
button.pack(pady=10, padx=5)

title2 = ctk.CTkLabel(master=frame, text="", font=("Nunito", 14))  # copied you dumb fuck
title2.pack(pady=5, padx=5)

cbutton = ctk.CTkButton(master=frame, text="Copy", command=copyfc, font=("Nunito", 14), state="disabled")  # yay button2
cbutton.pack(pady=10, padx=5)

root.mainloop()  # ♾️
