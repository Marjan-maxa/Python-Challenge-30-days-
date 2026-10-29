from pathlib import Path
folder=Path("sona_paki")
try:
    for files in folder.iterdir():
        if files.is_file():
            print(files.name)
except OSError as erroe:
    print("Folder could'n access",erroe)            