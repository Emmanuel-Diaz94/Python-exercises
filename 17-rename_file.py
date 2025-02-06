import os 

folder_path = r"C:\Users\sergi\OneDrive\Escritorio\python" 

files =  os.listdir(folder_path)

for file in files: 

    if "factura" in file and file.endswith(".doc"):

        new_name = "bindustry_" + file
        
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        
        os.rename(old_file, new_file)