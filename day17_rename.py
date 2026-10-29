from pathlib import Path
folder=Path("sona_paki")
image_files=sorted(
    list(folder.glob("*.jpg"))+
    list(folder.glob("*.png"))
)
index=1
for files in image_files:
    new_note=folder/f"photo{index}{files.suffix}"
    while new_note.exists():
        index+=1
        new_note=folder/f"photo{index}{files.suffix}"
    files.rename(new_note)
    index+=1
print("Rename Comleted !")    