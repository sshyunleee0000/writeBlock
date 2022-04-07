from winreg import *
from tkinter import *
from tkinter.messagebox import *


def make_registry(label):
    sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"# Make 'StorageDevicePolicies' key
    key = CreateKey(HKEY_LOCAL_MACHINE, sdp_path)
    try: # Make WriteProtect value (Default 0)
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
        label['text'] = "The registry is made."
    except EnvironmentError:
        label['text'] = "Encountered EnvironmentError"


def check():
    sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, sdp_path, 0, KEY_ALL_ACCESS)
    except OSError:
        return None
    return key


def write_disable(label):
    key = check()
    if key is None:
        label['text'] = "Make registry first."
    else:
        v = EnumValue(key, 0)
        if v[1] == 1:
            label['text'] = "Write is already disabled."
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x1)
                label['text'] = "Write is disabled now."
            except EnvironmentError:
                label['text'] = "Encountered EnvironmentError"


def write_able(label):
    key = check()
    if key is None:
        label['text'] = "Make registry first."
    else:
        v = EnumValue(key, 0)
        if v[1] == 0:
            label['text'] = "Write is already able."
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
                label['text'] = "Write is able now."
            except EnvironmentError:
                label['text'] = "Encountered EnvironmentError"


def delete_registry(label):
    sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
    try: # Delete 'StorageDevicePolicies' key
        DeleteKey(HKEY_LOCAL_MACHINE, sdp_path)
        label['text'] = "Deleted"
    except FileNotFoundError:
        label['text'] = "Make registry first."


def quit_btn():
    msg = askquestion('Confirm', 'Quit?')
    if msg == 'yes':
        exit()


def main():
    root = Tk()
    root.title('WBS')
    root.geometry("350x225")
    root.resizable(width=False, height=False)

    frame = Frame(root)
    frame.configure(bg="#F3F1F5", borderwidth=0)
    frame.pack(side="right", fill="both", expand=True)

    b1 = Button(frame, text='Make registry', command=lambda: make_registry(label), borderwidth=1,
                width=20, height=2, bg="#F4EEFF").grid(row=0, column=0, pady=2)
    b2 = Button(frame, text='Write disable', command=lambda: write_disable(label), borderwidth=1,
                width=20, height=2, bg="#F4EEFF").grid(row=1, column=0, pady=2)
    b3 = Button(frame, text='Write able', command=lambda: write_able(label), borderwidth=1,
                width=20, height=2, bg="#F4EEFF").grid(row=2, column=0, pady=2)
    b4 = Button(frame, text='Delete registry', command=lambda: delete_registry(label), borderwidth=1,
                width=20, height=2, bg="#F4EEFF").grid(row=3, column=0, pady=2)
    b5 = Button(frame, text='Quit', command=quit_btn, borderwidth=1,
                width=10, height=1, bg="#F4EEFF").grid(row=4, column=0, pady=(18, 0), padx=(68, 0))

    left = LabelFrame(root)
    left.configure(bg="#F3F1F5", borderwidth=0)
    left.pack(side="left", fill="both", expand=True)

    wexb = Label(left, text="WexB", width=128, height=3)
    wexb.pack()
    wexb.configure(bg="#F3F1F5", font=("Arial", 18))

    text = Label(left, text="Windows External\nStorage Write\nBlocking Software",
                 bg="#F3F1F5", width=128, height=3)
    text.configure(font=("Arial", 10))
    text.pack()

    label = Label(left, text="Status Bar", bg="#F3F1F5", width=100, height=2)
    label.configure(font=("Arial", 10))
    label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
