import os
import sys

def pre_gen_project():
    """
    This hook script runs before the project is generated.
    It checks if the specified code file exists and exits with an error if it does not.
    """
    code_file = "{{ cookiecutter.code_file }}"
    if not os.path.isfile(code_file):
        print(f"Error: The specified code file {code_file} does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    pre_gen_project()
