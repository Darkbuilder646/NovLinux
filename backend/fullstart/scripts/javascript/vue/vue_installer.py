import subprocess

def install_vue():
    # Met à jour la liste des paquets
    subprocess.run(["xbps-install", "-Sy"])

    # Installe Node.js et npm
    subprocess.run(["xbps-install", "-y", "nodejs"])

    # Vérifie l'installation de Node.js et npm
    subprocess.run(["node", "-v"])
    subprocess.run(["npm", "-v"])

    # Installe Vue CLI
    subprocess.run(["npm", "install", "-g", "@vue/cli"])

# Appelle la fonction pour installer Vue
install_vue()