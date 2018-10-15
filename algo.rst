==========================================
Algorithmique et programmation procédurale
==========================================

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
        RETURN m
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
            self.delta = b**2 - 4*a*c
            SI self.delta < 0 ALORS
                self.r_one,self.r_two = None
            SINON SI self.delta > 0 ALORS
                self.r_one = (-b-sqrt(self.delta))/(2*a)
                self.r_two = (-b+sqrt(self.delta))/(2*a)
            SINON
                self.r_one,self.r_two = -b/(2*a)
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
        x.modul = sqrt(a.reel**2 + a.img**2)
        t_one = arccos(a.reel/x.modul)/pi
        t_two = arcsin(a.img/x.modul)/pi
        SI -t_one = t_two ALORS:  //si l'angle trouvé par cosinus est l'opposé de l'angle trouvé par sinus
            x.arg = t_two  //l'angle final prend la valeur du sinus
        SINON:
            x.arg = arccos(cos(-t_one))  //l'ange final prend la valeur de l'angle dont le cosinus est l'opposé du sinus
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
        x.reel = a.reel + b.reel  //on additionne les réels
        x.imaginaire = a.imaginaire + b.imaginaire //on additionne les imaginaires
        RETOURNER(x)
    FIN
    
    FONCTION expAdd(a:expComplex, b:expComplex) : expComplex //additionner deux formes exponentielles
    VAR alga:algComplex //a, sous forme algébrique
	algb:algComplex //idem pour b
	algsomme:algComplex //la somme sous forme algébrique
    DEBUT
        alga = switch2(a)
	algb = switch2(b)
	algsomme = algAdd(alga,algb)
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
        s = 1
        POUR i de 1 à n:
	    s = s*i
	RETOURNER(s)
    FIN
