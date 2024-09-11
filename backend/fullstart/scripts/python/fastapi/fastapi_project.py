class Setup:
    def __init__(self):
        self.password = getpass("Enter your password: ")
        self.path = input("Enter the directory where you want to set up the project (leave blank for current directory): ")
        self.python_version = input("Enter the Python version you want to install (default is python3): ")
        self.fastapi_version = input("Enter the FastAPI version you want to install (default is 0.68.1): ")
        self.db_type = input("Enter the type of database you want to use (sqlite, postgres, mysql, mongodb): ")
        self.python_version = self.python_version if self.python_version else "python3"
        self.fastapi_version = self.fastapi_version if self.fastapi_version else "0.68.1"
        if self.path:
            os.chdir(self.path)

    def setup_python_project(self):
        print("Setting up Python project...")
        subprocess.run(["echo", self.password, "|", "sudo", "-S", "xbps-install", "-Su"], shell=True)
        subprocess.run(["echo", self.password, "|", "sudo", "-S", "xbps-install", "-y", self.python_version, f"{self.python_version}-virtualenv", f"{self.python_version}-pip"], shell=True)
        os.system(f"{self.python_version} -m venv venv")
        os.system(f"source venv/bin/activate && pip install fastapi[all]=={self.fastapi_version}")

    def setup_database(self):
        if self.db_type == "sqlite":
            os.system(f"source venv/bin/activate && pip install sqlalchemy aiosqlite")
        elif self.db_type == "postgres":
            os.system(f"source venv/bin/activate && pip install sqlalchemy asyncpg")
        elif self.db_type == "mysql":
            os.system(f"source venv/bin/activate && pip install sqlalchemy aiomysql")
        elif self.db_type == "mongodb":
            os.system(f"source venv/bin/activate && pip install motor")

    def start_project(self):
        with open("main.py", "w") as f:
            f.write("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")
        print("Python FastAPI project setup complete.")

    def run(self):
        self.setup_python_project()
        self.setup_database()
        self.start_project()

setup = Setup()
setup.run()