import os
import shutil

def replace_files_in_subdirectories(base_directory, source_directory, filenames):
    """
    Replaces specific files in each subdirectory of a given directory with new files
    from a source directory.

    Args:
        base_directory (str): The path of the base directory containing subdirectories.
        source_directory (str): The path of the source directory containing the new files.
        filenames (list): List of filenames to be replaced.
    """
    # Ensure source files exist
    for filename in filenames:
        source_file_path = os.path.join(source_directory, filename)
        if not os.path.exists(source_file_path):
            print(f"Source file '{source_file_path}' does not exist. Please check your source directory.")
            return

    # Iterate through each subdirectory
    for subdirectory in os.listdir(base_directory):
        subdirectory_path = os.path.join(base_directory, subdirectory)

        if os.path.isdir(subdirectory_path):
            print(f"Processing subdirectory: {subdirectory_path}")

            for filename in filenames:
                destination_file_path = os.path.join(subdirectory_path, filename)

                # Replace the file
                try:
                    source_file_path = os.path.join(source_directory, filename)
                    shutil.copy2(source_file_path, destination_file_path)
                    print(f"Replaced '{destination_file_path}' with '{source_file_path}'.")
                except Exception as e:
                    print(f"Error replacing '{destination_file_path}': {e}")

if __name__ == "__main__":
    # Base directory containing subdirectories
    base_directory = "./pokemon"

    # Source directory containing the 4 new files
    source_directory = "./pokemon/wooper"

    # List of filenames to replace
    filenames = ["anim0.asm", "anim1.asm", "back.png", "front.png"]

    # Call the function
    replace_files_in_subdirectories(base_directory, source_directory, filenames)
