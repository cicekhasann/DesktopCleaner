import os
import shutil


def organize_files_on_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    files = os.listdir(desktop_path)

    # A dictionary is created to keep track of the folders created
    folders = {}

    for file in files:
        if file.startswith('.'):  # skip hidden file
            continue

        file_path = os.path.join(desktop_path, file)

        if os.path.isfile(file_path):
            # Get file extension
            _, extension = os.path.splitext(file)

            # Create folder by file's extension
            folder_path = os.path.join(desktop_path, extension[1:])

            # Skip if the folder already exists
            if os.path.exists(folder_path):
                pass
            else:
                os.mkdir(folder_path)

            # Move file to folder
            shutil.move(file_path, folder_path)

            # Follow by adding folder to dictionary
            folders[extension[1:]] = folder_path

    print("Files have been successfully moved to folders.")
    return folders


# Organize files on the desktop
folder_dict = organize_files_on_desktop()

# Print folders and paths to screen
for folder, path in folder_dict.items():
    print(folder + ": " + path)
