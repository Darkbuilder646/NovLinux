import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def setup_php_project(project_name, path):
    # Change le répertoire de travail actuel vers le chemin spécifié
    os.chdir(path)

    # Crée le répertoire du projet
    os.makedirs(project_name, exist_ok=True)

    # Change le répertoire de travail actuel vers le répertoire du projet
    os.chdir(project_name)

    # Crée les fichiers de base du projet
    with open('index.php', 'w') as f:
        f.write("<?php\n\n// Your code here\n")

# Exemple d'utilisation
project_name = input("Enter the name of the PHP project you want to create: ")
path = input("Enter the path where you want to create the project: ")
setup_php_project(project_name, path)