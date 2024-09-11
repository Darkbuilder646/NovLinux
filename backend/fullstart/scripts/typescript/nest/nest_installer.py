import subprocess

def install_nest():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe Node.js et npm
    subprocess.run(["xbps-install", "-y", "nodejs"])

    # Vérifie l'installation de Node.js et npm
    subprocess.run(["node", "-v"])
    subprocess.run(["npm", "-v"])

    # Installe Nest CLI
    subprocess.run(["npm", "install", "-g", "@nestjs/cli@10.3.2"])

# Appelle la fonction pour installer Nest
install_nest()