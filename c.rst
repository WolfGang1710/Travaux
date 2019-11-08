=================
Introduction au C
=================

-----------------------
TD 1 : Entrées, sorties
-----------------------


Exercice 9 : Minimum et maximum
-------------------------------

**Consigne :** *Écrire une méthode permettant de saisir une liste de n réels et de calculer et d’afficher les valeurs minimale et maximale de cette liste.*


.. code-block:: c

    /*!
    \fn void ex9(void)
    \brief Code de l'exercice 9
    \return rien
    */
    void ex9() {
        int int_min, int_max;   // minimum et maximum
        int int_n;              // nombre de cases
        int i;                  // iterateur
        printf("Entrez le nombre de cases à remplir, entre 1 et 50: ");
        scanf("%d",&int_n);
        if ((int_n < 1) || (int_n > 50)) { // si N dépasse les bornes
            printf("Nombre invalide");
            return;
        }
        int liste[int_n];
        for (i = 0; i < int_n; ++i) { // on construit la liste avec les entrees de l'utilisateur
            scanf("%d",&liste[i]);
            if (i==0) { // initialisation du min et du max avec une valeur de la liste
                int_min = liste[i];
                int_max = liste[i];
            }
            else { // recherche du min et du max dans le reste de la liste
                if (int_min > liste[i]) {
                int_min = liste[i];
            };
            if (int_max < liste[i]) {
                int_max = liste[i];
            };
            }
        };
        printf("Minimum : %d - Maximum : %d", int_min, int_max);
    }


------------------
TD 4 : Vecteurs 2D
------------------


Exercice : Puissance 4
----------------------

**Consigne :** *Ben... créer un puissance 4 avec une matrice (donc un vecteur de vecteurs). La taille est définie dans une constante symbolique notée N. Le plateau de jeu est noté :code:`ttint_plateau[i][i]`, avec i pour le numéro de colonne et j le numéro de ligne.*

Extrait de code 1 : vérifier l'état actuel du jeu, si un joueur a gagné ou si ex-aequo (toutes les cases sont occupées), ou si on continue de jouer. J'ai défini les fonctions :code:`checkDiag1`, :code:`checkDiag2` etc. à côté, elles renvoient chacune d'entre elles le nombre de pions alignés io en fonction de la coordonnée donnée.

.. code-block:: c

    int aGagne(int PLATEAU) {
        if (plateauRempli(ttint_plateau)) {
            return(0);
        }
        for (int int_joueur=1; int_joueur<3; int_joueur++) {
            for (int int_increment=0; int_increment<N; int_increment++) {
                if (checkDiag1(ttint_plateau, int_increment, int_joueur) > 3) {
                    return(int_joueur);
                }
                if (checkDiag2(ttint_plateau, int_increment, int_joueur) > 3) {
                    return(int_joueur);
                }
                if (checkColonne(ttint_plateau, int_increment ,int_joueur) > 3) {
                    return(int_joueur);
                }
                if (checkLigne(ttint_plateau, int_increment, int_joueur) > 3) {
                    return(int_joueur);
                }
            }
        }
        return(-1);
    }
    
Extrait de code 2 : l'affichage du plateau. En vrai il n'y a pas grand chose de compliqué, il suffit de ne pas s'emmêler avec les indices et les boucles. Mais c'est joli donc woala.

.. code-block:: c

    void affichage(int PLATEAU) {
        int i;
        int j;
        printf("+");
        for (j=0;j<N;j++) {
            printf("---+");
        }
        for (j=0;j<N;j++) {
            printf("\n|");
            for (i=0;i<N;i++) {
                switch (ttint_plateau[i][j]) {
                    case 1:
                        printf(" O |");
                        break;
                    case 2:
                        printf(" X |");
                        break;
                    default:
                        printf("   |");
                        break;
                }
            }
            printf("\n+");
            for (i=0;i<N;i++) {
                printf("---+");
            }
        }
        printf("\n+");
        for (i=0;i<N;i++) {
            printf(" %d +",i+1);
        }
        printf("\n");
    }
    
Extrait de code 3 : le retournement du plateau à 90° (pi/2 pour les intimes). Le plus compliqué est le retournement en lui-même, surtout si l'on souhaite une fonction modulable et courte. Mais j'ai réussi en 30 lignes, je suis content. La base de d'algo vient d'`ici <https://forum.hardware.fr/hfr/Programmation/Algo/algo-rotation-matrice-sujet_63972_1.htm>`_.

.. code-block:: c

    void gravite(int PLATEAU) {
        int i,j,k;
        for (i=0; i<N; i++) {
            k = N-1;
            for (j=N-1;j>=0;j--) {
                if (ttint_plateau[i][j] > -1) {
                    if (ttint_plateau[i][k] == -1) {
                    ttint_plateau[i][k] = ttint_plateau[i][j];
                    ttint_plateau[i][j] = -1;
                    }
                    k--;
                }
            }
        }
    }

    void rotationPlateau(int PLATEAU) {
        int i,j;
        for (j=0; j<N-2; j++)
        {
            for (i=j; i <N-j-1; i++)
            {
                int temp = ttint_plateau[i][j];
                ttint_plateau[i][j] = ttint_plateau[j][N-i-1];
                ttint_plateau[j][N-i-1] = ttint_plateau[N-i-1][N-j-1];
                ttint_plateau[N-i-1][N-j-1] = ttint_plateau[N-j-1][i];
                ttint_plateau[N-j-1][i] = temp;
            }
        }
        gravite(ttint_plateau);
    }
