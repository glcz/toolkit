#!/usr/bin/env python
import click
import qrcode
from platformdirs import user_pictures_dir
import io
from pathlib import Path

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
)

@click.command(epilog="Exemple : xxxxxxxxxx")
@click.argument('texttoqr')
@click.option('-c', default="black", help="Couleur du code")
@click.option('-b', default="white", help="Couleur de fond")
def start(texttoqr, c, b):
    """Génère des codes QR."""
    # Création du QR
    qr.add_data(texttoqr)
    qr.make(fit=True)
    # Affichage du code dans le terminal
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())
    # Génération de l'image sur le disque
    imagepath = (Path(user_pictures_dir()) / texttoqr).with_suffix(".png")
    img = qr.make_image(fill_color=c, back_color=b)
    img.save(imagepath)
    # Validation
    click.echo(click.style("Image créée : " + str(imagepath), fg="green"))

# Programme

if __name__ == "__main__":
    start()

