from PIL import Image
import os

# === PARAMÈTRES À MODIFIER ===
dossier_entree = "img_orig"
dossier_sortie = "img_cropped"
hauteur_a_cropper = 100  # en pixels

# Crée le dossier de sortie s'il n'existe pas
os.makedirs(dossier_sortie, exist_ok=True)

# Parcours des fichiers
for nom_fichier in os.listdir(dossier_entree):
    if nom_fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        chemin_image = os.path.join(dossier_entree, nom_fichier)
        with Image.open(chemin_image) as img:
            largeur, hauteur = img.size
            # Définir la zone à garder (tout sauf les X pixels du bas)
            zone_crop = (0, 0, largeur, hauteur - hauteur_a_cropper)
            image_croppee = img.crop(zone_crop)

            # Sauvegarde
            chemin_sortie = os.path.join(dossier_sortie, nom_fichier)
            image_croppee.save(chemin_sortie)

print("Recadrage terminé !")