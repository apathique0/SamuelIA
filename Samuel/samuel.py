import pyfiglet
from colorama import init, Fore, Style
init()
figlet = pyfiglet.figlet_format("Samuel AI")
print(figlet)

while True:
    with open("data.txt", "r+") as data:
        question = input(Fore.LIGHTRED_EX + "→ ")
        dt = data.readlines()
        if question:
            for lines in dt:
                if question in lines:
                    answer = lines[lines.find(':'):].replace(":", "")
                    print(Fore.RED + f"\n╚> Samuel : {answer}")
                    break
            if not question in lines:
                add = input(Fore.GREEN + "Veuillez ajouter une réponse à cette question : ")
                data.write(f"{question}:{add}\n")
                print(Fore.GREEN + Style.DIM + "Réponse ajoutée avec succès\n")