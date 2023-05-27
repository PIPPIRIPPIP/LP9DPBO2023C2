from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Ayesha", 3, 3, 10000000))
hunians.append(Rumah("Ali", 5, 2, 500))
hunians.append(Indekos("Firdaus", "Skypaaww", 1000000))
hunians.append(Rumah("Pipaaww", 1, 4, 100))

def show_home():
    # Clear window
    for widget in root.winfo_children():
        widget.destroy()

    # Center window on screen
    window_width = 600
    window_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    # Show home page
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan data pemilik
    i = 0
    Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1
    Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1
    Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1
    if(hunians[index].get_jenis() == "Rumah"):
        Label(d_frame, text="Harga Beli: Rp. " + str(hunians[index].get_harga()) + " juta", anchor="w").grid(row=i, column=0, sticky="w")
        i += 1
    else:
        Label(d_frame, text="Harga Sewa: Rp. " + str(hunians[index].get_harga()), anchor="w").grid(row=i, column=0, sticky="w")
        i += 1

        
    Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    if(hunians[index].get_jenis() == "Indekos"):
        Label(d_frame, text="Nama Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=i, column=0, sticky="w")
        i += 1

    Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=i, column=0, sticky="w")
    
    btn = LabelFrame(top,padx=0,pady=0)
    btn.pack(padx=10,pady=10)
    b_close = Button(btn,text="Close",command=top.destroy)
    b_close.grid(row=0,column=0)


root = tk.Tk()
root.title("Praktikum DPBO")\

# Center window on screen
window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Load and display image
image = Image.open("images/logo.png")
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root,image=photo)
label.pack()

# Add space between image and buttons
space = tk.Label(root,text="")
space.pack()

# Add frame to center buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Add buttons
button1 = tk.Button(button_frame, text="Masuk",command=lambda: show_home())
button1.pack(side=tk.RIGHT)

button2 = tk.Button(button_frame, text="Keluar", command=root.destroy)
button2.pack(side=tk.LEFT)

root.mainloop()
