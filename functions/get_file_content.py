import os
MAX_CHARS = 10000
def get_file_content(working_directory, file_path):
    abs_file_path = os.path.join(os.path.abspath(working_directory), file_path)
    try:
        if os.path.isfile(abs_file_path):
            with open(abs_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    return file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
                return file_content_string
            
        elif os.path.commonpath([abs_file_path, working_directory]) != working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        elif not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error encountered: {e}"