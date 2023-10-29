import customtkinter as ctk
import pyperclip

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("256x256")
root.title("FC-GEN")
root.resizable(False, False)


def get_friend_code(bbb_id: int) -> str:
    b = bbb_id * 11 // 14 % 14
    c = bbb_id * 11 % 14
    return str(bbb_id) + chr(ord("a") + b) + chr(ord("a") + c)


def copyfc():
    print("Copied " + fc.upper())
    pyperclip.copy(fc.upper())
    cbutton.configure(text="Copied!")
    print("-------------------")


def gen():
    # title2.configure(text="no fuck you")
    print("Gen Clicked")
    cbutton.configure(text="Copy")
    if identry.get().isupper() or identry.get().islower():
        title2.configure(text="ID Cannot Contain Letters")
        print("ID Has Letters")
    elif len(identry.get()) < 8:
        title2.configure(text="ID Too Short")
        print("ID Is Too Short")
    elif len(identry.get()) > 10:
        title2.configure(text="ID Too Long")
        print("ID Is Too Long")
    else:
        bbb_id = int(identry.get())
        b = bbb_id * 11 // 14 % 14
        c = bbb_id * 11 % 14
        global fc
        fc = str(bbb_id) + chr(ord("a") + b) + chr(ord("a") + c)
        if len(fc) == 10:
            title2.configure(text=(fc.upper() + " (Mobile)"))
            print("ID Is Old Mobile")
            cbutton.configure(state="normal")
        elif len(fc) == 11:
            if fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
                print("ID Is New Mobile 11")
                cbutton.configure(state="normal")
            else:
                title2.configure(text="ID Invalid")
                print("ID Is Invalid")
        elif len(fc) == 12:
            if fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
                print("ID Is New Mobile 12")
                cbutton.configure(state="normal")
            elif fc.startswith("4"):
                title2.configure(text=(fc.upper() + " (Steam)"))
                print("ID Is Steam")
            else:
                title2.configure(text="ID Invalid")
                print("ID Is Invalid")
        else:
            # title2.configure(text=(fc.upper() + " wait fuck what"))
            title2.configure(text="ID Invalid")
            print("ID Is Invalid")

        print("-------------------")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="BBB ID To Friend Code", font=("Nunito", 14))
title.pack(pady=10, padx=5)

identry = ctk.CTkEntry(master=frame, placeholder_text="Insert Friend Code", font=("Nunito", 14))
identry.pack(pady=10, padx=5)

button = ctk.CTkButton(master=frame, text="Generate", command=gen, font=("Nunito", 14))
button.pack(pady=10, padx=5)

title2 = ctk.CTkLabel(master=frame, text="", font=("Nunito", 14))
title2.pack(pady=5, padx=5)

cbutton = ctk.CTkButton(master=frame, text="Copy", command=copyfc, font=("Nunito", 14), state="disabled")
cbutton.pack(pady=10, padx=5)

root.mainloop()
