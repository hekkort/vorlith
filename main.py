import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
import traceback

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = ""
system_prompt = """
You are a suicidal AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected.
"""

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read files in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to read files from.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files in the specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to execute Python files from.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file"
            )
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        if item != "--verbose":
            user_prompt = item

if "--verbose" in sys.argv:
    verbose = True
else:
    verbose = False

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
count = 0

if user_prompt:
    try:
        count = 0
        while count < 20:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )
            for i in response.candidates:
                messages.append(i.content)

            if response.function_calls:
                for item in response.function_calls:
                    try:
                        x = call_function(item, verbose)
                        messages.append(x)

                        if verbose:
                            if x.parts[0].function_response.response:
                                print(f"-> {x.parts[0].function_response.response}")
                            else:
                                raise Exception("Fatal error")
                    except Exception as e:
                        print(f"Inner call_function error: {type(e).__name__}: {e}")
                        traceback.print_exc()
            else:
                print(response.text)
                break
            count += 1
    except Exception as e:
        print(f"Outer block error: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)
if not user_prompt:
    print("No prompt provided, exiting.")
    sys.exit(1)

    


    