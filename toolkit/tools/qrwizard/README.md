# QRWizard

Génère un QR code à partir d'un texte, l'affiche directement dans le terminal, et l'enregistre en PNG dans le dossier Images de l'utilisateur.

## Utilisation

```bash
python cli.py qrwizard "texte à encoder" [OPTIONS]
```

Ou de manière autonome, sans passer par le toolkit :

```bash
python main.py "texte à encoder" [OPTIONS]
```

## Options

| Option | Description | Défaut |
|---|---|---|
| `-c` | Couleur du QR code | `black` |
| `-b` | Couleur de fond | `white` |

## Exemples

```bash
# QR code par défaut
python cli.py qrwizard "https://example.com"

# QR code bleu sur fond jaune
python cli.py qrwizard "https://example.com" -c blue -b yellow
```

## Où l'image est enregistrée

Le fichier `.png` est automatiquement placé dans le dossier Images de l'utilisateur (détecté via `platformdirs`, donc correct sur Linux, Windows et macOS, y compris avec des noms de dossiers traduits). Le nom du fichier correspond au texte encodé.

## Todo

- [ ] Gérer le cas où un fichier du même nom existe déjà (écrasement silencieux actuellement)
- [ ] Gérer le cas d'un texte vide ou invalide
- [ ] Compléter l'exemple dans l'epilog de la commande
- [ ] Isoler la création de l'objet `QRCode` à l'intérieur de `start()` (actuellement au niveau module, ce qui pourrait accumuler des données en cas d'appels multiples dans un même processus)
