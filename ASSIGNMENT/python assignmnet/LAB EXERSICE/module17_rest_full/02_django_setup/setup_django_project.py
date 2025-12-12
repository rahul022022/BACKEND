\"\"\"
Small helper script to create a Django project called `doctor_finder` and install
basic apps. You can also follow the instructions in README instead of running this.

Usage (after creating and activating a virtualenv):

    python setup_django_project.py
\"\"\"
import subprocess
import sys

def run(cmd):
    print(f"$ {cmd}")
    subprocess.check_call(cmd, shell=True)

def main():
    # Install requirements
    run(f"{sys.executable} -m pip install --upgrade pip")
    run(f"{sys.executable} -m pip install -r requirements.txt")

    # Create Django project (if you want a fresh one)
    # Comment this out if you are using the project from the zip.
    # run(f\"{sys.executable} -m django startproject doctor_finder ..\")

if __name__ == "__main__":
    main()
