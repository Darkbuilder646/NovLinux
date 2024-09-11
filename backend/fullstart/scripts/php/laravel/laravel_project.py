import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def setup_laravel_project(project_name, path):
    # Change le répertoire de travail actuel vers le chemin spécifié
    os.chdir(path)

    # Crée un nouveau projet Laravel
    run_command(f"composer create-project --prefer-dist laravel/laravel {project_name}")

# Exemple d'utilisation
project_name = input("Enter the name of the Laravel project you want to create: ")
path = input("Enter the path where you want to create the project: ")
setup_laravel_project(project_name, path)