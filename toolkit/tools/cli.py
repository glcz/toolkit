from pathlib import Path
import click
import importlib

tools = []

# Découvrir les modules automatiquement et les ajouter à la liste
p = Path.cwd()
for entry in p.iterdir():
    mainpy = entry / "main.py"
    if mainpy.exists():
        tools.append(entry.name)

@click.group()
def toolkit():
    """Une collection de petits outils.""" # S'affiche dans --help

for tool in tools:
    #@toolkit.command(tool)
    #def decouverte(tool_name=tool): # Important de passer la valeur de tool à tool_name sinon la boucle redéfinit tool à chaque passe
        module_path = tool + ".main" # On construit la chaine du module à importer (par exemple namegen.main)
        module = importlib.import_module(module_path) # Import du module
        toolkit.add_command(module.start, name=tool)

if __name__ == "__main__":
    toolkit()