from .base_framework import BaseFramework
import os
import subprocess

class AngularFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")
        self.execute_command("xbps-install -y nodejs")
        self.execute_command("xbps-install -S expect")
        
        # Vérifie l'installation de Node.js et npm
        node_version, node_error = self.execute_command("node -v")
        npm_version, npm_error = self.execute_command("npm -v")
        
        if node_error or npm_error:
            return f"Error installing Node.js or npm: {node_error} {npm_error}", ""
        
        # Installe Angular CLI
        angular_install, angular_error = self.execute_command("npm install -g @angular/cli")
        
        if angular_error:
            return f"Error installing Angular CLI: {angular_error}", ""
        
        return "Node.js, npm, Angular CLI and dependencies installed.", ""

    def run_project(self):
        project_name = "my-angular-app"
        self._create_angular_project(project_name)
        command = f"cd {project_name} && ng serve"
        return self.execute_command(command)

    def _create_angular_project(self, project_name):
        path = os.getcwd()
        self._setup_angular_project(project_name, path)

    def _setup_angular_project(self, project_name, path):
        os.chdir(path)
        self.execute_command(f"ng new {project_name}")
        os.chdir("..")

    def run_project_details(self, project_name, project_path):
        # Construire le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Vérifier si le répertoire existe, sinon le créer
        if not os.path.exists(full_project_path):
            print(f"Le répertoire {full_project_path} n'existe pas. Création en cours...")
            os.makedirs(full_project_path, exist_ok=True)
        
        # Appeler _create_angular_project_details pour configurer le projet Angular
        create_status, create_message = self._create_angular_project_details(project_name, project_path)
        if not create_status:
            print(f"Erreur lors de la création des détails du projet Angular: {create_message}")
            return None, create_message
        
        # Définir la commande pour démarrer le serveur de développement Angular
        command = f"cd {full_project_path} && ng serve"
        
        # Exécuter la commande pour démarrer le serveur de développement
        stdout, stderr = self.execute_command(command)
        if stderr:
            print(f"Erreur lors du démarrage du serveur de développement Angular: {stderr}")
            return stdout, stderr
        else:
            print(f"Serveur de développement Angular démarré avec succès pour {project_name}. Accédez à http://localhost:4200")
            return stdout, None

    def _create_angular_project_details(self, project_name, project_path):
        try:
            # Utiliser Angular CLI pour créer un nouveau projet Angular dans le répertoire parent
            command = f"cd {project_path} && ng new {project_name} --skip-install"
            stdout, stderr = self.execute_command(command)
            if stderr:
                return False, stderr
            
            # Installer les dépendances du projet Angular
            command = f"cd {project_path}/{project_name} && npm install"
            stdout, stderr = self.execute_command(command)
            if stderr:
                return False, stderr
            
            return True, "Angular project created and dependencies installed successfully."
        except Exception as e:
            return False, str(e)

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')


class NestJSFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")
        self.execute_command("xbps-install -y nodejs")
        
        # Vérifie l'installation de Node.js et npm
        node_version, node_error = self.execute_command("node -v")
        npm_version, npm_error = self.execute_command("npm -v")
        
        if node_error or npm_error:
            return f"Error installing Node.js or npm: {node_error} {npm_error}", ""
        
        # Installe Nest CLI
        nest_install, nest_error = self.execute_command("npm install -g @nestjs/cli@10.3.2")
        
        if nest_error:
            return f"Error installing Nest CLI: {nest_error}", ""
        
        return "Node.js, npm, Nest CLI and dependencies installed.", ""

    def run_project(self):
        project_name = "my-nestjs-app"
        self._create_nestjs_project(project_name)
        command = f"cd {project_name} && npm run start"
        return self.execute_command(command)

    def _create_nestjs_project(self, project_name):
        path = os.getcwd()
        self._setup_nestjs_project(project_name, path)

    def _setup_nestjs_project(self, project_name, path):
        os.chdir(path)
        project_name = project_name.lower()
        self.execute_command(f"npx @nestjs/cli new {project_name}")
        os.chdir("..")
    
    def run_project_details(self, project_name, project_path):
        # Construire le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Vérifier si le répertoire existe, sinon le créer
        if not os.path.exists(full_project_path):
            print(f"Le répertoire {full_project_path} n'existe pas. Création en cours...")
            os.makedirs(full_project_path, exist_ok=True)
        
        # Appeler _create_nestjs_project_details pour configurer le projet NestJS
        create_status, create_message = self._create_nestjs_project_details(project_name, project_path)
        if not create_status:
            print(f"Erreur lors de la création des détails du projet NestJS: {create_message}")
            return None, create_message
        
        # Définir la commande pour démarrer le serveur de développement NestJS
        command = f"cd {full_project_path} && npm run start"
        
        # Exécuter la commande pour démarrer le serveur de développement
        stdout, stderr = self.execute_command(command)
        if stderr:
            print(f"Erreur lors du démarrage du serveur de développement NestJS: {stderr}")
            return stdout, stderr
        else:
            print(f"Serveur de développement NestJS démarré avec succès pour {project_name}.")
            return stdout, None

    def _create_nestjs_project_details(self, project_name, project_path):
        try:
            # Utiliser le script expect pour créer un nouveau projet NestJS dans le répertoire parent
            print(f"Création du projet NestJS: {project_name}")
            script_path = os.path.join(os.path.dirname(__file__), 'create_nestjs_project.exp')
            command = f"expect {script_path} {project_path} {project_name}"
            stdout, stderr = self.execute_command(command)
            print(f"stdout: {stdout}")
            if stderr:
                return False, stderr
            
            # Installer les dépendances du projet NestJS
            command = f"cd {project_path}/{project_name} && npm install"
            stdout, stderr = self.execute_command(command)
            if stderr:
                return False, stderr
            
            return True, "NestJS project created and dependencies installed successfully."
        except Exception as e:
            return False, str(e)

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
