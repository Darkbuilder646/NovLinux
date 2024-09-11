import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr.decode()}")

def install_rust():
    # Installe Rust à partir des dépôts XBPS
    run_command("xbps-install -Sy rust")

# Installe Rust
install_rust()

print("Rust installed successfully.")