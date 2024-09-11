from .base_framework import BaseFramework
import os
import subprocess

class RailsFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        print("Updating package list...")
        self.execute_command("xbps-install -Sy")

        # Installe Ruby
        self.execute_command("xbps-install -y ruby")

        # Installe Bundler et Rails
        self.execute_command("gem install bundler rails")

        return "Ruby, Bundler, and Rails installed.", ""

    def run_project_details(self, project_name, project_path):
        print(f"Creating Rails project: {project_name}")
        self._create_rails_project_details(project_name, project_path)
        instructions = "Don't forget to run 'rails server' at the root of your project."
        return instructions, ""

    def _create_rails_project(self, project_name):
        path = os.path.join(os.getcwd(), project_name)
        if not os.path.exists(path):
            print(f"Le répertoire {path} n'existe pas. Création en cours...")
            os.makedirs(path, exist_ok=True)
        self._setup_rails_project(project_name, path)
        print(f"Create Rails project: {project_name}")

    def _create_rails_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        if not os.path.exists(full_project_path):
            os.makedirs(full_project_path)

        # Ajoute le chemin des gemmes Ruby à la variable d'environnement PATH
        gem_path = subprocess.check_output("gem environment gemdir", shell=True).decode('utf-8').strip()
        ruby_bin_path = os.path.join(gem_path, 'bin')
        os.environ['PATH'] += os.pathsep + ruby_bin_path

        command = f"rails new {project_name}"
        
        try:
            subprocess.check_call(command, shell=True, cwd=project_path)
            print(f"Le projet Rails {project_name} a été créé avec succès dans {project_path}.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création du projet Rails: {e}")

    def _setup_rails_project(self, project_name, path):
        os.chdir(path)
        command = f"rails new {project_name}"
        self.execute_command(command)
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

class SinatraFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("xbps-install -Sy")

        # Installe Ruby
        self.execute_command("xbps-install -y ruby")

        # Installe Sinatra
        self.execute_command("gem install sinatra")

        return "Ruby and Sinatra installed.", ""

    def run_project(self):
        project_name = "my-sinatra-app"
        self._create_sinatra_project(project_name)
        # Pour Sinatra, le serveur est lancé via un fichier Ruby spécifique
        command = f"cd {project_name} && ruby app.rb"
        return self.execute_command(command)
    
    def run_project_details(self, project_name, project_path):
        print(f"Creating Sinatra project: {project_name}")
        self._create_sinatra_project_details(project_name, project_path)
        instructions = "Don't forget to run 'ruby app.rb' at the root of your project."
        return instructions, ""
    
    def _create_sinatra_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        if not os.path.exists(full_project_path):
            os.makedirs(full_project_path)

        os.chdir(full_project_path)
        with open('app.rb', 'w') as f:
            f.write("""require 'sinatra'
get '/' do
  'Hello, Sinatra!'
end
""")
        print(f"Le projet Sinatra {project_name} a été créé avec succès dans {full_project_path}.")

    def _create_sinatra_project(self, project_name):
        path = os.getcwd()
        self._setup_sinatra_project(project_name, path)

    def _setup_sinatra_project(self, project_name, path):
        os.chdir(path)
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)
        with open('app.rb', 'w') as f:
            f.write("""require 'sinatra'
get '/' do
  'Hello world!'
end""")
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')