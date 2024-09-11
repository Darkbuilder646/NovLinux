import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def install_go():
    # Installe Go à partir des dépôts XBPS
    run_command("xbps-install -Sy go")

# Installe Go
install_go()