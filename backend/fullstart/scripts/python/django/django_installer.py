import subprocess

def install_django():
    # Update the package list
    subprocess.run(["xbps-install", "-Sy"])

    # Install Python3 and pip
    subprocess.run(["xbps-install", "-y", "python3", "python3-pip"])

    # Install Django using pip
    result = subprocess.run(["pip3", "install", "Django"])
    if result.returncode != 0:
        print("Error installing Django.")
        return

    print("Django installed successfully.")

# Call the function to install Django
install_django()