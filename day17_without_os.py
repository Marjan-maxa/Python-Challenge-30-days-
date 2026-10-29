from pathlib import Path
# folder=Path("sona_paki")
# folder.mkdir(exist_ok=True)
# print("Folder Exist :",folder.exists())
# print("Is Foder :",folder.is_dir())
# file_path=Path("te.py")
# if file_path.exists():
#     print("File found in the root directory!")
# else:
#     print("Sorry ,File not found")    

folder=Path("sona_paki")
files=[]
for item in folder.iterdir():
    if item.is_file():
        files.append(item)
print("Total files in the dir :",len(files))        

for file in files:
    print(file.name )


    
    