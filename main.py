import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("256x208")
root.title("FC-GEN")
root.resizable(False, False)


def get_friend_code(bbb_id: int) -> str:
    b = bbb_id * 11 // 14 % 14
    c = bbb_id * 11 % 14
    return str(bbb_id) + chr(ord("a") + b) + chr(ord("a") + c)


def gen():
    # title2.configure(text="no fuck you")
    if identry.get().isupper() or identry.get().islower():
        title2.configure(text="ID Cannot Contain Letters")
    elif len(identry.get()) < 8:
        title2.configure(text="ID Too Short")
    elif len(identry.get()) > 10:
        title2.configure(text="ID Too Long")
    else:
        c = int(identry.get())
        a = (c - (3 * (c - 1) + 2) // 14) % 14
        if a == 0:
            a = 14
        b = 14 - ((15 - 3 * c) * -1) % 14
        fc = str(c) + chr(a + ord("a") - 1) + chr(b + ord("a") - 1)
        if len(fc) == 10:
            title2.configure(text=(fc.upper() + " (Mobile)"))
        elif len(fc) == 11:
            if fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
            else:
                title2.configure(text="ID Invalid")
        elif len(fc) == 12:
            if fc.startswith("1"):
                title2.configure(text=(fc.upper() + " (Mobile)"))
            elif fc.startswith("4"):
                title2.configure(text=(fc.upper() + " (Steam)"))
            else:
                title2.configure(text="ID Invalid")
        else:
            # title2.configure(text=(fc.upper() + " wait fuck what"))
            title2.configure(text="ID Invalid")


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

root.mainloop()
