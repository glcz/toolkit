import main

def mainloop():
    data = ""
    while not data:
        data = input("Texte à coder : ")
        if not data:
            print("Le code QR ne peut pas être vide.")
        else:
            img = qrcode.make(data)
            type(img)
            img.save(data + ".png")
            print("Code QR créé")

mainloop()