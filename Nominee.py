from pathlib import Path
import tkinter as tk
import EVM_System
from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"I:\Projects-main\Electronic Voting Sys\assets\Nominee")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PswdDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.new_pswd = None
        self.old_pswd = None
        self.confirm_pswd = None
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        tk.Label(master, text="Old Password:").grid(row=1)
        self.old_pswd_entry = tk.Entry(master)
        self.old_pswd_entry.grid(row=1, column=1)

        tk.Label(master, text="New Password:").grid(row=2)
        self.new_pswd_entry = tk.Entry(master)
        self.new_pswd_entry.grid(row=2, column=1)

        tk.Label(master, text="Confirm Password:").grid(row=3)
        self.confirm_pswd_entry = tk.Entry(master)
        self.confirm_pswd_entry.grid(row=3, column=1)
        return self.old_pswd_entry  # initial focus

    def apply(self):
        self.old_pswd = self.old_pswd_entry.get()
        self.new_pswd = self.new_pswd_entry.get()
        self.confirm_pswd = self.confirm_pswd_entry.get()

def get_pswd_details():
    dialog = PswdDialog(window, "Change Password")
    return dialog.old_pswd, dialog.new_pswd, dialog.confirm_pswd


def change_pswd(cnic):
    old, new, confirm = get_pswd_details()
    if old != None:
        EVM_System.vm.change_driver_password(cnic, old, new, confirm)
    else:
        pass

def candidate_canvas(back_to_main_window, cnic):
    global window
    window = Tk()
    window.title("Nominee Login")
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
        x=470.0,
        y=311.0,
        width=135.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: EVM_System.vm.candidate_results(cnic),
        relief="flat"
    )
    button_2.place(
        x=470.0,
        y=264.0,
        width=135.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_pswd(cnic),
        relief="flat"
    )
    button_3.place(
        x=470.0,
        y=217.0,
        width=135.0,
        height=30.0
    )

    canvas.create_text(
        457.0,
        135.0,
        anchor="nw",
        text="Nominee ",
        fill="#FFFFFF",
        font=("Josefin Sans Bold", 40 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
