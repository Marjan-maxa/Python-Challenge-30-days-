# Challenge --1

import os
from pathlib import Path
print(os.getcwd())
folder=Path("Practice")
folder.mkdir(exist_ok=True)
print("Folder-->files :")
print("--------------------")
for files in folder.iterdir():
    
    if files.is_file():
        print(files)
        
 
 
 
 
 
 
        
        
# Challenge -- 2

from pathlib import Path

folder=Path("Practice")
files=list(folder.iterdir())
for file in files:
    print(file.name)
print("Total files :",len(files))           











#Challenges --3

from pathlib import Path


folder=Path("Practice")
for files in folder.iterdir():
    print(files.name,"-->",files.suffix)
   
   





#Challenge --4
   
from pathlib import Path
folder=Path("Test")
txt_files=folder.glob("*.txt")
index=1
for files in txt_files:
    new_note=folder/f"note{index}.txt"
    while files.exists():
        index+=1
        new_note=folder/f"note{index}.txt"
        files.rename(new_note)
        index+=1
print("Files Rename Successfully!")        








#Challenges -- 5

from pathlib import Path
import shutil
folder=Path("Test")
for files in folder.iterdir():
    if files.is_file():
        if files.suffix.lower() in [".jpeg",".png"]:
            category="img_files"
        elif files.suffix.lower()==".pdf":
            category="pdfs_files"
        elif files.suffix.lower()==".txt":
            category="txt_files"
        else:
            continue
        des_folder=folder/category
        des_folder.mkdir(exist_ok=True) 
        destination=des_folder/files.name 
        if destination.exists():
            print("File already exist!",files.name)
        else:
             shutil.move(str(files),str(destination))   
             print("Moved",files.name,"-->",destination)
                    
                    
                    
                    
                    
                    




# Challenges -- 6

from pathlib import Path      
folder=Path("Test")
try:
    fileName=input("Enter your file name :")
    file=None
    for item in folder.rglob(fileName):
        if item.is_file():
            file=item
            break
    if file is not None:
        print("Your File is found")
        print("File Name :",file.name)
        print("Extention Name :",file.suffix)
        print("File Size :",file.stat().st_size,"byte")    
 
                        
except OSError as error:
    print("System Crashed!",error)













# Home Work

from pathlib import Path
import shutil
folder=Path("Download_test")
images=[".jpeg",".png"]
pdfs=[".pdf"]
txt_files=[".txt"]
skipped=0
moved=0

for files in folder.iterdir():
    
    if files.is_file():
        tex=files.suffix.lower()
        if tex in images:
            destination=folder/"Images"
        elif tex in pdfs:
            destination=folder/"PDFS"
        elif tex in txt_files:
            destination=folder/"Text_files"   
        else:
            continue
    destination.mkdir(exist_ok=True)    
    new_file=destination/files.name   
    if new_file.exists():
        print("Skipped ",files.name)
        skipped+=1
    else:
        shutil.move(str(files),str(destination))
        print("Moved ",files.name)
        moved+=1
               
print("------------Summary ------------------")        
print("Successfully moved :",moved)
print("Skipped ",skipped)        










# mini-Project 

from pathlib import Path
import shutil
from datetime import datetime

report=Path("students_Report.txt")
backup_folder=Path("backups")
try:
    name=input("ERnter Student Name :")
    marks=float(input("Enter Students  marks :"))
    
    #grade cal]culate
    
    if marks>=80:
        grade="A+"
    elif marks>=70:
        grade="A"  
    elif marks>=60:
        grade="B"
              
    elif marks>=50:
        grade="C"
    elif marks>=40:
        grade="D"
    else:
        grade="F"
        
        
    # save     
    with open(report,"a") as file:
        print("       ")
        print("       ")
        file.write("Student Performance Report \n")
        file.write("----------------------------\n")
        file.write(f"Name : {name}\n")
        file.write(f"Marks : {marks}\n")
        file.write(f"Grade : {grade}\n")
    print("Report saved successfully!")
    # backup folder create 
    backup_folder.mkdir(exist_ok=True) 
    current_time=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    backup_file=backup_folder/f"student_report{current_time}.txt"
    
    #copy report to backup_file
    shutil.copy2(report,backup_file)
    print("Backup Created Successfully!")   
    print("Backup locaton :",backup_file)
except(ValueError,OSError) as error:
    print("System Crashed ",error)
        