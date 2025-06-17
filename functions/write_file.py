import os

def write_file(working_directory, file_path, content):

    working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(working_directory, file_path)

    dirname = os.path.dirname(abs_file_path)

    if os.path.commonpath([abs_file_path, working_directory]) != working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(dirname, exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: could not create directory{e}'