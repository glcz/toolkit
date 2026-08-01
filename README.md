# Toolkit

Une collection de petits utilitaires Python, réunis sous un seul point d'entrée en ligne de commande.

L'idée : plutôt que d'avoir dix scripts éparpillés qu'il faut retrouver et lancer un par un, chaque outil vit dans son propre dossier et devient automatiquement accessible via `toolkit <nom_outil>`.

## Outils disponibles

| Outil | Description |
|---|---|
| [`namegen`](toolkit/tools/namegen/README.md) | Génère des noms d'utilisateur aléatoires en combinant des mots issus d'un dictionnaire éditable |

D'autres outils sont en cours de refonte et rejoindront la liste au fur et à mesure.

## Prérequis

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances

## Installation

```bash
git clone https://github.com/glcz/toolkit.git
cd toolkit
uv sync
```

## Utilisation

Depuis `toolkit/tools/` :

```bash
python cli.py <nom_outil> [options]
```

Par exemple :

```bash
python cli.py namegen -n 5
```

Pour voir la liste des outils disponibles et l'aide générale :

```bash
python cli.py --help
```

Chaque outil expose aussi sa propre aide :

```bash
python cli.py namegen --help
```

## Comment ça marche

`cli.py` scanne automatiquement les sous-dossiers de `toolkit/tools/` à la recherche d'un fichier `main.py`. Si un dossier en contient un, son outil est enregistré comme sous-commande du CLI.

**Concrètement, ajouter un nouvel outil ne nécessite jamais de modifier `cli.py`.** Il suffit de :

1. Créer un dossier dans `toolkit/tools/`
2. Y placer un `main.py` qui expose une fonction `start` décorée avec `@click.command()`
3. C'est tout — l'outil apparaît automatiquement au prochain lancement

Chaque outil reste par ailleurs utilisable indépendamment, en le lançant directement (`python toolkit/tools/namegen/main.py`).

## Structure du projet

```
toolkit/
├── toolkit/
│   ├── __init__.py
│   ├── __main__.py
│   └── tools/
│       ├── cli.py          # Point d'entrée, découverte et routage des outils
│       └── <outil>/
│           ├── __init__.py
│           ├── main.py     # Logique de l'outil + commande Click
│           └── README.md   # Doc spécifique à l'outil
├── pyproject.toml
└── README.md
```

## Todo

- [ ] Tirer au clair `__init__.py` et `__main__.py`
- [ ] Transformer le projet en vrai paquet installable (`project.scripts`, commande `toolkit` accessible globalement)
- [ ] Ajouter un dossier de code partagé entre outils
- [ ] Ajouter des tests