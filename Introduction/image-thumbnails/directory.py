from PIL import Image
import os

# Accepts filepath and list of filtypes.
# Returns list of available files of that filetype.
def list_files(path, filetypes):
    
    filetype_tuple = list_to_tuple(filetypes)
    files_list = []

    for file in os.listdir(path):
        if file.endswith(filetype_tuple):
            files_list.append(file)
            
    return files_list

# Accepts filepath to parent directory, name for new directory, list of files to convert, size dimensions for thumbnails.
# Returns nothing, but created thumbnails and prints out progress.
def image_thumbnails(parent_dir, new_dir, files, size):
    
    # Keep a record of thumbnails created.
    counter = 0
    
    path = new_dir_path(parent_dir, new_dir)
 
    try: 
        os.mkdir(path)
        print("Directory '% s' created" % new_dir)
    except OSError as error:
        print(error)
        return
        
    # Loop through the files in the directory and create thumnail.
    for file in files:
        im = Image.open(os.path.join( parent_dir, file ))
        im.thumbnail( (size, size) )
        # Concatonate thumbnail size with original image name.
        im.save( os.path.join( path, str(size) + '_' + file ))
        # Increment thumbnail counter.
        counter = counter + 1
        
    print( str(counter) + ' thumbnails created')
    
    return

# Accepts list.
# Returns tuple with all interies in lowercase and caps.
def list_to_tuple(my_list):
    
    # Start by building a list, accounting for upper and lower case.
    my_tuple = []
    for item in my_list:
        my_tuple.append(item.lower())
        my_tuple.append(item.upper())

    # Convert list to tuple.
    my_tuple = tuple(my_tuple)
    
    return my_tuple

# Accepts parent directory, and new directory name.
# Returns joined filepath to new directory.
def new_dir_path(parent_dir, new_dir):
    
    return os.path.join(parent_dir, new_dir)

# Accepts filepath.
# Returns boolean value to indicate if the directory exists.
def check_directory( path ):
    
    if os.path.isdir(path):
        return True
    else:
        return False
    