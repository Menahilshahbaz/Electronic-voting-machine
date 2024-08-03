from pathlib import Path
import tkinter as tk
import EVM_System, Admin, Nominee

from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"I:\Projects-main\Electronic Voting Sys\assets\main")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class UserDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.username = None
        self.password = None
        self.who_is = title
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        if self.who_is == "Admin Login":
            tk.Label(master, text="Enter Username:").grid(row=1)
            self.username_entry = tk.Entry(master)
            self.username_entry.grid(row=1, column=1)
            tk.Label(master, text="Enter Password:").grid(row=2)
            self.password_entry = tk.Entry(master, show='*')
            self.password_entry.grid(row=2, column=1)
        elif self.who_is == "Candidate Login":
            tk.Label(master, text="Enter CNIC:").grid(row=1)
            self.username_entry = tk.Entry(master)
            self.username_entry.grid(row=1, column=1)
            tk.Label(master, text="Enter Password:").grid(row=2)
            self.password_entry = tk.Entry(master, show='*')
            self.password_entry.grid(row=2, column=1)
        elif self.who_is == "Voter Login":
            tk.Label(master, text="Enter CNIC:").grid(row=1)
            self.username_entry = tk.Entry(master)
            self.username_entry.grid(row=1, column=1)
            tk.Label(master, text="Enter Name:").grid(row=2)
            self.password_entry = tk.Entry(master)
            self.password_entry.grid(row=2, column=1)
        
        return self.username_entry  # initial focus

    def apply(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

def get_admin_login():
    dialog = UserDialog(window, "Admin Login")
    return dialog.username, dialog.password

def get_candidate_login():
    drv_dialog = UserDialog(window, "Candidate Login")
    return drv_dialog.username, drv_dialog.password

def get_voter_login():
    std_dialog = UserDialog(window, "Voter Login")
    return std_dialog.username, std_dialog.password

def admin_login():
        username, password = get_admin_login()
        if username == None or password == None:
            pass
        else:
            if EVM_System.vm.admin_login(username, password):
                messagebox.showinfo("Login Success", "Admin logged in successfully!")
                window.destroy()
                Admin.admin_canvas(main_window)
            else:
                messagebox.showerror("Login Failed", "Wrong Username or Password!")

def candidate_login():
        cnic, password = get_candidate_login()
        if cnic == None or password == None:
            pass
        else:
            if EVM_System.vm.candidate_login(cnic, password):
                text = f"Logged in as :  "
                text += f"{EVM_System.vm.candidates[cnic].name} !"
                messagebox.showinfo("Login Successfuly", text)
                window.destroy()
                Nominee.candidate_canvas(main_window, cnic)
            else:
                messagebox.showerror("Login Failed", "Wrong Username or Password!")

def voter_login():
        cnic, name = get_voter_login()
        if cnic == None or name == None:
            pass
        else:
            if EVM_System.vm.voter_login(cnic):
                if EVM_System.vm.nota_voter(cnic):
                    EVM_System.vm.add_voter(name, cnic)
                text = f"Logged in as :  "
                text += f"{EVM_System.vm.voters[cnic].name} !"
                messagebox.showinfo("Login Successfuly", text)
                EVM_System.vm.voter_functions(cnic)    
            else:
                messagebox.showerror("Login Failed", "This CNIC is of Candidate!")

def exit():
    window.quit()

def main_window():
    global window
    window = Tk()
    window.title("Electronic Voting Machine")
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
        command=lambda: exit(),
        relief="flat"
    )
    button_1.place(
        x=473.0,
        y=313.0,
        width=135.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: voter_login(),
        relief="flat"
    )
    button_2.place(
        x=473.0,
        y=268.0,
        width=135.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: candidate_login(),
        relief="flat"
    )
    button_3.place(
        x=473.0,
        y=223.0,
        width=135.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: admin_login(),
        relief="flat"
    )
    button_4.place(
        x=473.0,
        y=178.0,
        width=135.0,
        height=30.0
    )
    window.resizable(False, False)
    window.mainloop()

main_window()