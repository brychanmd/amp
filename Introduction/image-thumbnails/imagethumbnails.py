import directory

# Get directory path for where thumbnails will be created
# e.g. '/Users/brychan/Pictures/ImageThumbs'
directory_path = input("Please enter directory path: ")

if not directory.check_directory(directory_path):
    print('Error: Invalid directory path. Please try again with a valid path to directory.')
    quit()

# Get new directory name from user, and check if it already exists.
while True:
    try:
        new_directory = input("Please enter new directory name: ")
    except:
        print("Error, please try again")
        continue
    if directory.check_directory(directory.new_dir_path(directory_path, new_directory)):
        print('Error: Non unique name.')
        continue
    else:
        break

# Get list of desired file types to alter.
# e.g. ['jpg', 'png']
filetypes = input("List all filetypes you want converted, separated by commas e.g. 'jpg,png': ").split(',')

# List of files available to edit in the chosen directory.
my_files = directory.list_files(directory_path, filetypes)

# Check if there are any files to edit.
if not my_files :
    print('Error: There are no images of your chosen filtypes in this directory.')
    quit()
    
# Get desired thumbnail size from user.
# e.g. '128'
while True:
    try:
        thumbnail_size = int(input("Thumbnail size in pixels: "))
    except ValueError: 
        print('Error: Please enter a valid number.')
        continue
    if thumbnail_size < 1:
        print('Error: Please enter a positive number.')
        continue
    else:
        break

# Execute the function that creates thumbnails in the new directory.
directory.image_thumbnails( directory_path, new_directory, my_files, thumbnail_size )


