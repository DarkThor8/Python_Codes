text = "This is an example, of text processing."

translation_table = str.maketrans("aeiou", "12345", " ,")
translated_text = text.translate(translation_table)
print(translated_text)  

import os
import shutil

def organize_files_by_extension(directory):
    # List all files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get file extension
            file_extension = filename.split('.')[-1]
            if file_extension == filename:  # No extension
                file_extension = 'no_extension'
            
            # Create a directory for the file extension if it doesn't exist
            extension_dir = os.path.join(directory, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            
            # Move file to the corresponding directory
            shutil.move(file_path, os.path.join(extension_dir, filename))

# Input directory from user
directory = input("Enter the directory path to organize: ")

# Organize files in the specified directory
organize_files_by_extension(directory)

print("Files have been organized.")
 