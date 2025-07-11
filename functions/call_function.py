from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .write_file import write_file
from google.genai import types



def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"- Calling function: {function_call_part.name}")

    if function_call_part.name == "get_file_content":
        kw_dict = {"working_directory": "./calculator", "file_path": function_call_part.args["file_path"]}
        x = get_file_content(**kw_dict)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": x},
                )
            ],
        )

    elif function_call_part.name == "get_files_info":
        kw_dict = {"working_directory": "./calculator", "directory": function_call_part.args.get("directory", ".")}
        x = get_files_info(**kw_dict)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": x},
                )
            ],
        )
    
    elif function_call_part.name == "run_python_file":
        kw_dict = {"working_directory": "./calculator", "file_path": function_call_part.args["file_path"]}
        x = run_python_file(**kw_dict)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": x},
                )
            ],
        )
    
    elif function_call_part.name == "write_file":
        kw_dict = {"working_directory": "./calculator", "file_path": function_call_part.args["file_path"], "content": function_call_part.args["content"]}
        x = write_file(**kw_dict)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": x},
                )
            ],
        )

    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )