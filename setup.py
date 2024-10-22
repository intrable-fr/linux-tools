import os
import time

setup = """
 _______  _______ _________          _______ 
(  ____ \(  ____ \\__   __/|\     /|(  ____ )
| (    \/| (    \/   ) (   | )   ( || (    )|
| (_____ | (__       | |   | |   | || (____)|
(_____  )|  __)      | |   | |   | ||  _____)
      ) || (         | |   | |   | || (      
/\____) || (____/\   | |   | (___) || )      
\_______)(_______/   )_(   (_______)|/       
[!]Bienvenue dans le Menu d'installations , cela installer que les modules python
[!]quand vous serrez sur le main , avant d'utiliser chaque programme , faites bien l'option 3
"""
print(setup)
print('[*]Les Modules vont etres installer dans 3 seconde')
time.sleep(3)
os.system('pip install colorama')
os.system('pip install fade')
os.system('pip install clear')
print('[*]tout les requirement ont etais installer !')
input('[*]Appuyer sur entrée pour Aller au menu principal...')
os.system('clear')
os.system('python3 linux-tool.py')
