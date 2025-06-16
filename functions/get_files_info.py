import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    joined = os.path.join(working_directory, directory)
    #print(working_directory)
    #print(joined)
    #print("=======")
    if os.path.commonpath([joined, working_directory]) != working_directory or directory.startswith(".."):
        return f'Error: Cannot list "{joined}" as it is outside the permitted working directory'
    elif not os.path.isdir(joined):
        return f'Error: "{joined}" is not a directory'
    else:
        string = ""
        lst = os.listdir(joined)
        #print(lst)
        for l in lst:
            path_string = os.path.join(working_directory, directory)
            #print(path_string)
            #print(l)
            string += f"- {l}: file_size={os.path.getsize(path_string + '/' + l)} bytes, is_dir={os.path.isdir(path_string + '/' + l)}\n"

        return string