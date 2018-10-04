==========================================
Algorithmique et programmation procédurale
==========================================

--------------------------------
TD Eléments de base – Structures
--------------------------------

**Consigne :** *Entrer des valeurs de pièces (0.1€, 0.2€, 0.5€, 1€, 2€).*
Contrôler la saisie et arrêter quand la valeur de la pièce est nulle. Puis, constituer des rouleaux de 10 pièces de même valeur et des sacs de 20 rouleaux. Afficher alors, pour chaque type de pièces, le nombre de rouleaux, de sacs et de pièces non emballées.


.. code-block:: ocaml

    PROGRAMME tic-tac-boum
    VARIABLES
        n1,n2,n5,n10,n20 : ENTIER  //nombre de pièces par type
        r1,r2,r5,r10,r20 : ENTIER  //nombre de rouleaux
        s1,s2,s5,s10,s20 : ENTIER  //nombre de sacs
    DEBUT
        n2,n5,n10,n20 <- 0,0,0,0,0
        //on récupère le nombre de pièces de 0.1e
        ECRIRE("Nombre de pièces de 0.1€")  
        LIRE(p1)
        SI (p1<>0) ALORS:
            //idem pour les pièce de 0.2e
            ECRIRE("Nombre de pièces de 0.2€")
            LIRE(p2)