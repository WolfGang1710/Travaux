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
