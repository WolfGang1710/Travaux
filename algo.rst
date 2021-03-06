==============================
Introduction à l'algorithmique
==============================

--------------------------------
TD Eléments de base – Structures
--------------------------------


Exercices sur les pièces (#13)
------------------------------

**Consigne :** *Entrer des valeurs de pièces (0.1€, 0.2€, 0.5€, 1€, 2€).
Contrôler la saisie et arrêter quand la valeur de la pièce est nulle. Puis, constituer des rouleaux de 10 pièces de même valeur et des sacs de 20 rouleaux. Afficher alors, pour chaque type de pièces, le nombre de rouleaux, de sacs et de pièces non emballées.*


.. code-block:: ocaml

    PROGRAMME tic-tac-boum
    VARIABLES
        n1,n2,n5,n10,n20 : ENTIER  //nombre de pièces par montant
        r1,r2,r5,r10,r20 : ENTIER  //nombre de rouleaux
        s1,s2,s5,s10,s20 : ENTIER  //nombre de sacs
    DEBUT
        n2,n5,n10,n20 <- 0,0,0,0,0
        //on récupère le nombre de pièces de 0.1e
        ECRIRE("Nombre de pièces de 0.1€")  
        LIRE(n1)
        SI (n1<>0) ALORS :
            //idem pour les pièce de 0.2e
            ECRIRE("Nombre de pièces de 0.2€")
            LIRE(n2)
            SI (n2<>0) ALORS :
                //idem pour 0.5e
                ECRIRE("Nombre de pièces de 0.5€")
                LIRE(n5)
                SI (n5<>0) ALORS :
                    //idem pour 1e
                    ECRIRE("Nombre de pièces de 1€")
                    LIRE(n10)
                    SI (n10<>0) :
                        //idem pour 2e
                        ECRIRE("Nombre de pièces de 2€")
                        LIRE(n20)
                    FIN SI
                FIN SI
            FIN SI
        FIN SI
        
        //r1 récupère le nombre de rouleaux complets de 0.1 et n1 le reste, 
        // le tout grâce à une division euclidienne
        r1,n1 <- n1 DIV 10, n1 MOD 10
        //s1 récupère le nombre de sacs complets de 0.1e et r1 tout les rouleaux restants
        s1,r1 <- n1 DIV 10, n1 MOD 20
        //la suite des instructions est sur la même base, seuls les valeurs changent  
        r2,n2 <- n2 DIV 10, n2 MOD 10
        s2,r2 <- r2 DIV 10, r2 MOD 20
        r5,n5 <- n5 DIV 10, n5 MOD 10
        r5,n5 <- r5 DIV 10, r5 MOD 20
        r10,n10 <- n10 DIV 10, n10 MOD 10
        s10,r10 <- r10 DIV 10, r10 MOD 20
        r20,n20 <- n20 DIV 10, n20 MOD 10
        s10,r20 <- r20 DIV 10, r20 MOD 20

        //puis on affiche le résultat dans un texte sur plusieurs lignes
        ECRIRE("Il y a ",s1," sacs ",r1," rouleaux ",p1," pièces de 0.1€, \n",
			s2," sacs ",r2," rouleaux ",p2," pièces de 0.2€, \n",
			s5," sacs ",r5," rouleaux ",p5," pièces de 0.5€, \n",
			s10," sacs ",r10," rouleaux ",p10," pièces de 1€, et \n",
			s20," sacs ",r20," rouleaux ",p20," pièces de 2€")
    FIN

Plusieurs améliorations sont possible, comme par exemple créer une fonction qui retourne le nombre de rouleaux et de sacs possibles à partir du nombre de pièces, ou utiliser une boucle POUR afin de réduire la taille du premier bloc de code, comme ceci :

.. code-block:: ocaml

    [...]
    DEBUT
        n2,n5,n10,n20 <- 0,0,0,0,0
        POUR i DANS [(n1,0.1),(n2,0.2),(n3,0.5),(n4,1),(n5,2)] FAIRE :
            ECRIRE("Nombre de pièces de ",i[1],"€")
            LIRE(i[0])
            SI (i[0]=0) ALORS:
                BREAK
        [...]


Exercice de l’horloge (#14)
---------------------------

**Consigne :** *Créer un compte à rebours (heures, minutes, secondes) qui affichera «boum» à 00:00:00*


.. code-block:: ocaml

    PROGRAMME tic-tac-boum
    VARIABLES
        h,m,s : ENTIER  //heures, minutes et secondes restantes
    DEBUT
        ECRIRE("Saisissez le temps restant (heures, minutes et secondes) : ")
        LIRE(h,m,s)
        TANT QUE (h<>0 OU m<>0 OU s<>0) :  //tant qu'il reste du temps
            s <- s-1
            SI (s<0 ET (m>0 OU h>0) ALORS :  //si la minute est terminée
                m <- m-1    
                s <- 59
                SI (m<0 ET h>0) ALORS :  //si l'heure est terminée
                    h <- h-1
                    m <- 59
                FIN SI
            FIN SI
            ECRIRE(h,":",m,":",s)
        FIN TANT QUE  //fin du décompte
        ECRIRE("BOUM !")
    FIN

On pourra éventuellement ajouter avant la boucle TANT QUE une sécurité permettant d'empêcher un nombre supérieur à 59 de minutes ou de secondes : 

.. code-block:: ocaml

    TANT QUE (s>59) :
        s <- s-60
        m <- m+1
    FIN TANT QUE
    TANT QUE (m>59) :
        m <- m-60
        h <- h+1
    FIN TANT QUE

Enfin, pour plus de réalisme, il est possible d'ajouter une instruction demandant au code d'attendre une seconde, dans la boucle TANT QUE. Cela permettra d'attendre une seconde entre deux décomptes, au lieu de tout afficher quasi-instantanément.

PGCD
----

**Consigne :** *Ecrire une fonction permettant de calculer le plus grand diviseur commun de deux entiers naturels.*

.. code-block:: ocaml

    FONCTION PGCD(a:INT, b:INT) :INT
    VAR I,m : INT
    DEBUT
        m = 0
        POUR I DE 1 A a:
            SI (a MOD I = 0) ET (b MOD I = 0) ALORS:
                m <- I        
	        FIN SI
        FIN POUR
        RETOURNER(m)
    FIN


    PROGRAMME pgcd
    VAR x,y,r : ENTIER
    DEBUT
        ECRIRE("Saisissez les deux entiers positifs")
        LIRE(x,y)
        r <- PGCD(x,y)
        ECRIRE("Le PGCD de ",x," et ",y," est ",r)
    FIN



---------------------------
TD Structures - Les classes
---------------------------


Résolution du second degré
--------------------------

**Consigne :** *Définir en algorithmique, une structure nommée Eq2D qui permet de définir l'ensemble des solutions d'une équation du second degré.*


.. code-block:: ocaml

    TYPE
    STRUCTURE Eq2D
        r_one:float //première racine
        r_two:float //deuxième racine
        delta:float
        
        PROCEDURE calc (self,a:float, b:float, c:float)
        DEBUT
            self.delta <- b**2 - 4*a*c
            SI self.delta < 0 ALORS
                self.r_one,self.r_two = None
            SINON SI self.delta > 0 ALORS
                self.r_one <- (-b-sqrt(self.delta))/(2*a)
                self.r_two <- (-b+sqrt(self.delta))/(2*a)
            SINON
                self.r_one,self.r_two <- -b/(2*a)
            FIN SI
        FIN

    PROGRAMME superSoluce
    VAR a,b,c:float
	    s:Eq2D
    DEBUT
    	ECRIRE("Entrez les coefficients")
    	SAISIR(a,b,c)
    	s.calc(a,b,c)
    	ECIRE("Les deux solutions sont",s.r_one,"et",s.r_two)
	FIN

On peut aussi définir une fonction qui va calculer ces racines, au lieu d'un programme : 

.. code-block:: ocaml

    FONCTION superSoluce (a:float, b:float, c:float) : Eq2D
    VAR s:Eq2D
    DEBUT
        s.calc(a,b,c)
	    RETOURNER(s)
    FIN


Opérations complexes
--------------------

**Consigne :** *Ecrire deux fonctions qui permettent de passer un nombre complexe de sa forme algébrique à sa forme exponentielle, puis d'additionner deux complexes sous leur forme algébrique.*

.. code-block:: ocaml
	
    TYPE
        STRUCTURE algComplex
            reel:float
            img:float
    
        STRUCTURE expComplex
            arg:float
            modul:float


    FONCTION switch(a:algComplex) : expComplex //passer de la forme algébrique à la forme exponentielle
    VAR x:expComplex
        acos:float  //angle trouvé par cosinus
	    asin:float //angle trouvé par sinus
    DEBUT
        x.modul <- sqrt(a.reel**2 + a.img**2)
        t_one <- arccos(a.reel/x.modul)/pi
        t_two <- arcsin(a.img/x.modul)/pi
        SI -t_one <- t_two ALORS:  //si l'angle trouvé par cosinus est l'opposé de l'angle trouvé par sinus
            x.arg <- t_two  //l'angle final prend la valeur du sinus
        SINON:
            x.arg <- arccos(cos(-t_one))  //l'ange final prend la valeur de l'angle dont le cosinus est l'opposé du sinus
        FIN SI
        RETOURNER(x)
    FIN

    FONCTION switch2(a:expComplex) : algComplex //passer de la forme exponentielle à la forme algébrique
    VAR x:algComplex
    DEBUT
        x.reel = a.modul*cos(a.arg)
	    x.img = a.modul*sin(a.arg)
	    RETOURNER(x)
    FIN

    FONCTION algAdd(a:algComplex, b:algComplex) : algComplex //additionner deux formes algébriques
    VAR x:algComplex
    DEBUT
        x.reel <- a.reel + b.reel  //on additionne les réels
        x.imaginaire <- a.imaginaire + b.imaginaire //on additionne les imaginaires
        RETOURNER(x)
    FIN
    
    FONCTION expAdd(a:expComplex, b:expComplex) : expComplex //additionner deux formes exponentielles
    VAR alga:algComplex //a, sous forme algébrique
	algb:algComplex //idem pour b
	algsomme:algComplex //la somme sous forme algébrique
    DEBUT
        alga <- switch2(a)
	    algb <- switch2(b)
	    algsomme <- algAdd(alga,algb)
	    RETOURNER(switch(aglsomme))
    FIN
	

Je ne suis pas sûr de la formule pour calculer l'argument d'un complexe à partir de sa valeur algébrique, mais après tout... c'est un cours d'informatique, pas de maths, n'est-ce pas ?

--------------
TD Récursivité
--------------

Factorielle itérative
---------------------

**Consigne :** *Créer une fonction qui calcule la factorielle d'un nombre en utilisant une itération.*

.. code-block:: ocaml

    FONCTION fact (n:int) : int
    VAR i:int //itération
        s:int //total
    DEBUT
        s <- 1
        POUR i de 1 à n:
            s <- s*i
        FIN POUR
            RETOURNER(s)
    FIN

Division euclidienne
--------------------

**Consigne :** *Écrire deux fonctions récursives qui calculent  le  quotient et le reste de la division entière de deux nombres strictement positifs.*


.. code-block:: ocaml

    FONCTION quotient(a,b,c,i:int) : int
    VAR r:int //résultat
    DEBUT
        SI a<i OU b<i ALORS
            RETOURNER(c)
        SINON SI a*i<=b OU b*i<=a ALORS
            c <- i
        FIN SI
        r <- Quotient(a,b,c,i+1)
        RETOURNER(r)
    FIN
    
    FONCTION reste(a,b,c,i:int) : int
    VAR r:int //résultat
    DEBUT
        SI a<i OU b<i ALORS
            RETOURNER(c)
        SINON SI a*i<=b OU b*i<=a ALORS
            c <- ABS(MIN(a*i-b , b*i-a))
        FIN SI
        r <- Reste(a,b,c,i+1)
        RETOURNER(r)
    FIN
	
Palindromes
-----------

**Consigne :** *Écrire un algorithme récursif qui permet de vérifier si une chaîne de caractères est un palindrome ou non.*

.. code-block:: ocaml

    FONCTION palindrome(text:string, n:int) : bool
    DEBUT
        text <- REPLACE(text," ","")
        SI n > len(text)/2 ALORS
            RETOURNER(Vrai)
        SINON SI text[n]=text[-n-1] ALORS
            RETOURNER(Palindrome(text,n+1)
        SINON
            RETOURNER(Faux)
        FIN SI
    FIN

On suppose que la fonction REPLACE prend en paramètre trois chaines de caractères et retourne une copie de la chaîne de caractères dans laquelle les occurrences de la deuxième ont été remplacées par la troisième.

Miroir
------

**Consigne :** *Écrire  un algorithme  récursif qui  permet  de réaliser cette fonction, et puis proposer une version itérative équivalente.*

Fonction récursive : 

.. code-block:: ocaml

    FONCTION miroir(text:string, n:int, rep:string) : string
    DEBUT
        SI n = len(text) ALORS
            RETOURNER(rep)
        FIN SI
        rep <- text[n]+rep
        RETOURNER(Miroir(text,n+1,rep))
    FIN


Fonction itérative :

.. code-block:: ocaml

    FONCTION miroir2(text:string) : string
    VAR i:int //itération
        rep:string //résultat
    DEBUT
        POUR i DANS text:
            rep <- i+rep
        FIN POUR
        RETOURNER(rep)
    FIN


Power
-----

**Consigne :** *Écrire la fonction récursive puissance qui calcule n^k de façon naïve en considérant que n^k= n*n(k-1) et que n^0 = 1*


.. code-block:: ocaml
    
    FONCTION naive(n,k,i : int) : int
    DEBUT
        SI k=0 ALORS
            RETOURNER(1)
        SINON SI i<k-1 ALORS
            RETOURNER(Naive(n,k,i+1)*n
        SINON
            RETOURNER(n)
        FIN SI
    FIN

*Puis la même fonction, en récursion terminale.*

.. code-block:: ocaml

    FONCTION term(n,k,acc : int) : int
    DEBUT
        SI k=0 ALORS
            RETOURNER(acc)
        SINON
            RETOURNER(Term(n,k-1,acc*n))
        FIN SI
    FIN

*Puis par dichotomie.*

.. code-block:: ocaml

    FONCTION puissance-dic(n,k,i : int) : int
    DEBUT
        SI k=0 ALORS
            RETOURNER 1
        SINON SI k MOD 2 = 0 ALORS
            SI i*2 = k ALORS
                RETOURNER((n*n)^(1/2))
            SINON
                RETOURNER(puissance-dic(n,k,i+1)^2)
            FIN SI
        SINON
            SI i = k-1 ALORS
                RETOURNER(n)
            SINON
                RETOURNER(puissance-dic(n,k,i+1)*n)
            FIN SI
        FIN SI
    FIN

Parité
------

**Consigne :** *Un nombre n est pair si n-1 est impair, et un nombre n est impair si n-1 est pair. Partant de cette définition, créez deux fonctions récursives pair(n) et impair(n) qui permettent ensemble de savoir si un nombre entré est pair ou impair.*

.. code-block:: ocaml

    FONCTION pair(n,i=0 : int) : bool
    DEBUT
        SI i=n
            RETOURNER(True)
        SINON
            RETOURNER(impair(n,i+1))
        FIN SI
    FIN
    
    FONCTION impair(n,i=0 : int) : bool
    DEBUT
        SI i=n
            RETOURNER(False)
        SINON
            RETOURNER(pair(n,i+1))
        FIN SI
    FIN

Une autre méthode permet cependant d'écrire ce code en une seule fonction :

.. code-block:: ocaml

    FONCTION pair(n,i=0 : int ,c=True : bool) : bool
    DEBUT
        SI i=n ALORS
            RETOURNER(c)
        SINON
            RETOURNER(n,i-1,not c)
        FIN SI
    FIN



---------------------------
TD Unix - Commandes de base
---------------------------

Exercice 1
----------

a.  

.. code-block:: bash
    
        $ echo $PATH $PS1
    /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games 
    \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ 
        
        $ export PS1="linux on en veux encore # > "

        #On peut même changer la couleur !
        $ export PS1="\e[0;36m\! - linux on en veux encore # > \e[m"

        $ export PS1="\e[0;36m\!\e[m - \e[0;32m\w # \e[m"

c. La commande :code:`man ls` fonctionne, et affiche un beau pavé de texte explicatif.



.. code-block:: bash

        $ cal 10 2018
        Octobre 2018      
    di lu ma me je ve sa  
        1  2  3  4  5  6  
     7  8  9 10 11 12 13  
    14 15 16 17 18 19 20  
    21 22 23 24 25 26 27  
    28 29 30 31    

        $ who
    blaisearth tty2         2018-10-24 10:40 (:1)
        $ whoami
    blaisearth

f. La commande :code:`stty -echo` permet de rentrer du texte sans l'afficher à l'écran, comme par exemple un mot de passe.

g. On peut confirmer, :code:`stty echo` nous permet de voir à nouveau les commandes entrées. C'est plus partique pour continuer le TP...


.. code-block:: bash

        $ xterm -hc blue -bg cyan -fg brown

        $ which python3
    /usr/bin/python3

        $ alias hop=ls`

        $ alias rs="rm -i"

        $touch test.txt
        $rm test.txt
    rm : supprimer fichier vide 'test.txt' ? y


Exercice 2
----------

.. code-block:: bash

        $ emacs
        #appui sur les touches Ctrl-Z
        $ bg
        
        $ sleep 60
        #Cette commande demande au processus en cours d'attendre 60 secondes sans rien faire.
        #Pour l'interrompre, il suffit d'appuyer sur les touches Ctrl-C
        
        $ ps
      PID TTY          TIME CMD
     5092 pts/0    00:00:00 bash
     5159 pts/0    00:00:00 emacs
     5202 pts/0    00:00:00 ps
        $ kill 5159
        
Exercice 3
----------

.. code-block:: bash

        $ pwd
    /cergy/homee/b/blaisearth
        $ cd /
        $ ls
    bin    dev   initrd.img      lib64       mnt   root  srv  usr      vmlinuz.old
    boot   etc   initrd.img.old  lost+found  opt   run   sys  var      vms
    cergy  home  lib             media       proc  sbin  tmp  vmlinuz
        $ cd ~
        $ mkdir Prepal
        $ mkdir Prepal/Info
        $ cd Prepal/info
        $ mkdir tmp
        $ cd tmp
        $ touch toto
        $ $ find ../.. | sed 's/[^/]*\//| /g;s/| *\([^| ]\)/+--- \1/'
    +--- ..
    | +--- Info
    | | +--- tmp
    | | | +--- toto
        $ cd ..
        $ rmdir tmp
    rmdir: impossible de de supprimer 'tmp': Le dossier n est pas vide
        $ rm -r tmp
        
        $ head -n 15 lorem.txt
    [...]
        $ head -n 9 lorem.txt >temp.txt
        $ tail -n 5 temp.txt >temp2.txt
        $ head -n 13 lorem.txt >temp.txt
        $ tail -n 1 temp.txt >temp3.txt
        $ cat temp2.txt temp3.txt >final.txt
        
        $ cat final.txt
        $ more final.txt
        #Aucune différence visible
        
        $ mkdir tmp
        $ cp final.txt tmp/
        
        $ cd tmp
        $ cp final.txt "lorem en ipsum".txt
        $ mv final.txt ~/.local/share/Trash/files #Corbeille de l ordinateur
        $ mv "lorem en ipsum.txt" ~/
        $ ls ~/
    Bureau     Images              Modèles  Prepal  Téléchargements  VirtualBox VMs
    Documents  lorem en ipsum.txt  Musique  Public  Vidéos
    
        $ ln -s "/cergy/homee/b/blaisearth/lorem_en_ipsum.txt" ipsum
        $ ls -A --author -F -h -H -i -s
        $ ls -l
    total 1
    lrwxrwxrwx 1 blaisearth users 44 oct.  24 12:28 ipsum -> /cergy/homee/b/blaisearth/lorem_en_ipsum.txt
        $ rm ~/lorem_en_ipsum.txt
        $ ls -l
        #La direction de l'alias est colorée en rouge, annoncant que le lien est rompu
        


-----------------------
TD Binaire - Complexité
-----------------------

Quel serait l'intervalle réel représentable par un codage hypothétique en « quadruple précision », c'est à dire en 128 bits ?

Sur 128 bits, selon la norme IEEE 754, l'exponentielle est codée sur 15 bits et la mantisse sur 113 bits. Pour éviter d'avoir des nombres trop longs, nous travaillerons avec la base 16.

Les valeurs minimales et maximales de l'exponentielle sont donc celles que nous pouvons coder le mieux sur 15 bits, soient :math:`0001_{(16)} − 3FFF_{(16)} = −16382(10)` et :math:`7FFE_{(16)} − 3FFF_{(16)} = 16383_{(10)}`.

De là, pour obtenir la plus petite valeur positive, il suffit de calculer :math:`2^{−16382}` (car on considère la mantisse à 0), soit environ :math:`3.36 × 10^{−4932}`.
La valeur maximale est calculée avec une exponentielle à 16383, et une mantisse à :math:`2^{112}`, ce qui donne :math:`2^{16383} × (2 − 2^{−112}) = 1.19 × 10^{4932}`.

Les bornes des réels représentables par un codage en quadruple précision, aussi appelé binary128, sont donc approximativement :math:`3.36 × 10^{−4932}` et :math:`1.19 × 10^{4932}` pour la partie positive. Pour la partie négative, il suffit de les multiplier par -1.


Comparaisons et affectations
----------------------------

Voici une fonction pour vérifier si une liste est triée (peu importe l'ordre), et une procédure pour insérer une valeur dans une liste triée en ordre croissant.

.. code-block:: pas

    function check(A:intArray) : boolean;
    var i:integer;
    begin
        check := True;
        for i:=0 to high(A)-2 do
            check := check and ((A[i]-A[i+1]) * (A[i+1]-A[i+2]) >= 0);
    end;

    procedure Insert(var A:intArray;val:integer);
    var i:integer;
        temp:intArray;
    begin
        i := 0;
        SetLength(temp,length(A)+1);
        while A[i] < val do begin
            temp[i] := A[i];
            i := i+1;
        end;
        temp[i] := val;
        while i < high(A)+1 do begin
            temp[i+1] := A[i];
            i := i+1;
        end;
        A := temp;
    end;


----------------
Maths Appliquées
----------------

Cryptage César
--------------

Voilà comment crypter un message via le code César, en python. Pour le décrypter, il suffit de rentrer l'opposé de la clé (-3 pour Cicéron par exemple).

.. code-block:: python

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Clé de cryptage

    def crypte(sent,key=10): # fonction à appeler
        answer = ''
        for i in sent.upper(): # on mélange majuscules et minuscules
            if i in alpha: # si le caractère est dans la clé
                answer += alpha[(alpha.index(i)+key)%26]
            else: # sinon (comme un espace ou une ponctuation)
                answer += i
        return answer
