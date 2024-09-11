from .base_framework import BaseFramework
import os
import shutil

class SpringBootFramework(BaseFramework):
    def install_dependencies(self):
        if not self._check_spring_boot_cli():
            if not self._install_spring_boot_cli():
                return "Failed to install Spring Boot CLI.", ""
        self._setup_env_variables()
        return "Spring Boot CLI and dependencies installed.", ""

    def run_project(self):
        project_name = "my-spring-app"
        package_name = "com.example.myspringapp"
        self._create_spring_boot_project(project_name, package_name)
        command = f"cd {project_name} && ./mvnw spring-boot:run"
        return self.execute_command(command)

    def _check_spring_boot_cli(self):
        return self.execute_command("which spring")[0] != ""

    def _install_spring_boot_cli(self):
        commands = [
            "curl -o spring.zip https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-cli/3.3.0/spring-boot-cli-3.3.0-bin.zip",
            "unzip spring.zip -d /usr/local/",
            "rm -fr spring.zip",
            "mv /usr/local/spring-3.3.0 /usr/local/bin/"
        ]
        for cmd in commands:
            if not self.execute_command(cmd)[0]:
                return False

        java_versions = ["xbps-install -S openjdk", "xbps-install -S openjdk17", "xbps-install -S openjdk20", "xbps-install -S openjdk22"]
        for cmd in java_versions:
            if not self.execute_command(cmd)[0]:
                return False

        return True

    def _setup_env_variables(self):
        path_lines = [
            "export JAVA_HOME=/usr/lib/jvm/openjdk17",
            "export PATH=$JAVA_HOME/bin:$PATH",
            "export SPRING_HOME=/usr/local/bin/spring-3.3.0",
            "export PATH=$SPRING_HOME/bin:$PATH"
        ]

        shell_config_file = os.path.expanduser("~/.bashrc")
        with open(shell_config_file, 'r') as file:
            lines = file.readlines()

        with open(shell_config_file, 'a') as file:
            for line in path_lines:
                if line + '\n' not in lines:
                    file.write(line + '\n')

    def _create_spring_boot_project(self, project_name, package_name):
        command = f"spring init --dependencies=web {project_name}"
        self.execute_command(command)
        
        os.chdir(project_name)
        src_main_java = os.path.join("src", "main", "java")
        package_path = os.path.join(src_main_java, package_name.replace('.', os.sep))
        os.makedirs(package_path, exist_ok=True)
        
        main_app_content = f"""package {package_name};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {project_name.capitalize()}Application {{
    public static void main(String[] args) {{
        SpringApplication.run({project_name.capitalize()}Application.class, args);
    }}
}}
"""
        main_app_file = os.path.join(package_path, f"{project_name.capitalize()}Application.java")
        with open(main_app_file, 'w') as f:
            f.write(main_app_content)

        os.chdir("..")
