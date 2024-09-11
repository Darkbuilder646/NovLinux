import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr.decode()}")

def create_rocket_project(project_name, project_path):
    # Crée le chemin complet du projet
    full_path = os.path.join(project_path, project_name)

    # Crée un nouveau répertoire pour le projet
    os.makedirs(full_path, exist_ok=True)

    # Change le répertoire de travail actuel vers le répertoire du projet
    os.chdir(full_path)

    # Initialise un nouveau projet Rust
    run_command("cargo init")

    # Ajoute Rocket comme une dépendance dans le fichier Cargo.toml
    with open("Cargo.toml", "a") as f:
        f.write("""
[dependencies]
rocket = "0.4.10"
""")

# Exemple d'utilisation
project_name = input("Enter the name of the Rocket project you want to create: ")
project_path = input("Enter the path where you want to create the project: ")
create_rocket_project(project_name, project_path)