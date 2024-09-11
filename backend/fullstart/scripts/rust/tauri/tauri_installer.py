import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr.decode()}")

def install_tauri_dependencies():
    # Installe Node.js et Yarn à partir des dépôts XBPS
    run_command("xbps-install -Sy nodejs yarn")

    # Installe Rust à partir des dépôts XBPS
    run_command("xbps-install -Sy rust")

# Installe les dépendances de Tauri
install_tauri_dependencies()

print("Tauri dependencies installed successfully.")