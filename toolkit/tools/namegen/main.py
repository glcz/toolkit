#!/usr/bin/env python
import click
import random
from pathlib import Path

# Charger le fichier txt contenant les entrées
namedict = Path(__file__).parent / "dict.txt"

# Dict des possibilités
larousse = {}
with open(namedict) as entries:
    for cle, line in enumerate(entries, start=1):
        larousse[cle] = line.rstrip()

# Variables
amplitude = len(larousse) ** 2
message = f"Généré depuis {amplitude} possibilités"

# Fonctions

def tirage():
    part = larousse[random.randint(1, len(larousse))].capitalize()
    return part

@click.command(epilog="Exemple : toolkit namegen -cn 8 -s _")
@click.option('-n', default=3, help=": Nombre de propositions à générer (par défaut 3)")
@click.option('-s', default="", help=": Séparateur (par défaut aucun)")
@click.option('-c', is_flag=True, help=": Ajouter un nombre à la fin")
def start(n, s, c):
    """Génère des noms aléatoires."""
    resultats = []
    for _ in range(n):
        if not c:
            username = tirage() + s + tirage()
        else:
            username = tirage() + s + tirage() + s + str(random.randint(111, 999))
        resultats.append(username)
    print(" / ".join(resultats))
    if amplitude >= n:
        click.echo(click.style(message, fg="yellow"))
    else:
        click.echo(click.style(message + " (attention aux doublons)", fg="red"))

# Programme

if __name__ == "__main__":
    start()