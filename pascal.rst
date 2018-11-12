======
Pascal
======

Voici la page où je mettrai quelques travaux codés en Pascal. Ni plus ni moins.

----------
Premier TP
----------

.. code-block:: pas

    (*
     ------------------------------------------------------------------------------------
     -- Fichier           : TP1.pas
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 13:20:06 2017
     --
     -- But               : Premier TP
     -- Remarques         : Aucune
     -- Compilation       : fpc
     -- Edition des liens : fpc
     -- Execution         : shell
     ------------------------------------------------------------------------------------
     *)
    PROGRAM Tp1;
    
    (*
     ------------------------------------------------------------------------------------
     -- Fonction          : LireEntier() : Integer
     -- Auteur            :
     -- Date de creation  :
     --
     -- But               : Lire un entier
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Lire un entier
     ------------------------------------------------------------------------------------*)
    FUNCTION LireEntier() : Integer;
    VAR
       resultat : Integer;
    BEGIN
        write('>>> ');
        read(resultat);
        LireEntier := resultat;
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Fonction          : Max4(nb1, nb2, nb3, nb4 : Integer) : Integer
     -- Auteur            :
     -- Date de creation  :
     --
     -- But               : Retourne le maximum de 4 nombres
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : retourne le plus grand des nombres passés en paramètre
     ------------------------------------------------------------------------------------*)
    FUNCTION Max4(nb1, nb2, nb3, nb4 : Integer) : Integer;
    BEGIN
        if (nb1>=nb2) and (nb1>=nb3) and (nb1>=nb4) then
        BEGIN
            Max4 := nb1
        END;
        if (nb2>=nb1) and (nb2>=nb3) and (nb2>=nb4) THEN
        BEGIN
            Max4 := nb2
        End;
        if (nb3>=nb1) and (nb3>=nb2) and (nb3>=nb4) then
        BEGIN
            Max4 := nb3
        END;
        if (nb4>=nb1) and (nb4>=nb2) and (nb4>=nb3) then
        BEGIN
            Max4 := nb4
        END;
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AfficheMax4()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:12:09 2017
     --
     -- But               : Afficher le maximum de 4 nombre
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Afficher le maximum de 4 nombre
     ------------------------------------------------------------------------------------*)
    PROCEDURE AfficheMax4();
    VAR
       nb1, nb2, nb3, nb4 : Integer;
    BEGIN
       nb1 := LireEntier();
       nb2 := LireEntier();
       nb3 := LireEntier();
       nb4 := LireEntier();
       writeln('Le maximum de ', nb1, ', ', nb2, ', ', nb3, ' et ', nb4, ' est : ', Max4(nb1, nb2, nb3, nb4));
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AfficheBissextile()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:25:52 2017
     --
     -- But               : Affiche si une année est bissextile
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Affiche si une année est bissextile
     ------------------------------------------------------------------------------------*)
    PROCEDURE AfficheBissextile();
    VAR
        year :Integer;
    BEGIN
        year := LireEntier();
        if ((year MOD 4 = 0) and (year MOD 100 <> 0)) or (year MOD 400 = 0) THEN
            writeln(year,' est bissextile !')
        else
            writeln(year,' n''est pas bissextile')
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AffichePGCD()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:26:28 2017
     --
     -- But               : Calcule et affiche le pgcd de deux nombres
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Calcule et affiche le pgcd de deux nombres
     ------------------------------------------------------------------------------------*)
    PROCEDURE AffichePGCD();
    VAR
        a,b,i,m : Integer;
    BEGIN
        m := 1;
        a := LireEntier();
        b := LireEntier();
        for i:=1 TO a DO
        BEGIN
            if (a MOD i = 0) and (b MOD i = 0) then
                if (i>m) then
                    m := i
            ;
        END;
        writeln('Le PGCD de ',a,' et ',b,' est ',m);
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Fonction         : Power()
     -- Auteur            : Moi
     -- Date de creation  : Wed Nov 7 11:33:05 2018
     --
     -- But               : Retourne a élevé à la puissance b
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : ¯\_(ツ)_/¯
     ------------------------------------------------------------------------------------*)
    FUNCTION Power(a,b:Integer) : Integer;
    VAR
        n : Integer;
        sum : Integer;
    BEGIN
        sum := 1;
        for n:=1 to b do
            sum := sum*a;
        Power := sum;
    END;
    
    PROCEDURE AfficherPower();
    VAR
        s:Integer;
    BEGIN
        s := Power(LireEntier(),LireEntier());
        writeln('Résultat : ',s);
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AffichePiEuler()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:27:05 2017
     --
     -- But               : Affiche et calcule pi par la méthode d'Euler
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Affiche et calcule pi par la méthode d'Euler
     ------------------------------------------------------------------------------------*)
    PROCEDURE AffichePiEuler();
    VAR
        p : Real;
        n,x,a : Integer;
    BEGIN
        p := 0;
        writeln('Entrez le degré de précision');
        n := LireEntier();
        for x := 1 to n do
        BEGIN
            a := Power(x,2);
            p := p+ 1/a;
        END;
        writeln('check');
        writeln(sqrt(p*6))
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AffichePiLeibniz()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:27:42 2017
     --
     -- But               : Affiche et calcule Pi par la méthode de Leibniz
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Affiche et calcule Pi par la méthode de Leibniz
     ------------------------------------------------------------------------------------*)
    PROCEDURE AffichePiLeibniz();
    VAR
        n,x : Integer;
        temp : Real;
        cond : boolean;
    BEGIN
        cond := True;
        writeln('Entrez le degré de précision');
        n := LireEntier();
        temp := 0;
        for x:=1 to n do
            BEGIN
                IF (x MOD 2 = 1) THEN
                BEGIN
                IF cond THEN
                    temp := temp + 1/x
                ELSE
                    temp := temp - 1/x
                ;
                cond := not cond;
                END;
            END;
        writeln(temp*4)
    END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : AfficheMenu()
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 13:25:58 2017
     --
     -- But               : Affiche le menu du TP
     -- Remarques         : Aucune
     -- Pré conditions    : Aucune
     -- Post conditions   : Affiche le menu du TP
     ------------------------------------------------------------------------------------*)
    PROCEDURE AfficheMenu();
    BEGIN
       writeln('1 : afficher le maximum de 4 nombres');
       writeln('2 : affiche si une année est bissextile');
       writeln('3 : affiche le PGCD de deux nombres');
       writeln('4 : calcul de PI par la méthode d''Euler');
       writeln('5 : calcul de PI par la méthode de Leibniz');
       writeln('6 : calcul d''une puissance');
       writeln('');
       writeln('0 : Quitter');
        END;
    
    (*
     ------------------------------------------------------------------------------------
     -- Procedure         : effectueActionMenu(choix : Integer)
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 14:20:19 2017
     --
     -- But               : Lance les actions correspondantes par rapport au choix de l'utilisateur
     -- Remarques         : Si choix vaut 0 alors on affiche un message de sortie
     -- Pré conditions    : 0 <= choix < 6
     -- Post conditions   : Lance les actions correspondantes par rapport au choix de l'utilisateur
     ------------------------------------------------------------------------------------*)
    PROCEDURE effectueActionMenu(choix : Integer);
    BEGIN
       CASE choix OF
         1 : AfficheMax4();
         2 : AfficheBissextile();
         3 : AffichePGCD();
         4 : AffichePiEuler();
         5 : AffichePiLeibniz();
         6 : AfficherPower();
       ELSE
            writeln('');
            writeln('Bye');
       END;
    END;

    (*
     ------------------------------------------------------------------------------------
     -- Fonction          : SaisirChoix() : Integer
     -- Auteur            : Florent Devin <fd@eisti.eu>
     -- Date de creation  : Mon Nov 13 13:32:14 2017
     --
     -- But               : Permet la saisie d'un choix pour le menu
     -- Remarques         : Le nombre retourné est compris : 0 <= x < 6
     -- Pré conditions    : Aucune
     -- Post conditions   : Permet la saisie d'un choix pour le menu
     ------------------------------------------------------------------------------------*)
    FUNCTION SaisirChoix() : Integer;
    VAR
       choix : Integer;
    BEGIN
       REPEAT
          AfficheMenu();
          writeln('');
          writeln('Entrez votre choix : ');
          readln(choix);
       UNTIL ((choix >= 0) and (choix < 7));
       SaisirChoix:=choix;
    END;

    VAR
       choix : Integer;
    (*Début du programme principal*)
    BEGIN
       REPEAT
          choix:=SaisirChoix();
          effectueActionMenu(choix);
          (* Ou aussi effectueActionMenu(SaisirChoix()) *)
          writeln('')
       UNTIL (choix = 0);
    END.
    (*feat Loann*)
