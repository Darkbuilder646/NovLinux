import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def setup_js_project(project_name, path):
    # Change le répertoire de travail actuel vers le chemin spécifié
    os.chdir(path)

    # Crée le répertoire du projet
    os.makedirs(project_name, exist_ok=True)

    # Change le répertoire de travail actuel vers le répertoire du projet
    os.chdir(project_name)

    # Crée les fichiers de base du projet
    with open('index.html', 'w') as f:
        f.write("""
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <script src="main.js"></script>
</body>
</html>
        """)

    with open('main.js', 'w') as f:
        f.write("// Your JavaScript code here\n")

# Exemple d'utilisation
project_name = input("Enter the name of the JavaScript project you want to create: ")
path = input("Enter the path where you want to create the project: ")
setup_js_project(project_name, path)