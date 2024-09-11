import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def create_gin_project(project_name, project_path):
    # Crée le chemin complet du projet
    full_path = os.path.join(project_path, project_name)

    # Crée un nouveau répertoire pour le projet
    os.makedirs(full_path, exist_ok=True)

    # Change le répertoire de travail actuel vers le répertoire du projet
    os.chdir(full_path)

    # Initialise un nouveau module Go
    run_command(f"go mod init {project_name}")

    # Ajoute Gin comme une dépendance du module
    run_command("go get github.com/gin-gonic/gin")

    # Crée un nouveau fichier main.go avec un exemple de code Gin
    with open("main.go", "w") as f:
        f.write("""
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // listen and serve on 0.0.0.0:8080
}
""")

# Exemple d'utilisation
project_name = input("Enter the name of the Gin project you want to create: ")
project_path = input("Enter the path where you want to create the project: ")
create_gin_project(project_name, project_path)