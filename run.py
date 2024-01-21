import os
import subprocess
import webbrowser


def activate_venv():
    venv_activate_path = os.path.abspath(os.path.join(
        "C:\\Users\\Ventura\\Desktop\\Projects\\training-tracker-api", "venv", "Scripts", "activate"))
    subprocess.run([venv_activate_path], shell=True, check=True)


def run_uvicorn():
    uvicorn_path = os.path.abspath(os.path.join(
        "C:\\Users\\Ventura\\Desktop\\Projects\\training-tracker-api", "venv", "Scripts", "uvicorn.exe"))
    subprocess.Popen([uvicorn_path, "app.main:app"], shell=True)


def open_chrome():
    webbrowser.open("http://127.0.0.1:8000/docs")


if __name__ == "__main__":
    activate_venv()
    run_uvicorn()
    open_chrome()

    while True:
        pass
