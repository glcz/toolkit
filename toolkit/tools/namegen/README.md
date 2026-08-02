# Namegen

Génère des noms d'utilisateur aléatoires en combinant deux mots piochés dans un dictionnaire.

## Utilisation

```bash
python cli.py namegen [OPTIONS]
```

Ou de manière autonome, sans passer par le toolkit :

```bash
python main.py [OPTIONS]
```

## Options

| Option | Description | Défaut |
|---|---|---|
| `-n` | Nombre de propositions à générer | `3` |
| `-s` | Séparateur entre les deux mots | aucun |
| `-c` | Ajoute un nombre à 3 chiffres à la fin de chaque nom | désactivé |

## Exemples

```bash
# 3 noms par défaut
python cli.py namegen

# 5 noms séparés par un underscore
python cli.py namegen -n 5 -s _

# Noms avec suffixe numérique, séparateur inclus
python cli.py namegen -cn 8 -s _
```

## Personnaliser le dictionnaire

Les mots utilisés viennent de [`dict.txt`](dict.txt), un mot par ligne. Pour changer les possibilités de génération, il suffit d'éditer ce fichier — aucune modification de code n'est nécessaire.

Le nombre de combinaisons possibles affiché après chaque génération (`amplitude`) est calculé automatiquement à partir du nombre de mots présents dans le fichier.

## Todo

- [x] Pouvoir ajouter une entrée au dictionnaire depuis la commande
- [x] Pouvoir supprimer une entrée au dictionnaire depuis la commande
- [x] Gérer les lignes vides ou les doublons de mots dans `dict.txt`
- [ ] Une vraie estimation du risque de doublon (type paradoxe des anniversaires) plutôt que la comparaison actuelle
- [x] Empêcher `-n` négatif ou non numérique