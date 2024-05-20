import os
import shutil
source = "C:/Users/Admin/OneDrive/Documents/ABC"
destination = "C:/Users/Admin/OneDrive/Desktop"
files = os.listdir(source)
print(files)
for i in files:
    name,ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in[".txt", ".doc", ".docx", ".pdf"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "document_files"
        path3 = destination + "/" + "document_files" + "/" + i
        if os.path.exists(path2):
            print("Folder already exists and moving the file")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Creating the folder and moving the file")
            shutil.move(path1,path3)