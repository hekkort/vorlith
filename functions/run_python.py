import os

def run_python_file(working_directory, file_path):
    abs_file_path = os.path.join(os.path.abspath(working_directory), file_path)

    if os.path.commonpath([abs_file_path, working_directory]) != working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
