from api.app import app
import threading

def run_api():
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
