import subprocess
import os

def install_symfony():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe Composer
    subprocess.run(["xbps-install", "-y", "composer"])

    # Installe Symfony CLI
    result = subprocess.run("curl -sS https://get.symfony.com/cli/installer | bash", shell=True)
    if result.returncode != 0:
        print("Erreur lors de l'installation de Symfony CLI.")
        return

    # Déplace le binaire Symfony dans le répertoire /usr/local/bin/
    subprocess.run(["mv", "/root/.symfony5/bin/symfony", "/usr/local/bin/symfony"])

    print("Symfony CLI installed successfully. Please run 'source ~/.bashrc' or restart your shell to update your PATH.")

# Appelle la fonction pour installer Symfony
install_symfony()