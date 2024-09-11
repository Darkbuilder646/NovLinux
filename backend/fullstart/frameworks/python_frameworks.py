from .base_framework import BaseFramework
import os
import subprocess

class DjangoFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")
        self.execute_command("xbps-install -y python3 python3-virtualenv python3-pip")
        self.execute_command("python3.12 -m venv venv")
        self.execute_command(". venv/bin/activate && python3.12 -m pip install setuptools")
        self.execute_command(". venv/bin/activate && python3.12 -m pip install Django==3.2.7")
        return "Django and dependencies installed.", ""

    def run_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        self._create_django_project_details(project_name, full_project_path)
        instructions = "Don't forget to run 'python manage.py runserver' at the root of your project."
        return instructions, ""

    def _create_django_project_details(self, project_name, project_path):
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        command = f". venv/bin/activate && django-admin startproject {project_name} {project_path}"
        stdout, stderr = self.execute_command(command)
        if stderr:
            print(f"Error creating Django project: {stderr}")
        else:
            print(f"Django project created successfully: {stdout}")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')


class FastAPIFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")
        self.execute_command("xbps-install -y python3 python3-virtualenv python3-pip")
        self.execute_command("python3 -m venv venv")
        self.execute_command("source venv/bin/activate && pip install fastapi[all]==0.68.1")
        return "FastAPI and dependencies installed.", ""

    def run_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        self._create_fastapi_project_details(full_project_path)
        instructions = "Don't forget to run 'uvicorn main:app --reload' at the root of your project."
        return instructions, ""

    def _create_fastapi_project_details(self, project_path):
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        with open(os.path.join(project_path, "main.py"), "w") as f:
            f.write("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')


class FlaskFramework(BaseFramework):
    def install_dependencies(self):
        self.execute_command("xbps-install -Sy")
        self.execute_command("xbps-install -y python3 python3-virtualenv python3-pip")
        self.execute_command("python3 -m venv venv")
        self.execute_command("source venv/bin/activate && pip install Flask==2.0.1")
        return "Flask and dependencies installed.", ""

    def run_project_details(self, project_name, project_path):
        full_project_path = os.path.join(project_path, project_name) if project_path else os.path.join(os.getcwd(), project_name)
        self._create_flask_project_details(full_project_path)
        instructions = "Don't forget to run 'python app.py' at the root of your project."
        return instructions, ""

    def _create_flask_project_details(self, project_path):
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        with open(os.path.join(project_path, "app.py"), "w") as f:
            f.write("""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
""")

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')