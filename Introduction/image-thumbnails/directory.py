from PIL import Image
import os

def list_files( path, filetypes ):
    
    filetype_tuple = list_to_tuple(filetypes)
    files_list = []

    for file in os.listdir(path):
        if file.endswith(filetype_tuple):
            files_list.append(file)
            
    return files_list

def image_thumbnails(parent_dir, new_dir, files, size):
    
    counter = 0
    
    path = os.path.join(parent_dir, new_dir)
    print(path)
    try: 
        os.mkdir(path)
        print("Directory '% s' created" % new_dir)
    except OSError as error:
        print(error)
        return
        
    for file in files:
        im = Image.open(os.path.join( parent_dir, file ))
        im.thumbnail( (int(size), int(size)) )
        im.save( os.path.join( path, size + '_' + file ))
        counter = counter + 1
        
    print( str(counter) + ' thumbnails created')
    
    return

def list_to_tuple( my_list ):
    
    # Start by building a list, accounting for upper and lower case.
    my_tuple = []
    for item in my_list:
        my_tuple.append(item.lower())
        my_tuple.append(item.upper())

    # Convert list to tuple.
    my_tuple = tuple(my_tuple)
    
    return my_tuple

