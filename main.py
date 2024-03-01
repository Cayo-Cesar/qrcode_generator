import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from ttkthemes import ThemedStyle

def generate():
    link = data.get()
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    filename = filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    if filename:
        img.save(filename + ".png")
        messagebox.showinfo("QR Code Generator", "QR Code gerado e salvo com sucesso!")
        img.show()
    else:
        messagebox.showerror("QR Code Generator", "Erro ao salvar o QR Code!")

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x150")

style = ThemedStyle(window)
style.set_theme("equilux")

bg_color = style.lookup("TFrame", "background")

window.configure(bg=bg_color)

label = ttk.Label(window, text="Insira o link para gerar o QR Code", font=('Arial', 14))
label.pack(pady=10)

data = tk.StringVar()
entry = ttk.Entry(window, textvariable=data, font=('Arial', 12), width=50)
entry.pack(pady=5)

button = ttk.Button(window, text="Gerar QR Code", command=generate)
button.pack(pady=10)

window.mainloop()
