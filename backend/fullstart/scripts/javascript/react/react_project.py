import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def setup_react_project(project_name, path):
    # Change le répertoire de travail actuel vers le chemin spécifié
    os.chdir(path)

    # Convertit le nom du projet en minuscules
    project_name = project_name.lower()

    # Crée un nouveau projet React avec Vite
    run_command(f"npx create-vite {project_name} --template react")

# Exemple d'utilisation
project_name = input("Enter the name of the React project you want to create: ")
path = input("Enter the path where you want to create the project: ")
setup_react_project(project_name, path)