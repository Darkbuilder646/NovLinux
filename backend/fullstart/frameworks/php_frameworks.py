from .base_framework import BaseFramework
import os
import subprocess


class LaravelFramework(BaseFramework):
    def install_dependencies(self):
        # Met à jour la liste des paquets
        self.execute_command("sudo xbps-install -Sy")

        # Installe PHP et les extensions nécessaires
        self.execute_command("sudo xbps-install -y php php-fpm php-mbstring php-xml php-pdo php-zip php-gd php-curl")

        # Installe Composer
        self.execute_command("sudo xbps-install composer")

        # Installe Laravel Installer
        self.execute_command("composer global require laravel/installer")

        # Ajoute le répertoire bin de Composer au PATH dans le fichier de profil de l'utilisateur
        bashrc_path = os.path.expanduser("~/.bashrc")
        with open(bashrc_path, "a") as f:
            f.write('export PATH="$HOME/.config/composer/vendor/bin:$PATH"\n')

        return "Laravel and dependencies installed. Please run 'source ~/.bashrc' or restart your shell to update your PATH.", ""

    def run_project_details(self, project_name, project_path):
        print(f"Creating Laravel project: {project_name}")
        self._create_laravel_project_details(project_name, project_path)
        instructions = "Don't forget to run 'php artisan serve' at the root of your project."
        return instructions, ""

    def _create_laravel_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        if not os.path.exists(full_project_path):
            os.makedirs(full_project_path)

        command = f"composer create-project --prefer-dist laravel/laravel {full_project_path}"
        try:
            subprocess.check_call(command, shell=True)
            print(f"Le projet Laravel {project_name} a été créé avec succès dans {project_path}.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création du projet Laravel: {e}")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

class NativePHPFramework(BaseFramework):
    def install_dependencies(self):

        self.execute_command("sudo xbps-install -Sy")

        self.execute_command("sudo xbps-install -y php")

        return "PHP and dependencies installed.", ""

    def run_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        if not os.path.isdir(full_project_path):
            os.makedirs(full_project_path)
        
        create_status, create_message = self._create_native_project_details(full_project_path)
        if not create_status:
            return None, create_message
        
        instructions = "Don't forget to run 'php -S localhost:8000' at the root of your project."
        return instructions, ""

    def _create_native_project_details(self, project_path):
        try:
            index_php_content = """<?php
                echo "Hello, World!";
            ?>"""
            with open(os.path.join(project_path, 'index.php'), 'w') as f:
                f.write(index_php_content)
            
            composer_json_content = """{
                "name": "native/php-project",
                "description": "A native PHP project",
                "require": {}
            }"""
            with open(os.path.join(project_path, 'composer.json'), 'w') as f:
                f.write(composer_json_content)
            
            return True, "Native PHP project created successfully."
        except Exception as e:
            return False, str(e)

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

class SymfonyFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")

        self.execute_command("xbps-install -y composer")

        result, error = self.execute_command("curl -sS https://get.symfony.com/cli/installer | bash")
        if error:
            return f"Error installing Symfony CLI: {error}", ""

        self.execute_command("mv /root/.symfony5/bin/symfony /usr/local/bin/symfony")

        return "Symfony CLI and dependencies installed. Please run 'source ~/.bashrc' or restart your shell to update your PATH.", ""

    def _create_symfony_project_details(self, project_path):
        try:
            command = f"composer create-project symfony/skeleton {project_path}"
            stdout, stderr = self.execute_command(command)
            if stderr:
                return False, stderr
            
            return True, "Symfony project created successfully."
        except Exception as e:
            return False, str(e)

    def run_project_details(self, project_name, project_path):

        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        
        if not os.path.exists(full_project_path):
            os.makedirs(full_project_path, exist_ok=True)
        
        create_status, create_message = self._create_symfony_project_details(full_project_path)
        if not create_status:
            return None, create_message
        
        command = f"cd {full_project_path} && php bin/console server:run"
        stdout, stderr = self.execute_command(command)
        
        if stderr:
            return stdout, stderr
        else:
            instructions = "Don't forget to run 'php bin/console server:run' at the root of your project."
            return instructions, ""

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
