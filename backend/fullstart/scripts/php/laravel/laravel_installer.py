import subprocess
import os

def install_laravel():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe PHP et les extensions nécessaires
    subprocess.run(["xbps-install", "-y", "php", "php-fpm", "php-mbstring", "php-xml", "php-pdo", "php-zip", "php-gd", "php-curl"])

    # Installe Composer
    subprocess.run(["xbps-install", "-y", "composer"])

    # Installe Laravel Installer
    subprocess.run(["composer", "global", "require", "laravel/installer"])

    # Ajoute le répertoire bin de Composer au PATH dans le fichier de profil de l'utilisateur
    with open(os.path.expanduser("~/.bashrc"), "a") as f:
        f.write('export PATH="$HOME/.config/composer/vendor/bin:$PATH"\n')

    print("Laravel installed successfully. Please run 'source ~/.bashrc' or restart your shell to update your PATH.")

# Appelle la fonction pour installer Laravel
install_laravel()