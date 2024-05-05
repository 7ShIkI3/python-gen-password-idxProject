import string
import random
import re
import os
import platform

class Os:
    @staticmethod
    def get_os():
        """Fonction qui recupère la version de l'os utiliser pour adapter le programme a l'utilisateur

            exemple : Windows : Mdp_Historique\mdp.txt
                      Linux   : Mdp_Historique/mdp.txt
                      Mac     : Mdp_Historique/mdp.txt 

        """
        system = platform.system()
        if system == "Windows":
            return "Windows"
        elif system == "Mac":
            return "Mac"
        elif system == "Linux":
            return "Linux"
        else:
            return "Système d'exploitation inconnu"

class Parametre:
    @staticmethod
    def close():
        exit(0)
    
    @staticmethod
    def saute_ligne():
        print()

    @staticmethod  
    def affichage():
        print()
        print("_"*80)
        print()


class Application:
    def __init__(self) -> None:
        self.__password:str = None
        self.os = Os.get_os()
        self.site:str = None
        self.regex = r"^(?=.*[a-z]{2})(?=.*[A-Z]{2})(?=.*\d{2})(?=.*[!@#$%^&*()_+\-={}\[\]|\\:;\"'<>,.?/])(?=.*\s).{8,}$" #parametre qui par la suite pourra etre changer en fonction de la demande de l'utilisateur
    
    def getMdp(self):
        return self.__password

    def checkMdp(self):
        password = self.__password #recupere le mot de passe
        strength = 0
        remarks = ""
        lower_count = upper_count = num_count = wspace_count = special_count = 0

        for char in list(password):
            if char in string.ascii_lowercase:
                lower_count += 1
            elif char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == ' ':
                wspace_count += 1
            else:
                special_count += 1
        
        if lower_count >= 1:
            strength += 1
        if upper_count >= 1:
            strength += 1
        if num_count >= 1:
            strength += 1
        if wspace_count >= 1:
            strength += 1
        if special_count >= 1:
            strength += 1
        
        if strength == 1:
            remarks = "C'est un mot de passe très faible. Changez-le dès que possible."
        elif strength == 2:
            remarks = "C'est un mot de passe faible. Vous devriez envisager d'utiliser un mot de passe plus fort."
        elif strength == 3:
            remarks = "Votre mot de passe est correct, mais il peut être amélioré."
        elif strength == 4:
            remarks = "Votre mot de passe est difficile à deviner, mais vous pourriez le rendre encore plus sécurisé."
        elif strength == 5:
            remarks = "C'est un mot de passe extrêmement fort ! Les hackers n'ont aucune chance de deviner ce mot de passe !"
        
        print("Votre mot de passe contient : ")
        print(f"{lower_count} lettres minuscules", f"{upper_count} lettres majuscules", f"{num_count} chiffres", f"{wspace_count} espaces", f"{special_count} caractères spéciaux")
        print(f"Indice de force du mot de passe : {strength / 5}")
        print(f"Remarques : {remarks}")
        input()
        

    def saveMdp(self):
        if self.os == "Windows":
            try:
                with open("Mdp_Historique\mdp.txt", "a") as f:
                    f.write(f"{self.site}: {self.__password}\n")
            except:
                os.mkdir('Mdp_Historique')
                with open("Mdp_Historique\mdp.txt", "a") as f:
                    f.write(f"{self.site}: {self.__password}\n")
        elif self.os =="Linux" or self.os == "Mac":
            try:
                with open("Mdp_Historique/mdp.txt", "a") as f:
                    f.write(f"{self.site}: {self.__password}\n")
            except:
                os.mkdir('Mdp_Historique')
                with open("Mdp_Historique/mdp.txt", "a") as f:
                    f.write(f"{self.site}: {self.__password}\n")
        else:
            print("your device is not compatible")
            exit()

    def genMDP(self):
        """ 
            Fonction qui permet de generer un mot de passe
        """
        mdpValide = False
        while not mdpValide:
            longueur = 15 #nombre de caratère du mot de passe
            lettres = string.ascii_letters #recupère toutes les lettres ascii
            chiffres = string.digits #recupère tout les chiffres ascii
            caracteres_speciaux = string.punctuation #recupère tout les caratères spéciaux ascii
            code = lettres + chiffres + caracteres_speciaux + " " #reunifie tout les types de caractères autorisé
            mot_de_passe = ''.join(random.choice(code) for i in range(longueur)) #genere le mot de passe aléatoirement

            if re.match(self.regex, mot_de_passe): #verifie si le mots de passe verifie les restriction du regex
                self.__password = mot_de_passe
                mdpValide = True
                self.site = str(input("Entrez le nom du site : "))
                break #arrete la boucle while

def main():
    """
        Fonction qui permet de lancer le programme
    """
    app = Application()
    Parametre.affichage()
    print("Your OS : ",Os.get_os())
    Parametre.affichage()
    print("[A] Génerate Passeword")
    print("[B] Test Passeword")
    print("[X] Exit")

    choice = str(input("> "))
    if choice == "A":
        app.genMDP()
        Parametre.saute_ligne()
        print(app.getMdp())
        Parametre.saute_ligne()
        app.saveMdp()
        Parametre.saute_ligne()
        app.checkMdp()
        main()
    elif choice == "B":
        app.verifyMDP()
        main()
    else:
        while choice != "X":
            main()
        exit()

#execute le programme
if __name__ == "__main__":
        main()