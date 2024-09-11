import subprocess

def install_nodejs_npm():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe Node.js et npm
    subprocess.run(["xbps-install", "-y", "nodejs"])

    # Vérifie l'installation de Node.js et npm
    subprocess.run(["node", "-v"])
    subprocess.run(["npm", "-v"])

# Appelle la fonction pour installer Node.js et npm
install_nodejs_npm()