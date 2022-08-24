from tkinter import *
from PIL import ImageTk, Image
import qrcode


root = Tk()

root.geometry("1280x1200")

root.iconbitmap("qr_code.ico")

root.title("Qr generator")

def generarQr():
    archivo= Archivo.get()
    url= Url.get()
    qr = qrcode.make(url)
    qr.save("qrs/"+str(archivo)+"png")

    Image=PhotoImage(file="qrs/"+str(archivo)+"png")
    Imagen_visua.config(image=Image)



lbl_img = Image.open("qr_image.png")
lbl_img = lbl_img.resize((200, 200))

img = ImageTk.PhotoImage(file="qr_image.png")

lbl_img = Label(root, image=img)
lbl_img.place( y=0.8)


contenido = Frame()
contenido.config(width=650, height=700)
contenido.place(relx=0.45)


NombreArch=Label(contenido, text="Ingrese el nombre del archivo correspondiente", font=('Arial', 15))
NombreArch.place(x=130, y=50)

Archivo = Entry(contenido, width=75, borderwidth=3)
Archivo.place(x=110, y= 100)

NombreUrl=Label(contenido, text="Ingrese la Url",font=('Arial', 15))
NombreUrl.place(x=270, y=150)

Url= Entry(contenido, width=75, borderwidth=3)
Url.place(x=110, y= 200)


generar = Button(contenido, text="Generar QR", width=30, height=3, bg="gray11", fg="white" , font=('Arial', 11), command=generarQr)
generar.place(x=200, y=250)

Imagen_visua=Label(contenido)
Imagen_visua.place(x=170, y=350)












root.mainloop()