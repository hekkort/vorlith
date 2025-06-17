import os
from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path):

    working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(working_directory, file_path)
    path = Path(abs_file_path)
    resolved_path = path.resolve()
    resolved_path = str(resolved_path)

    if os.path.commonpath([resolved_path, working_directory]) != working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    elif not os.path.exists(resolved_path):
        return f'Error: File "{file_path}" not found.'
    
    elif resolved_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    else:
        try:
            x = subprocess.run(["python3", resolved_path], capture_output=True, timeout=30)

            if x.returncode != 0:
                string = "STDOUT:" + str(x.stdout) + "\n" + "STDERR:" + str(x.stderr) + "\n" + "Process exited with code " + str(x.returncode)

            elif str(x.stderr) + str(x.stdout) + str(x.returncode) == "":
                return "No output produced"

            else:
                string = "STDOUT:" + str(x.stdout) + "\n" + "STDERR:" + str(x.stderr) + "\n" + str(x.returncode)
            
            return string
        except Exception as e:
            return f"Error: executing Python file: {e}"
