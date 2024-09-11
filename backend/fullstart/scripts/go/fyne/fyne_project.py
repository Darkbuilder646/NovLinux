import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr.decode()}")
        
def create_fyne_project(project_name, project_path):
    # Crée le chemin complet du projet
    full_path = os.path.join(project_path, project_name)

    # Crée un nouveau répertoire pour le projet
    os.makedirs(full_path, exist_ok=True)

    # Change le répertoire de travail actuel vers le répertoire du projet
    os.chdir(full_path)

    # Initialise un nouveau module Go
    run_command(f"go mod init {project_name}")

    # Ajoute Fyne comme une dépendance du module
    run_command("go get fyne.io/fyne/v2")

    # Crée un nouveau fichier main.go avec un exemple de code Fyne
    with open("main.go", "w") as f:
        f.write("""
package main

import (
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/widget"
)

func main() {
    a := app.New()
    w := a.NewWindow("Hello")

    w.SetContent(widget.NewLabel("Hello Fyne!"))
    w.ShowAndRun()
}
""")

# Exemple d'utilisation
project_name = input("Enter the name of the Fyne project you want to create: ")
project_path = input("Enter the path where you want to create the project: ")
create_fyne_project(project_name, project_path)