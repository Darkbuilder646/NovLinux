import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def setup_vue_project(project_name, path):
    # Change le répertoire de travail actuel vers le chemin spécifié
    os.chdir(path)

    # Convertit le nom du projet en minuscules
    project_name = project_name.lower()

    # Crée un nouveau projet Vue.js
    run_command(f"vue create {project_name}")

# Exemple d'utilisation
project_name = input("Enter the name of the Vue.js project you want to create: ")
path = input("Enter the path where you want to create the project: ")
setup_vue_project(project_name, path)