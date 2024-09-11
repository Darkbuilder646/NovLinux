from .base_framework import BaseFramework
import os
import re
import json
import subprocess

def is_valid_project_name(name):
    return re.match(r'^[a-zA-Z0-9_-]+$', name) is not None

def clean_project_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '-', name)

class ExpressFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("sudo xbps-install -Sy")

        # Installe Node.js et npm
        self.execute_command("sudo xbps-install -y nodejs")

        # Vérifie l'installation de Node.js et npm
        node_version, node_error = self.execute_command("node -v")
        npm_version, npm_error = self.execute_command("npm -v")

        if node_error or npm_error:
            return f"Error installing Node.js or npm: {node_error} {npm_error}", ""

        # Installe Express Generator
        express_install, express_error = self.execute_command("npm install -g express-generator")

        if express_error:
            return f"Error installing Express Generator: {express_error}", ""

        return "Express and dependencies installed.", ""

    def run_project(self):
        project_name = "my-express-app"
        self._create_express_project(project_name)
        command = f"cd {project_name} && npm start"
        return self.execute_command(command)

    def _create_express_project(self, project_name):
        path = os.getcwd()
        self._setup_express_project(project_name, path)

    def _create_express_project_details(self, project_path):
        try:
            # Utiliser express-generator pour créer un nouveau projet Express avec le moteur de vue pug
            command = f"npx express-generator {project_path} --view=pug"
            stdout, stderr = self.execute_command(command)
            if stderr:
                return False, stderr
            
            return True, "Express project created successfully."
        except Exception as e:
            return False, str(e)

    def run_project_details(self, project_name, project_path):
        # Construire le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Vérifier si le répertoire existe, sinon le créer
        if not os.path.exists(full_project_path):
            print(f"Le répertoire {full_project_path} n'existe pas. Création en cours...")
            os.makedirs(full_project_path, exist_ok=True)
        
        # Appeler _create_express_project_details pour configurer le projet Express
        create_status, create_message = self._create_express_project_details(full_project_path)
        if not create_status:
            print(f"Erreur lors de la création des détails du projet Express: {create_message}")
            return None, create_message
        
        # Mettre à jour package.json
        package_json_path = os.path.join(full_project_path, 'package.json')
        with open(package_json_path, 'r+') as file:
            package_data = json.load(file)
            package_data['dependencies']['core-js'] = '^3.23.3'
            package_data['dependencies']['express'] = '^4.19.2'
            package_data['dependencies']['pug'] = '^3.0.3'
            file.seek(0)
            json.dump(package_data, file, indent=2)
            file.truncate()
        
        # Définir la commande pour démarrer le serveur de développement Express
        command = f"cd {full_project_path} && npm install && npm audit fix --force && npm start"
        
        # Exécuter la commande pour démarrer le serveur de développement
        stdout, stderr = self.execute_command(command)
        if stderr:
            print(f"Erreur lors du démarrage du serveur de développement Express: {stderr}")
            return stdout, stderr
        else:
            print(f"Serveur de développement Express démarré avec succès pour {project_name}. Accédez à http://localhost:3000")
            return stdout, None

    def _setup_express_project(self, project_name, path):
        os.chdir(path)
        project_name = project_name.lower()
        command = f"express {project_name}"
        self.execute_command(command)
        os.chdir(project_name)
        self.execute_command("npm install")
        os.chdir("..")

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return "", str(e)

class NativeJSFramework(BaseFramework):
    def install_dependencies(self):
        # Installe Node.js et npm
        self.execute_command("sudo xbps-install -y nodejs")

        # Vérifie l'installation de Node.js et npm
        node_version, node_error = self.execute_command("node -v")
        npm_version, npm_error = self.execute_command("npm -v")

        if node_error or npm_error:
            print("Erreur lors de l'installation de Node.js ou npm")
        else:
            print(f"Node.js version: {node_version.strip()}")
            print(f"npm version: {npm_version.strip()}")

    def setup_project(self):
        # Crée un fichier package.json s'il n'existe pas
        if not os.path.exists('package.json'):
            self.execute_command("npm init -y")

        # Initialiser un dépôt Git
        if not os.path.exists('.git'):
            self.execute_command("git init")

    def _create_nativejs_project_details(self, project_path):
        try:
            # Créer un répertoire pour le projet
            os.makedirs(project_path, exist_ok=True)
            
            # Créer un fichier package.json minimal
            package_json_content = '''{
                "name": "my-nativejs-app",
                "version": "1.0.0",
                "main": "app.js",
                "scripts": {
                    "start": "node app.js"
                }
            }'''
            with open(os.path.join(project_path, 'package.json'), 'w') as f:
                f.write(package_json_content)
            
            # Créer un fichier app.js minimal
            app_js_content = '''console.log("Hello, NativeJS!");'''
            with open(os.path.join(project_path, 'app.js'), 'w') as f:
                f.write(app_js_content)
            
            return True, "NativeJS project created successfully."
        except Exception as e:
            return False, str(e)

    def run_project_details(self, project_name, project_path):
        # Construire le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Vérifier si le répertoire existe, sinon le créer
        if not os.path.exists(full_project_path):
            print(f"Le répertoire {full_project_path} n'existe pas. Création en cours...")
            os.makedirs(full_project_path, exist_ok=True)
        
        # Appeler _create_nativejs_project_details pour configurer le projet NativeJS
        create_status, create_message = self._create_nativejs_project_details(full_project_path)
        if not create_status:
            print(f"Erreur lors de la création des détails du projet NativeJS: {create_message}")
            return None, create_message
        
        # Définir la commande pour démarrer le serveur de développement NativeJS
        command = f"cd {full_project_path} && node app.js"
        
        # Exécuter la commande pour démarrer le serveur de développement
        stdout, stderr = self.execute_command(command)
        if stderr:
            print(f"Erreur lors du démarrage du serveur de développement NativeJS: {stderr}")
            return stdout, stderr
        else:
            print(f"Serveur de développement NativeJS démarré avec succès pour {project_name}.")
            return stdout, None

    def _setup_nativejs_project(self, project_name, path):
        os.chdir(path)
        project_path = os.path.join(path, project_name)
        self._create_nativejs_project_details(project_path)
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')


class ReactFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("sudo xbps-install -Sy")

        # Installe Node.js et npm
        self.execute_command("sudo xbps-install -y nodejs")

        self.execute_command("sudo npm install -g create-react-app")

        # Vérifie l'installation de Node.js et npm
        node_version, node_error = self.execute_command("node -v")
        npm_version, npm_error = self.execute_command("npm -v")

        if node_error or npm_error:
            return f"Error installing Node.js or npm: {node_error} {npm_error}", ""

        return "Node.js, npm and dependencies installed.", ""


    def run_project_details(self, project_name, project_path):
        # Construire le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        self.execute_command(f"create-react-app {full_project_path}")
        instructions= 'Dont forget to run "npm isntall" and "npm run dev" at the root of your project.'
        return instructions, ""

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return "", str(e)


class VueJSFramework:
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("sudo xbps-install -Sy")

        # Installe Node.js et npm
        self.execute_command("sudo xbps-install -y nodejs npm")
        self.execute_command("sudo npm install -g create-vue")

        return "Node.js and npm installed successfully.", ""

    def run_project_details(self, project_name, project_path):
        print(f"Creating Vue.js project: {project_name}")
        self._create_vue_project(project_name, project_path)
        instructions = "Don't forget to run 'npm install' followed by 'npm run dev' at the root of your project."
        return instructions, ""

    def _create_vue_project(self, project_name, project_path):

        if not os.path.exists(project_path):
            os.makedirs(project_path)
            print(f"Le répertoire {project_path} a été créé.")
        else:
            print(f"Le répertoire {project_path} existe déjà.")

        os.chdir(project_path)
        print(f"Répertoire de travail actuel: {os.getcwd()}")

        command = f"create-vue {project_name} --default"
        print("commande en cours")
        
        try:
            print(f"Exécution de la commande: {command}")
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            # Décodage et affichage des sorties
            if process.returncode == 0:
                print(f"Le projet Vue.js a été créé avec succès dans {project_path}.")
                print("Output:", stdout)
            else:
                print(f"Erreur lors de la création du projet Vue.js.")
                print("Error:", stderr)
        
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création du projet Vue.js: {e}")


    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
