
#  Pour utiliser ce tool , il vous faut un systeme linux ou un wsl !!                            





import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
import fade                              # pour l'ascii art             
import time           
import colorama                           # pour l'ascii art
from colorama import Fore                 # pour l'ascii art
import clear           # clear c'est une super librairie qui permet de clear le terminal de chaque os
import sys



asciii = """
.____    .__                      ___________           .__          
|    |   |__| ____  __ _____  ___ \__    ___/___   ____ |  |   ______
|    |   |  |/    \|  |  \  \/  /   |    | /  _ \ /  _ \|  |  /  ___/   [*]Dev by intrable (id = 1282716636880830509)                                                  
|    |___|  |   |  \  |  />    <    |    |(  <_> |  <_> )  |__\___ \    [*]Version : 1.0
|_______ \__|___|  /____//__/\_ \   |____| \____/ \____/|____/____  >   [*]Discord.gg/freeforreal
        \/       \/            \/                                 \/ 
"""
asciii = fade.purplepink(asciii)
print(asciii)
question = Fore.MAGENTA+"[!]Appuyer sur entrée Pour aller au Menu..."
input(question)
clear.clear()

sqlmap = """
 ██▓     ██▓ ███▄    █  █    ██ ▒██   ██▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██▒    ▓██▒ ██ ▀█   █  ██  ▓██▒▒▒ █ █ ▒░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒██░    ▒██▒▓██  ▀█ ██▒▓██  ▒██░░░  █   ░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██░    ░██░▓██▒  ▐▌██▒▓▓█  ░██░ ░ █ █ ▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒                             # c'est un simple script , mais pratique. s'il vous plait , ne critiquez pas.
░██████▒░██░▒██░   ▓██░▒▒█████▓ ▒██▒ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░░   ░▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
  ░ ░    ▒ ░   ░   ░ ░  ░░░ ░ ░  ░    ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
    ░  ░ ░           ░    ░      ░    ░                  ░ ░      ░ ░      ░  ░      ░  
__________________________________________________________________________________________________________  
[!]juste un simple script qui automatise quelque linux tools , pour vous les rendre plus facile a utiliser
[!]ce n'est qu'une beta  !
__________________________________________________________________________________________________________ 
"""                                                                          

choix = Fore.MAGENTA+"[+]Votre Choix : "
sqlmap = fade.pinkred(sqlmap)
print(sqlmap)
print(Fore.BLUE+'[1]Vérifier si un site a des failles SQL (via sqlmap')
print(Fore.RED+'[2]Scanner Une adresse ip (via autorecon')
print(Fore.GREEN+'[3]Installer Tout Les tools nécessaire pour ce multitool')
print(Fore.YELLOW+'[4]Quitter')
choice = input(choix)
if "1" in choice.lower():
    lien = input(Fore.MAGENTA+"lien du site : ")
    os.system((f"sqlmap -u {lien} --batch"))
    input(Fore.MAGENTA+'C est la fin du scan. appuyer sur entrée pour revenir au menu...')
    clear.clear()
    os.system('python3 linux-tool.py')
    
if "2" in choice.lower():
  adresseip = input(Fore.MAGENTA+"Entrée l'adresse ip a scanner : ")
  os.system((f"autorecon {adresseip}"))
  input(Fore.MAGENTA+"L'adresse Ip a etais scanner avec succés. Appuyer sur entrée pour revenir au menu...")
  
if "3" in choice.lower():
  os.system('sudo apt install sqlmap && sudo apt install autorecon')
  input(Fore.MAGENTA+'Tout les Tool ont etais installer !. Appuyer sur entrée pour revenir Au Menu...')
  clear.clear()
  os.system('python3 linux-tool.py')
  
if "4" in choice.lower():
  sys.exit
  
  
else:
  print(Fore.CYAN+'Choix Non Disponible !')
  time.sleep(1)
  clear.clear()
  os.system('python3 sqlmap.py')
