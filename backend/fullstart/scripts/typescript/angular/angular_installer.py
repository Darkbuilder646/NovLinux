import subprocess

def install_angular():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe Node.js et npm
    subprocess.run(["xbps-install", "-y", "nodejs"])

    # Vérifie l'installation de Node.js et npm
    subprocess.run(["node", "-v"])
    subprocess.run(["npm", "-v"])

    # Installe Angular CLI
    subprocess.run(["npm", "install", "-g", "@angular/cli"])

# Appelle la fonction pour installer Angular
install_angular()