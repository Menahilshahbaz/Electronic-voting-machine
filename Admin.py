
from pathlib import Path
import tkinter as tk
import EVM_System
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, simpledialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"I:\Projects-main\Electronic Voting Sys\assets\Admin")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ADD_Dialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.cnic = None
        self.username = None
        self.password = None
        self.who_is = title
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))

        tk.Label(master, text="Enter CNIC:").grid(row=1)
        self.cnic_entry = tk.Entry(master)
        self.cnic_entry.grid(row=1, column=1)

        tk.Label(master, text="Enter Name:").grid(row=2)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=2, column=1)

        if self.who_is != "Voter Login":
            tk.Label(master, text="Enter Password:").grid(row=3)
            self.password_entry = tk.Entry(master, show='*')
            self.password_entry.grid(row=3, column=1)
            return self.username_entry  # initial focus

    def apply(self):
        self.cnic = self.cnic_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

def get_add_voter():
    dialog = ADD_Dialog(window, "Add Voter")
    return dialog.cnic, dialog.username, dialog.password

def get_add_candidate():
    dialog = ADD_Dialog(window, "Add Candidate")
    return dialog.cnic, dialog.username, dialog.password

def add_candidate():
    cnic, name, password = get_add_candidate()
    if cnic != None:
        if EVM_System.vm.valid_candidate(cnic):
            EVM_System.vm.add_candidate(name, cnic, password)
            messagebox.showinfo("Success", f"{name} has been added as a Candidate.")
        else:
            messagebox.showerror("Error", "Candidate Already Exists!")
    else:
        pass



def admin_canvas(back_to_main_window):
    global window
    window = Tk()
    window.title("Admin Login")
    window.geometry("650x416")
    window.configure(bg = "#FFFFFF")
    icon_path = relative_to_assets("icon.png")
    window.iconphoto(False, PhotoImage(file=icon_path))

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 416,
        width = 650,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        325.0,
        208.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), back_to_main_window()),
        relief="flat"
    )
    button_1.place(
        x=473.0,
        y=336.0,
        width=135.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: EVM_System.vm.view_results(),
        relief="flat"
    )
    button_2.place(
        x=473.0,
        y=295.0,
        width=135.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: EVM_System.vm.view_details(),
        relief="flat"
    )
    button_3.place(
        x=472.0,
        y=254.0,
        width=135.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_candidate(),
        relief="flat"
    )
    button_4.place(
        x=472.0,
        y=213.0,
        width=135.0,
        height=30.0
    )

    canvas.create_text(
        465.0,
        135.0,
        anchor="nw",
        text="Admin ",
        fill="#FFFFFF",
        font=("Josefin Sans", 48 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
