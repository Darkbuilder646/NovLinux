from .base_framework import BaseFramework
import os
import subprocess

class CatalystFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("xbps-install -Sy")

        # Installe Perl
        self.execute_command("xbps-install -y perl")

        # Installe cpanminus
        self.execute_command("xbps-install -y cpanminus")

        # Installe make
        self.execute_command("xbps-install -y make")

        # Installe le module File::ShareDir::Install
        stdout, stderr = self.execute_command("cpanm File::ShareDir::Install")
        if stderr:
            print(f"Erreur lors de l'installation de File::ShareDir::Install: {stderr}")
        else:
            print("File::ShareDir::Install installé avec succès.")

        # Installe Catalyst::Devel
        stdout, stderr = self.execute_command("cpanm Catalyst::Devel")
        if stderr:
            print(f"Erreur lors de l'installation de Catalyst::Devel: {stderr}")
            # Affiche les logs d'erreur détaillés
            try:
                with open('/root/.cpanm/work/1724165478.3637/build.log', 'r') as log_file:
                    print(log_file.read())
            except FileNotFoundError:
                print("Log file not found. Please check the path.")
        else:
            print("Catalyst::Devel installé avec succès.")

        # Vérifie si catalyst.pl est installé et ajoute son chemin au PATH
        stdout, stderr = self.execute_command("find / -name catalyst.pl 2>/dev/null")
        if stdout:
            catalyst_path = stdout.strip()
            print(f"catalyst.pl trouvé à: {catalyst_path}")
            self.execute_command(f"export PATH=$PATH:$(dirname {catalyst_path})")
        else:
            print("catalyst.pl n'a pas été trouvé. Veuillez vérifier l'installation de Catalyst::Devel.")

        return "Perl, cpanminus, make, and Catalyst installed.", ""
    
    def run_project(self):
        project_name = "my-catalyst-app"
        self._create_catalyst_project(project_name)
        # Pour Catalyst, le serveur de développement est lancé via catalyst.pl
        command = f"cd {project_name} && perl script/my_catalyst_app_server.pl -r"
        return self.execute_command(command)

    def _create_catalyst_project(self, project_name):
        path = os.getcwd()
        self._setup_catalyst_project(project_name, path)

    def run_project_details(self, project_name, project_path):
        print(f"Creating Catalyst project: {project_name}")
        self._create_catalyst_project_details(project_name, project_path)
        instructions = f"Don't forget to run 'perl script/{project_name}_server.pl -r' at the root of your project."
        return instructions, ""

    def _create_catalyst_project_details(self, project_name, project_path):
        # Détermine le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Crée le répertoire parent si nécessaire
        parent_path = os.path.dirname(full_project_path)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)

        # Change le répertoire courant pour le répertoire parent
        os.chdir(parent_path)

        # Utilise le chemin complet vers catalyst.pl
        catalyst_pl_path = "/usr/bin/catalyst.pl"  # Remplacez par le chemin correct si nécessaire
        command = f"{catalyst_pl_path} {project_name}"
        
        try:
            stdout, stderr = self.execute_command(command)
            if stderr:
                print(f"Erreur lors de la création du projet Catalyst: {stderr}")
            else:
                print(f"Le projet Catalyst {project_name} a été créé avec succès dans {full_project_path}.")
        except Exception as e:
            print(f"Une exception s'est produite: {e}")

    def _setup_catalyst_project(self, project_name, path):
        os.chdir(path)
        command = f"catalyst.pl {project_name}"
        self.execute_command(command)
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

class Dancer2Framework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("xbps-install -Sy")

        # Installe Perl
        self.execute_command("xbps-install -y perl")

        # Installe cpanminus
        self.execute_command("xbps-install -y cpanminus")

        # Installe Dancer2
        self.execute_command("cpanm Dancer2")

        return "Perl, cpanminus, and Dancer2 installed.", ""

    def run_project(self):
        project_name = "my-dancer2-app"
        self._create_dancer2_project(project_name)
        # Pour Dancer2, le serveur est lancé via plackup
        command = f"cd {project_name} && plackup bin/app.psgi"
        return self.execute_command(command)
    
    def run_project_details(self, project_name, project_path):
        print(f"Creating Dancer2 project: {project_name}")
        self._create_dancer2_project_details(project_name, project_path)
        instructions = f"Don't forget to run 'plackup bin/app.psgi' at the root of your project."
        return instructions, ""

    def _create_dancer2_project(self, project_name):
        path = os.getcwd()
        self._setup_dancer2_project(project_name, path)

    def _create_dancer2_project_details(self, project_name, project_path):
        # Détermine le chemin complet du projet
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        # Crée le répertoire parent si nécessaire
        parent_path = os.path.dirname(full_project_path)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)

        # Change le répertoire courant pour le répertoire parent
        os.chdir(parent_path)

        # Utilise le chemin complet vers dancer2
        dancer2_path = "/usr/bin/dancer2"  # Remplacez par le chemin correct si nécessaire
        command = f"{dancer2_path} gen -a {project_name}"
        
        try:
            stdout, stderr = self.execute_command(command)
            if stderr:
                print(f"Erreur lors de la création du projet Dancer2: {stderr}")
            else:
                print(f"Le projet Dancer2 '{project_name}' a été créé avec succès dans {full_project_path}.")
        except Exception as e:
            print(f"Une exception s'est produite: {e}")

    def _setup_dancer2_project(self, project_name, path):
        os.chdir(path)
        command = f"dancer2 -a {project_name}"
        self.execute_command(command)
        os.chdir("..")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')