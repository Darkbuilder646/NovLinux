import subprocess

class BaseFramework:
    def install_dependencies(self):
        raise NotImplementedError

    def run_project(self):
        raise NotImplementedError

    def execute_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
