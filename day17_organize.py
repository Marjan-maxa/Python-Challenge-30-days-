from pathlib import Path
import shutil
folder=Path("sona_paki")
for files in folder.iterdir():
    if files.suffix.lower() in [".png",".jpeg"]:
        category="images"
    elif files.suffix.lower()==".pdf" :
        category="pdfs"
    elif files.suffix.lower()==".py" :
            category="pys"
    elif files.suffix.lower()=="txt" :
            category="textFiles"
    else:
        continue
    destination_folder=folder/category
    destination_folder.mkdir(exist_ok=True)
    destination=destination_folder/files.name
    if destination.exists():
        print("File is already exict",files.name)    
    else:
    
        shutil.move(str(files),str(destination))
        print("Moved ", files.name ,"-->",category)    
              
               