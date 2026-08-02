#!/usr/bin/env python
import click
import random
from pathlib import Path

# Charger le fichier txt contenant les entrées
parts_file_txt = Path(__file__).parent / "dict.txt"

# Dict des possibilités
parts_dict = {}
with open(parts_file_txt) as entries:
    clean_entries = [line.strip() for line in entries if line.strip()]
    for cle, line in enumerate(clean_entries, start=1):
        parts_dict[cle] = line

# Variables
dict_range = len(parts_dict) ** 2
info_how_many = f"Généré depuis {dict_range} possibilités"

# Fonctions

def clean_file():
    parts_file_txt.write_text("\n".join(parts_dict.values()))

def get_dict_part():
    part = parts_dict[random.randint(1, len(parts_dict))].capitalize()
    return part

def add_dict(new_word_input):
    # On réécrit le fichier entièrement à partir de parts_dict (déjà nettoyé en mémoire)
    # plutôt que de manipuler le texte brut du fichier : ça évite toute dépendance
    # à l'état exact du fichier sur disque (ligne finale en trop ou en moins,
    # espaces parasites, etc.), peu importe comment il a été édité entre-temps.
    new_word = new_word_input.lower()
    if new_word in parts_dict.values():
        click.echo(click.style("'" + new_word + "'" + " existe déjà et n'a pas été ajouté", fg="red"))
    else:
        parts_dict.update({len(parts_dict)+1: new_word})
        parts_file_txt.write_text("\n".join(parts_dict.values()))
        click.echo(click.style("'" + new_word + "'" + " ajouté !", fg="green"))

def del_dict(del_word_input):
    del_word = del_word_input.lower()
    if del_word in parts_dict.values():
        del_key = [key for key, value in parts_dict.items() if value == del_word]
        for key in del_key: # On utilise une boucle au cas où il y aurait quand même un doublon dans le dictionnaire
            parts_dict.pop(key)
        parts_file_txt.write_text("\n".join(parts_dict.values()))
        click.echo(click.style("'" + del_word + "'" + " supprimé !", fg="green"))
    else:
        click.echo(click.style("'" + del_word + "'" + " n'existe pas", fg="red"))

@click.command(epilog="Exemple : toolkit namegen -cn 8 -s _")
@click.option('-n', type=click.IntRange(1), default=3, help=": Nombre de propositions à générer (par défaut 3)")
@click.option('-s', default="", help=": Séparateur (par défaut aucun)")
@click.option('-c', is_flag=True, help=": Ajouter un nombre à la fin")
@click.option('-a', type=click.STRING, help=": Ajouter un mot au dictionnaire")
@click.option('-d', type=click.STRING, help=": Supprimer un mot du dictionnaire")
def start(n, s, c, a, d):
    """Génère des noms aléatoires."""
    clean_file()
    resultats = []
    for _ in range(n):
        if not c:
            username = get_dict_part() + s + get_dict_part()
        else:
            username = get_dict_part() + s + get_dict_part() + s + str(random.randint(111, 999))
        resultats.append(username)
    print(" / ".join(resultats))
    if a:
        add_dict(a)
    if d:
        del_dict(d)
    if dict_range >= n:
        click.echo(click.style(info_how_many, fg="yellow"))
    else:
        click.echo(click.style(info_how_many + " (attention aux doublons)", fg="red"))

# Programme

if __name__ == "__main__":
    start()