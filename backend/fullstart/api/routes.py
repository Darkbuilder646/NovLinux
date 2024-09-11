from flask import current_app, jsonify
from frameworks.javascript_frameworks import ReactFramework, VueJSFramework, ExpressFramework, NativeJSFramework
from frameworks.php_frameworks import LaravelFramework, SymfonyFramework, NativePHPFramework
from frameworks.python_frameworks import DjangoFramework, FastAPIFramework, FlaskFramework
from frameworks.rust_frameworks import RocketFramework, TauriFramework
from frameworks.perl_frameworks import CatalystFramework, Dancer2Framework
from frameworks.ruby_frameworks import RailsFramework, SinatraFramework
from frameworks.typescript_frameworks import AngularFramework, NestJSFramework

AVAILABLE_LANGUAGES = ["Java", "Javascript", "PHP", "Python", "Rust", "Typescript", "Dart", "Perl", "Ruby"]

LANGUAGE_FRAMEWORKS = {
    "java": ["Springboot"],
    "javascript": ["Native", "Express", "Vue", "React"],
    "php": ["Laravel", "Symfony", "Native"],
    "python": ["Django", "Fastapi", "Flask"],
    "rust": ["Rocket", "Tauri"],
    "typescript": ["Angular", "Nest"],
    "perl": ["Dancer2", "Catalyst"],
    "ruby": ["Rails", "Sinatra"],
}

@current_app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(AVAILABLE_LANGUAGES)

@current_app.route('/frameworks/<language>', methods=['GET'])
def get_frameworks(language):
    frameworks = LANGUAGE_FRAMEWORKS.get(language.lower())
    if frameworks is None:
        return jsonify({"error": "Language not supported"}), 400
    return jsonify(frameworks)

@current_app.route('/install/<language>/<framework>', methods=['POST'])
def install_dependencies(language, framework):
    project = get_project(language, framework)
    if project is None:
        return jsonify({"error": "Language or framework not supported"}), 400
    output, error = project.install_dependencies()
    return jsonify({"output": output, "error": error})

@current_app.route('/run/<language>/<framework>', methods=['POST'])
def run_framework(language, framework):
    project = get_project(language, framework)
    if project is None:
        return jsonify({"error": "Language or framework not supported"}), 400
    output, error = project.run_project()
    return jsonify({"output": output, "error": error})

from flask import request, jsonify, current_app

@current_app.route('/run_with_details', methods=['POST'])
def run_framework_with_details():
    data = request.json
    language = data.get('language')
    framework = data.get('framework')
    project_name = data.get('project_name')
    project_path = data.get('project_path')

    # Vérifiez si toutes les informations nécessaires sont fournies
    if not all([language, framework, project_name, project_path]):
        return jsonify({"error": "Missing data in request"}), 400

    project = get_project(language, framework)
    if project is None:
        return jsonify({"error": "Language or framework not supported"}), 400

    try:
        output, error = project.run_project_details(project_name, project_path)
        return jsonify({"output": output, "error": error})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_project(language, framework):
    language = language.lower()
    framework = framework.lower()
    if language == "javascript":
        if framework == "express":
            return ExpressFramework()
        elif framework == "vue":
            return VueJSFramework()
        elif framework == "react":
            return ReactFramework()
        elif framework == "native":
            return NativeJSFramework()
    elif language == "php":
        if framework == "laravel":
            return LaravelFramework()
        elif framework == "symfony":
            return SymfonyFramework()
        elif framework == "native":
            return NativePHPFramework()
    elif language == "python":
        if framework == "django":
            return DjangoFramework()
        elif framework == "fastapi":
            return FastAPIFramework()
        elif framework == "flask":
            return FlaskFramework()
    elif language == "rust":
        if framework == "rocket":
            return RocketFramework()
        elif framework == "tauri":
            return TauriFramework()
    elif language == "typescript":
        if framework == "angular":
            return AngularFramework()
        elif framework == "nest":
            return NestJSFramework()
    elif language == "perl":
        if framework == "catalyst":
            return CatalystFramework()
        elif framework == "dancer2":
            return Dancer2Framework()
    elif language == "ruby":
        if framework == "rails":
            return RailsFramework()
        elif framework == "sinatra":
            return SinatraFramework()
    # Ajoutez les autres langages et frameworks si nécessaire
    return None