import subprocess

def install_fastapi():
    # Update the package list
    subprocess.run(["xbps-install", "-Sy"])

    # Install Python3 and pip
    subprocess.run(["xbps-install", "-y", "python3", "python3-pip"])

    # Install FastAPI
    result = subprocess.run(["pip3", "install", "fastapi"])
    if result.returncode != 0:
        print("Error installing FastAPI.")
        return

    # Install Uvicorn
    result = subprocess.run(["pip3", "install", "uvicorn[standard]"])
    if result.returncode != 0:
        print("Error installing Uvicorn.")
        return

    print("FastAPI and Uvicorn installed successfully.")

# Call the function to install FastAPI
install_fastapi()