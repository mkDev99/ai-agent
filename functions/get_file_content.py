import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    print(abs_file_path)

    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, 'r') as f:
            file_content = f.read()
            if len(file_content) > MAX_CHARS:
                return file_content[:10000] + '[...File "{file_path}" truncated at 10000 characters]'
            return file_content
    except Exception as e:
        return f'Error reading file: {e}'
