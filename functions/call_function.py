from get_files_info import get_files_info
from get_file_content import get_file_content
from run_python import run_python_file
from write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")


    function_name = function_call_part.name
    function_args = function_call_part.args

    function_args["working_directory"] = "./calculator"

    match function_name:
        case "get_files_info":
            return get_files_info(**function_args)
        case "get_file_content":
            return get_file_content(**function_args)
        case "run_python_file":
            return run_python_file(**function_args)
        case "write_file":
            return write_file(**function_args)
        case:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
