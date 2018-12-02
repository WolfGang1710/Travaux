
filename = 'lexique' # nom du fichier de traduction

def print_choices():
    """Affiche à l'écran les choix disponibles"""
    print('Choix disponibles :')
    print(" 1 - Traduire de l'anglais vers le français")
    print(" 2 - Traduire du français vers l'anglais")
    print(" 3 - Ajouter une traduction à la liste")
    print(" 4 - Nettoyer le fichier de traduction")
    print(" 0 - Quitter le programme")

def fileParser():
    """Parse le fichier de traduction pour en resortir un tableau composé de tableaux [en,fr]"""
    with open(filename,'r',encoding='utf-8') as file:
        fic = file.readlines()
    data = []
    for line in fic:
        if len(line)==0 or line[0]=="#":
            continue
        isFR = False
        j = 0
        fr = ""
        en = ""
        for i in range(0,len(line)):
            if line[i]==":":
                j = -1
                isFR = True
            elif line[i]=="\n":
                pass
            elif isFR:
                fr += line[i]
            else:
                en += line[i]
            j += 1
        data.append([en,fr])
    return data

def translate(choix):
    """Fonction pour rechercher la traduction d'un mot vers une langue. 
    La variable 'choix' doit être celle donnée dans le menu du programme (donc 1 ou 2)"""
    if choix == 1:
        result = 'français'
        result_column = 1
    else:
        result = 'anglais'
        result_column = 0
    print('Quel mot voulez-vous traduire en',result,'?')
    word = input('> ')
    translation = ''
    table = fileParser()
    for i in range(0,len(table)):
        if table[i][choix-1] == word:
            translation = table[i][result_column]
    if len(translation)>0:
        print("La traduction en",result,"de ce mot est",translation)
    else:
        print("Ce mot n'a pas été trouvé")

def addWord():
    """Demande la traduction d'un mot par l'utilisateur, et l'ajoute à la liste dans le fichier de traduction"""
    print("Entrez le mot dans sa version anglaise")
    en = input('> ')
    print("Et dans sa version française")
    fr = input('> ')
    with open(filename,'a',encoding='utf-8') as file:
        file.write(en+':'+fr+'\n')
    print("Traduction ajoutée !")

def clearFile():
    """Permet de nettoyer le fichier : trie les mots dans l'ordre alphabétique et supprime les lignes corrompues
    Il est possible d'ajouter des lignes ignorées en mettant un '#' au début de celle-ci"""
    data  = []
    errors = 0
    with open(filename,'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line[0]=='#':
                data.append(line[:-1])
            isfr = False
            fr = ''
            en = ''
            broken = False
            for char in line:
                if char == '\n':
                    continue
                if char == ':':
                    if isfr:
                        errors += 1
                        broken = True
                        break
                    isfr = True
                elif isfr:
                    fr += char
                else:
                    en += char
            if not broken:
                data.append(en.lower()+':'+fr.lower())
    with open(filename,'w',encoding='utf-8') as file:
        for line in sorted(data):
            file.write(line+'\n')
    print(str(len(data))+" lignes triées ! ("+str(errors)+" erreurs)")


def main():
    """Fonction principale du programme, qui demande le choix et lance la fonction associée"""
    while True:
        print_choices()
        choice = input('> ')
        if not choice.isnumeric():
            print('Choix invalide')
        else:
            choice = int(choice)
            if choice == 1 or choice == 2:
                translate(choice)
            elif choice == 3:
                addWord()
            elif choice == 4:
                clearFile()
            elif choice == 0:
                print("Au revoir !\n")
                break
            else:
                print('Choix invalide')
        print("")

main() # appel de la fonction principale
