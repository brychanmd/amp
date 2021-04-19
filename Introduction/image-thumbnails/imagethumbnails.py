import directory

# Get directory path for where thumbnails will be created
# directory_path = '/Users/brychan/Pictures/ImageThumbs'
directory_path = input("Please enter directory path: ")
new_directory = input("Please enter new directory name: ")

# Get list of desired file types to alter
# filetypes = ['JPG', 'PNG']
filetypes = input("List all filetypes you want converted, separated by commas e.g. 'jpg,png': ").split(',')

# Get desired thumbnail size from user
# thumbnailsize = '128'
thumbnail_size = input("Thumbnail size in pixels: ")

# List of files to edit.
my_files = directory.list_files(directory_path, filetypes)

directory.image_thumbnails( directory_path, new_directory, my_files, thumbnail_size )


