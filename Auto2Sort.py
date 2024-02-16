import os
import shutil

def sort_files_by_extension(folder_path):
    # Ensure the specified directory exists
    if not os.path.exists(folder_path):
        print("Specified directory does not exist.")
        return

    # Create a dictionary to hold file extensions and their respective folders
    extensions_folders = {
        'epub': 'Books',
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'doc': 'Documents',
        'docx': 'Documents',
        'xls': 'Spreadsheets',
        'xlsx': 'Spreadsheets',
        'jpg': 'Images',
        'png': 'Images',
        'gif': 'Images',
        'mp3': 'Audio',
        'mp4': 'Videos',
        'zip': 'Archives',
        # Add more file extensions and their corresponding folders as needed
    }

    # Get all files in the specified directory
    files = os.listdir(folder_path)

    if not files:
        print("No files found in the specified directory.")
        return

    print("Sorting files...")

    # Iterate over each file and move it to the corresponding folder based on its extension
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_extension = file_name.split('.')[-1].lower()
            if file_extension in extensions_folders:
                destination_folder = extensions_folders[file_extension]
                destination_path = os.path.join(folder_path, destination_folder)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                shutil.move(file_path, os.path.join(destination_path, file_name))
                print(f"Moved '{file_name}' to '{destination_folder}' folder.")

    print("Files sorted successfully!")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to sort: ")
    sort_files_by_extension(folder_path)
