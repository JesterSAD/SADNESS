import os

def change_extensions():
    for folder, subfolders, filenames in os.walk("C:\\"):
        for filename in filenames:
            if filename.endswith(".fun"):
                new_filename = filename[:-4] + ".exe"
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
            if filename.endswith(".smile"):
                new_filename = filename[:-6] + ".png"
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

change_extensions()
