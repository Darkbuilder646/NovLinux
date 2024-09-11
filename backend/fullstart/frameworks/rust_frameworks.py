from .base_framework import BaseFramework
import os
import subprocess

class RocketFramework(BaseFramework):
    def install_dependencies(self):
        # Définit la variable d'environnement pour ignorer les vérifications de chemin
        os.environ["RUSTUP_INIT_SKIP_PATH_CHECK"] = "yes"
        
        # Télécharge et installe rustup
        stdout, stderr = self.execute_command("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y")
        if "error" in stderr.lower():
            print(f"Erreur lors de l'installation de rustup: {stderr}")
            return "Erreur lors de l'installation de rustup.", stderr
        else:
            print("rustup a été installé avec succès.")
        
        # Ajoute rustup au PATH
        os.environ["PATH"] += os.pathsep + os.path.expanduser("~/.cargo/bin")
        
        # Utilise rustup pour installer Rust et cargo
        stdout, stderr = self.execute_command("rustup default stable")
        if "error" in stderr.lower():
            print(f"Erreur lors de l'installation de Rust via rustup: {stderr}")
            return "Erreur lors de l'installation de Rust via rustup.", stderr
        else:
            print("Rust et cargo ont été installés avec succès via rustup.")
        
        return "Rust et ses dépendances ont été installés avec succès.", ""

    def run_project_details(self, project_name, project_path):
        print(f"Creating Rocket project: {project_name}")
        stdout, stderr = self._create_rocket_project_details(project_name, project_path)
        if stderr:
            print(f"Erreur lors de la création du projet Rocket: {stderr}")
            return f"Erreur lors de la création du projet Rocket: {stderr}", stderr
        else:
            print(f"Projet Rocket '{project_name}' créé avec succès.")
        
        instructions = f"Don't forget to run 'cargo run' at the root of your project."
        return instructions, ""

    def _create_rocket_project_details(self, project_name, project_path):
        parent_path = os.path.abspath(project_path)
        full_project_path = os.path.join(parent_path, project_name)

        # Crée le répertoire parent s'il n'existe pas
        os.makedirs(parent_path, exist_ok=True)

        # Change le répertoire courant pour le répertoire parent
        os.chdir(parent_path)

        # Utilise cargo pour créer le projet
        command = f"cargo new {project_name} --bin"
        
        try:
            stdout, stderr = self.execute_command(command)
            if "error" in stderr.lower():
                print(f"Erreur lors de la création du projet Rocket: {stderr}")
                return stdout, stderr
            else:
                print(f"Le projet Rocket '{project_name}' a été créé avec succès dans {full_project_path}.")
                return stdout, ""
        except Exception as e:
            print(f"Une exception s'est produite: {e}")
            return "", str(e)

    def _setup_rocket_project(self, project_name, path):
        full_path = os.path.join(path, project_name)
        os.makedirs(full_path, exist_ok=True)
        os.chdir(full_path)
        self.execute_command("cargo init")
        with open("Cargo.toml", "a") as f:
            f.write("""
[dependencies]
rocket = "0.4.10"
""")
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
    
    


class TauriFramework(BaseFramework):
    def install_dependencies(self):
        # Installer Node.js, Yarn, Rust
        self.execute_command("xbps-install -Sy nodejs yarn")
        self.execute_command("xbps-install -Sy rust")
        
        return "Node.js, Yarn, Rust, pip, pexpect and dependencies installed.", ""


    def run_project(self):
        project_name = "my-tauri-app"
        self._create_tauri_project(project_name)
        command = f"cd {project_name} && yarn tauri dev"
        return self.execute_command(command)
    
    def run_project_details(self, project_name, project_path):
        print(f"Creating Tauri project: {project_name}")
        stdout, stderr = self._create_tauri_project_details(project_name, project_path)
        if stderr:
            print(f"Erreur lors de la création du projet Tauri: {stderr}")
            return f"Erreur lors de la création du projet Tauri: {stderr}", stderr
        else:
            print(f"Projet Tauri '{project_name}' créé avec succès.")
        
        instructions = f"Don't forget to run 'cd {project_name} && yarn tauri dev' at the root of your project."
        return instructions, ""

    def _create_tauri_project(self, project_name):
        path = os.getcwd()
        self._setup_tauri_project(project_name, path)


    def _create_tauri_project_details(self, project_name, project_path):
        parent_path = os.path.abspath(project_path)
        full_project_path = os.path.join(parent_path, project_name)

        print(f"Chemin du projet parent: {parent_path}")
        print(f"Chemin complet du projet: {full_project_path}")

        # Crée le répertoire parent s'il n'existe pas
        os.makedirs(parent_path, exist_ok=True)
        print(f"Répertoire parent créé ou déjà existant: {parent_path}")

        # Change le répertoire courant pour le répertoire parent
        os.chdir(parent_path)
        print(f"Répertoire courant changé pour: {parent_path}")

        # Utilise le script expect pour créer le projet Tauri
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'create_tauri_project.exp')
            command = f"expect {script_path} {parent_path} {project_name}"
            stdout, stderr = self.execute_command(command)
            print(f"stdout: {stdout}")
            if stderr:
                print(f"Erreur lors de la création du projet Tauri: {stderr}")
            else:
                print(f"Le projet Tauri '{project_name}' a été créé avec succès dans {full_project_path}.")
        except Exception as e:
            print(f"Une exception s'est produite: {e}")
    
    def _setup_tauri_project(self, project_name, path):
        full_path = os.path.join(path, project_name)
        os.makedirs(full_path, exist_ok=True)
        os.chdir(full_path)
        self.execute_command("yarn init -y")
        self.execute_command("npx create-tauri-app .")
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
