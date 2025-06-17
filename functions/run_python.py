import os
from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path):

    working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(working_directory, file_path)
    path = Path(abs_file_path)
    resolved_path = path.resolve()
    resolved_path = str(resolved_path)
    
    # print(resolved_path[-3:])
    # print(resolved_path)
    # print(os.path.exists(resolved_path))

    if os.path.commonpath([resolved_path, working_directory]) != working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    elif not os.path.exists(resolved_path):
        return f'Error: File "{file_path}" not found.'
    
    elif resolved_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    else:
        try:
            x = subprocess.run(["python3", resolved_path], capture_output=True, timeout=30)
            string = str(x.stdout) + str(x.stderr) + str(x.returncode)
            return string
        except Exception as e:
            return f"Error: executing Python file: {e}"
