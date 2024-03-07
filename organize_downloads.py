"""
Organize Files in Downloads Folder
"""
import os
import shutil

# Use os.path.expanduser to get the current user's Downloads folder dynamically
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Continue with the extended extension_to_folder mapping as discussed before...
extension_to_folder = {
    # Documents
    '.xlsx': 'excel-files',
    '.xls': 'excel-files',
    '.docx': 'word-documents',
    '.doc': 'word-documents',
    '.pptx': 'powerpoint-presentations',
    '.ppt': 'powerpoint-presentations',
    '.pdf': 'pdf-files',
    '.txt': 'text-files',
    '.csv': 'csv-files',
    
    # Images
    '.jpg': 'images',
    '.jpeg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.bmp': 'images',
    '.tiff': 'images',
    '.svg': 'images',
    
    # Music
    '.mp3': 'music',
    '.wav': 'music',
    '.aac': 'music',
    '.flac': 'music',
    '.m4a': 'music',
    '.ogg': 'music',
    
    # Videos
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mov': 'videos',
    '.wmv': 'videos',
    '.mkv': 'videos',
    '.flv': 'videos',
    
    # Executables
    '.exe': 'executables',
    '.msi': 'executables',
    
    # Archives
    '.zip': 'compressed',
    '.rar': 'compressed',
    '.7z': 'compressed',
    '.tar': 'compressed',
    '.gz': 'compressed',
    
    # Programming and Code
    '.py': 'code-files',
    '.js': 'code-files',
    '.html': 'code-files',
    '.css': 'code-files',
    '.java': 'code-files',
    '.c': 'code-files',
    '.cpp': 'code-files',
    
    # eBooks
    '.epub': 'ebooks',
    '.mobi': 'ebooks',
    
    # Others (no need to list them here, they will be moved to 'other' by default)
}


# Iterate over each file in the 'Downloads' folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    # Check if it's a file and not a directory
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        destination_folder_name = extension_to_folder.get(file_extension, 'other')
        destination_folder_path = os.path.join(downloads_path, destination_folder_name)
        
        # Create the destination folder if it does not exist
        if not os.path.exists(destination_folder_path):
            os.makedirs(destination_folder_path)
        
        # Construct the destination file path
        dest_file_path = os.path.join(destination_folder_path, filename)
        
        # Check if the file already exists in the destination to avoid overwriting
        if os.path.exists(dest_file_path):
            base, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(dest_file_path):
                # Create a new file name by appending a counter to the base name
                new_filename = f"{base} ({counter}){extension}"
                dest_file_path = os.path.join(destination_folder_path, new_filename)
                counter += 1
        
        # Move the file
        try:
            shutil.move(file_path, dest_file_path)
            print(f"Moved '{filename}' to '{destination_folder_path}'")
        except Exception as e:
            print(f"Error moving file '{filename}': {e}")

# Print a message when done
print("Files have been organized.")
