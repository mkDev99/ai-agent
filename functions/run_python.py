import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        run = subprocess.run(['python3', abs_file_path], capture_output=True)

        std_output = run.stdout
        std_error = run.stderr

        if std_output is None:
            return 'No output produced.'

        output = f'STDOUT: {std_output}\nSTDERR: {std_error}'
        if run.returncode != 0:
            output += f'\nProcess exited with code {run.returncode}'

        return output
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
