from pathlib import Path
folder=Path("sona_paki")
for files in folder.iterdir():
    if files.is_file():
        print(files.name,"-->",files.suffix)
if files.suffix.lower() in [".png",".jpeg"]:
    print("This is image")
elif files.suffix.lower()==".pdf":
    print("This is pdf")
elif files.suffix.lower()==".py" :
    print("This is py ") 
else:
    print("This is txt")          
        
