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


------
TP Sup
------

.. code-block:: pas

    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise / Loann Pottier
    -- Date de creation  : Sun Nov 11 2018
    --
    -- But               : TP de géométrie en Pascal
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    PROGRAM Tp1;

    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Sun Nov 11 2018
    --
    -- But               : TP de géométrie - question 1
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    PROCEDURE ligne(n : integer);
    VAR
        x: integer;
    begin
        for x:=1 to n do
            writeln('*');
    end;

    PROCEDURE carre1(n : integer);
    VAR
        x,y: integer;
    begin
        for x:=1 to n do
            begin
            for y:=1 to n do
                write('* ');
            writeln('')
            end;
    end;

    PROCEDURE triangle1(n : integer);
    VAR
        x,y: integer;
    begin
        for x:=1 to n do
            begin
                for y:=1 to x do
                    write('* ');
                writeln('');
            end;
    end ;

    PROCEDURE triangle2(n : integer);
    VAR
        x, y: integer;
    begin
        for x:=1 to n do
            begin
                for y:=1 to n-x do
                    write('  ');
                for y:=1 to x do
                    write('* ');
            writeln(' ');
            end;
    end;

    PROCEDURE carre2(n : integer);
    VAR x,y: integer;
    begin
        for x:=1 to n do
            begin
            if (x=1) or (x=n) then
                begin
                for y:=1 to n do
                    write('* ');
                end
            else
                begin
                write('* ');
                for y:=1 to n-2 do
                    write('  ');
                write('* ');
                end;
            writeln('');
            end;
    end;

    PROCEDURE croix(n : integer);
    VAR x,y: integer;
    begin
        for x:=1 to n do
            begin
            for y:=1 to n do
                begin
                if (y=x) or (y=n-x+1) then
                    write('* ')
                else
                    write('  ')
                ;
                end;
            writeln('');
            end;
    end;

    PROCEDURE q1();
    VAR
        choix,n : integer;
    begin
        writeln('Choisissez la fonction à lancer');
        writeln('1 - Ligne');
        writeln('2 - Carré1');
        writeln('3 - Triangle1');
        writeln('4 - Triangle2');
        writeln('5 - Carré2');
        writeln('6 - Croix');
        write('> ');read(choix);
        if (choix>6) or (choix<1) then
            begin
                writeln('Choix invalide')
            end
        else
            begin
                writeln('');
                write('Entrez l''entier n : ');read(n);
                case choix of
                    1 : ligne(n);
                    2 : carre1(n);
                    3 : triangle1(n);
                    4 : triangle2(n);
                    5 : carre2(n);
                    6 : croix(n);
                else
                    writeln('Nothing');
                end;
            end;
        writeln('')
    end;


    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Sun Nov 42
    --
    -- But               : TP de géométrie - question 2
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    PROCEDURE q2();
    VAR
        word : string;
        x : integer;
        a : char;
    begin
        writeln('Entrez une chaine de caractères');
        write('> ');read(word);
        for x:=1 to length(word) do
            begin
            a := word[x];
            if a in ['a','e','i','o','u','y'] then
                write('?')
            else
                write(a)
            ;
            end;
        writeln('');
    end;


    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Mon Nov 12 2018
    --
    -- But               : TP de géométrie - question 3
    -- Remarques         : Aucune
    -- Compilation       : fpc
     -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    FUNCTION q3f() : integer;
    VAR word : string;
        x,a : integer;
    begin
        writeln('Entrez une chaine de caractères');
        write('> ');read(word);
        a := 1;
        for x:=1 to length(word) do
            if (word[x] = ' ') then
                a := a+1
            ;
        q3f := a;
    end;

    PROCEDURE q3();
    VAR a:integer;
    begin
        a := q3f();
        writeln(a);
    end;


    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Tue Nov 13 2018
    --
    -- But               : TP de géométrie - question 4
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    FUNCTION q4f() : string;
    VAR sent,temp,rep:string;
        a:char;
        x,y:integer;
    begin
        write('Saisissez une chaine de caractères :');
        read(sent);
        if sent='' then
            begin
            sent := '     lol mdr     ';
            write(sent)
            end;
        a := ' ';
        x := 0;
        temp := '';
        rep := '';
        while a=' ' do
            begin
            x := x+1;
            a := sent[x];
            end;
        for y:=x to length(sent) do
            temp := temp+sent[y];

        a := ' ';
        x := length(temp)+1;
        while a=' ' do
            begin
            x := x-1;
            a := temp[x];
            end;
        for y:=x downto 1 do
            rep := temp[y]+rep;
        writeln('');
        q4f := rep;
    end;

    PROCEDURE q4();
    VAR s:string;
    begin
        s := q4f();
        writeln('-',s,'-')
    end;

    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Tue Nov 13 2018
    --
    -- But               : TP de géométrie - question 5
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    FUNCTION lireInt() :integer;
    VAR x:integer;
    begin
        writeln('');
        write('> ');
        read(x);
        lireInt := x;
    end;

    PROCEDURE q5funct(VAR x,y:real);
    VAR a,b,c,d,e,f:integer;
        temp1,temp2:real;
    begin
        writeln('Entrez les valeurs de a, b, c, d, e et f');
        a := lireInt();
        b := lireInt();
        c := lireInt();
        d := lireInt();
        e := lireInt();
        f := lireInt();
        temp1 := f-(d*c)/a;
        temp2 := e+b/a;
        y := -temp1/temp2;
        x := (c-b*y)/a;
    end;

    PROCEDURE q5();
    VAR x,y:real;
    begin
        x := 0.0;
        y := 0.0;
        q5funct(x,y);
        writeln('Les solutions sont x=',x,' et y=',y);
    end;

    (*
    ------------------------------------------------------------------------------------
    -- Fichier           : tp2.pas
    -- Auteur            : Arthur Blaise
    -- Date de creation  : Sun Nov 11 2018
    --
    -- But               : TP de géométrie - procédure prinicpale
    -- Remarques         : Aucune
    -- Compilation       : fpc
    -- Edition des liens : fpc
    -- Execution         : shell
    ------------------------------------------------------------------------------------
    *)

    VAR
        choix : integer;
    begin
        write('Question n°');
        read(choix);
        if (choix>5) or (choix<0) then
            writeln('Choix invalide')
        else
            begin
                writeln('');
                case choix of
                    1 : q1();
                    2 : q2();
                    3 : q3();
                    4 : q4();
                    5 : q5();
                else
                    writeln('Nothing');
                end;
            end;
        writeln('')
    end.


----------------
Encore plus loin
----------------

.. code-block:: pas

    PROGRAM minMax;

    CONST imin=1; imax=8;
    Type tabstat = array[imin..imax] of real;

    PROCEDURE q1(t:tabstat; var min, max:real);
    VAR i:integer;
    begin
    min := t[1]; max := t[1];
    FOR i:=1 to length(t) do
        begin
        if t[i]<min then
            min := t[i]
        ;
        if t[i]>max then
            max := t[i]
        end;
    end;

    VAR t:tabstat;
    i:integer;
    min,max:real;
    Begin
    FOR i:=imin to imax do
    begin
        write('> ');read(t[i]);
    end;
    writeln('');
    q1(t,min,max);
    writeln('Minimum : ',min,' | Maximum : ',max);
    writeln(' ');
    end.

.. code-block:: pas

    PROCEDURE q2(t1,t2:tabstat, var stroumpf:real);
    begin
    FOR i:=1 to length(t2) do
        for j:=1 to length(t) do
            stroumpf := stroumpf + t[j]*t2[i];
    end;
    
.. code-block:: pas

    PROCEDURE q1(t:tabstat; var t2:tabstat);
    VAR i,j:integer;
    begin
    j := 1;
    t2[1] := t[1];
    for i:=2 to length(t) do
        if t[i]<>t[i-1] then
        begin
            j := j+1;
            t2[j] := t[i];
        end;
    end;

-----------------------
Les tableaux dynamiques
-----------------------

Le carré magique
----------------

.. code-block:: pas

    function izmagic(tableau:carre):boolean;
    var j,s,exs:integer; // incrément, somme, et deuxième somme
        i:array of integer; // ligne du carré
    begin
        s := 0;
        exs := -1;
        izmagic := True;
        for i in tableau do begin // on commence par les lignes
            for j in i do
                s := s+j;
            if exs>-1 then
                izmagic := izmagic and (s=exs)
            else
                exs := s;
            s:=0;
            end;
        exs := -1;
        for j:=0 to high(tableau[0]) do begin // puis les colonnes
            for i in tableau do
            s := s+i[j];
            if exs>-1 then
                izmagic := izmagic and (s=exs)
            else
                exs := s;
            s := 0;
            end;
        exs := 0;
        for j:=0 to high(tableau) do begin // enfin les deux diagonales
            exs := exs + tableau[j,j]; // x=y
            s := s + tableau[j,high(tableau)-j]; // n-x=y
            end;
        izmagic := izmagic and (s=exs);
    end;


Horloge digitale
----------------

.. code-block:: pas

    Uses Dos,sysutils,Crt;
    Type number=array[0..4] of string;

    Const zero:number= ('#####',
                        '#   #',
                        '#   #',
                        '#   #',
                        '#####');
    Const one:number = ('    #',
                        '    #',
                        '    #',
                        '    #',
                        '    #');
    Const two:number = ('#####',
                        '    #',
                        '#####',
                        '#    ',
                        '#####');
    Const three:number=('#####',
                        '    #',
                        ' ####',
                        '    #',
                        '#####');
    Const four:number= ('#   #',
                        '#   #',
                        '#####',
                        '    #',
                        '    #');    
    Const five:number= ('#####',
                        '#    ',
                        '#####',
                        '    #',
                        '#####');
    Const six:number = ('#####',
                        '#    ',
                        '#####',
                        '#   #',
                        '#####');
    Const seven:number=('#####',
                        '    #',
                        '    #',
                        '    #',
                        '    #');
    Const eight:number=('#####',
                        '#   #',
                        '#####',
                        '#   #',
                        '#####');
    Const nine:number= ('#####',
                        '#   #',
                        '#####',
                        '    #',
                        '#####');
    Const point:number =('   ',
                        ' # ',
                        '   ',
                        ' # ',
                        '   ');
  
    procedure displayNumb(wo:string);
    var c:char;
        i:integer;
        t:string;
    begin
        t := '';
        for i:=0 to 4 do begin
            for c in wo do
                CASE c OF
                    '0': t := t+zero[i]+' ';
                    '1': t := t+one[i]+' ';
                    '2': t := t+two[i]+' ';
                    '3': t := t+three[i]+' ';
                    '4': t := t+four[i]+' ';
                    '5': t := t+five[i]+' ';
                    '6': t := t+six[i]+' ';
                    '7': t := t+seven[i];
                    '8': t := t+eight[i]+' ';
                    '9': t := t+nine[i]+' ';
                    ':': t := t+point[i];
                end;
            writeln(t);
            t := '';
        end;
    end;

    procedure q2;
    var Hour,Min,Sec,HSec:word;
        exSec:word; //backup des secondes
        H,M,S:string;
    begin
        exSec := 0;
        while True do begin
            GetTime(Hour,Min,Sec,HSec);
            if Sec<>exSec then begin
                clrscr;
                if Hour<10 then H := '0'+IntToStr(Hour) else H := IntToStr(Hour);
                if Min<10 then M := '0'+IntToStr(Min) else M := IntToStr(Min);
                if Sec<10 then S := '0'+IntToStr(Sec) else S := IntToStr(Sec);
                    displayNumb(H+':'+M+':'+S);
                    exSec := Sec;
                    end;
                end;
        end;


Manipulation de listes dynamiques
---------------------------------

Ici le but est de créer une fonction invert(array) qui permet d'inverser l'ordre des valeurs d'une liste, et une deuxième, push(array,integer) qui décale chaque valeur d'un certain nombre de rang vers la droite. Evidemment les fonctions doivent pouvoir s'adapter à la longueur de la liste.

Parce que le modulo natif en Pascal m'a occasionné pas mal de bugs, j'ai préféré créer moi-même une fonction de modulo. Avec si peu de lignes pour tellement de problèmes en moins, je n'avais rien à perdre !

.. code-block:: pas
    
    function modulo(a, b: integer): integer;
    begin
      modulo:= a - b * Round(a / b);
      if modulo<0 then modulo := modulo+b
    end;
    
    function invert(table:array):array
    var i:integer;
    Begin
        SetLength(invert,length(table));
        for i:=0 to high(table) do
            invert[high(table)-i] := table[i];
    end;

    function push(table:array; n:integer):array;
    var i,j:integer;
    Begin
        SetLength(push,length(table));
        for i:=0 to high(table) do begin
            j := modulo(n+i,length(table));
            push[j] := table[i];
            end;
    end;
    
    
-------------
Les pointeurs
-------------

Ici nous utilisons les pointeurs pour créer notre propre type de liste, et en implémentant sur ces listes différentes fonctions telles que l'insertion d'une valeur ou la suppression d'un index. Voici donc ces fonctions, ainsi que le menu qui permet de les tester.

.. code-block:: pas

    PROGRAM do_it_urself;

    {$mode objfpc}

    uses math;

    TYPE
        ptr_noeud = ^noeud;
        noeud = RECORD
            valeur : INTEGER;
            suivant : ptr_noeud;
        end;


    function creerNoeud(val:INTEGER;suivant:ptr_noeud=Nil):ptr_noeud;
    var nv:ptr_noeud;
    begin
        new(nv);
        nv^.valeur := val;
        nv^.suivant := suivant;
        creerNoeud := nv
    end;

    function len(tete:ptr_noeud):integer;
    var tmp:ptr_noeud;
    begin
        len := 0;
        tmp := tete;
        while (tmp <> Nil) do begin
            len := len+1;
            tmp := tmp^.suivant;
        end;
    end;

    procedure display(tete:ptr_noeud;text:string='');
    var i:integer;
    begin
        write(text,'[');
        for i:=1 to len(tete)-1 do begin
            write(tete^.valeur,';');
            tete := tete^.suivant;
            end;
        writeln(tete^.valeur,']');
    end;


    function insert_b(tete:ptr_noeud;val:integer):ptr_noeud;
    begin
        insert_b :=  creerNoeud(val,tete);
    end;

    procedure insert_e(tete:ptr_noeud;val:integer);
    var n:ptr_noeud;
    begin
        while tete^.suivant<>Nil do
            tete := tete^.suivant;
        n := creerNoeud(val);
        tete^.suivant := n;
    end;

    procedure insert_m(tete:ptr_noeud;val,pos:integer);
    var n:ptr_noeud;
        i:integer;
    begin
        i := 0;
        pos := min(pos,len(tete));
        while i<pos-1 do begin
            i := i+1;
            tete := tete^.suivant;
            end;
        n := creerNoeud(val,tete^.suivant);
        tete^.suivant := n;
    end;

    function del_b(tete:ptr_noeud):ptr_noeud;
    begin
        del_b := tete^.suivant;
        dispose(tete);
    end;

    procedure del_e(tete:ptr_noeud);
    begin
        while tete^.suivant^.suivant <> Nil do
            tete := tete^.suivant;
        dispose(tete^.suivant);
        tete^.suivant := Nil;
    end;

    procedure del_m(tete:ptr_noeud;pos:integer);
    var i:integer;
    begin
        i := 0;
        pos := min(pos,len(tete)-1);
        while i<pos-1 do begin
            i += 1;
            tete := tete^.suivant;
            end;
        tete^.suivant := tete^.suivant^.suivant
    end;

    function search(tete:ptr_noeud;val:integer):integer;
    var i:integer;
    begin
        i := 0;
        while tete<>Nil do begin
            if tete^.valeur=val then Exit(i);
            i := i+1;
            tete := tete^.suivant;
            end;
        exit(-1);
    end;

    function test:boolean;
    var tete,v2:ptr_noeud;
    begin
        v2 := creerNoeud(14);
        tete := creerNoeud(12,v2);
        insert_e(tete,20);
        display(tete,'Liste de départ: ');
        writeln;
        tete := insert_b(tete,-5);
        insert_e(tete,42);
        display(tete,'Insertion de -5 au début et 42 à la fin: ');
        writeln('Longueur de la liste: ',len(tete));
        insert_m(tete,34,3);
        display(tete,'Insertion de 34 à la case 3: ');
        writeln;
        del_e(tete);
        display(tete,'Suppression de la dernière case: ');
        del_m(tete,2);
        display(tete,'Suppression de la case 2: ');
        writeln('Index de la valeur 34: ',search(tete,34));
        Exit(True);
    end;


    function menu_insert(tete:ptr_noeud):ptr_noeud;
    var pos,val:integer;
    begin
        write('Entrez la valeur à insérer',#10,'> ');readln(val);
        if len(tete)=0 then
            Exit(creerNoeud(val));
        write('Entrez la position à laquelle insérer la valeur',#10,'> ');readln(pos);
        if (pos<0) or (pos>len(tete)) then begin
            writeln('Position invalide');
            Exit(tete);
            end;
        if pos=0 then
            tete := insert_b(tete,val)
        else if pos=len(tete) then
            insert_e(tete,val)
            else insert_m(tete,val,pos);
        exit(tete);
    end;

    function menu_search(tete:ptr_noeud):ptr_noeud;
    var val:integer;
    begin
        write('Entrez la valeur à rechercher',#10,'> ');readln(val);
        val := search(tete,val);
        if val=-1 then writeln('Valeur introuvable')
        else writeln('Cette valeur est à l''index ',val);
        exit(tete);
    end;

    function menu_del(tete:ptr_noeud):ptr_noeud;
    var pos:integer;
    begin
        write('Entrez l''index de la case à supprimer, entre 0 et ',len(tete),#10,'> ');readln(pos);
        if (pos<0) or (pos>len(tete)) then begin
            writeln('Position invalide');
            Exit(tete);
            end;
        if pos=0 then
            tete := del_b(tete)
        else if pos=len(tete) then
            del_e(tete)
            else del_m(tete,pos);
        exit(tete);
    end;

    function menu_random(tete:ptr_noeud):ptr_noeud;
    var i,n:integer;
    begin
        write('Entrez le nombre de cases à ajouter',#10,'> ');readln(n);
        if n<1 then begin
            writeln('Impossible d''ajouter un nombre négatif de cases !');Exit(tete);end;
        if n>150 then begin
            writeln('Impossible d''ajouter plus de 150 cases !');Exit(tete);end;
        if len(tete)=0 then begin
            tete := creerNoeud(round(random(n*200)-n*100));
            n := n-1;
            end;
        for i:=1 to n do
            insert_e(tete,round(random(n*200)-n*100));
        Exit(tete);
    end;

    function menu_del_2(tete:ptr_noeud):ptr_noeud;
    var val,pos:integer;
    begin
        write('Entrez la valeur à effacer du tableau',#10,'> ');readln(val);
        pos := search(tete,val);
        if pos=-1 then begin
            writeln('Valeur introuvable');
            Exit(tete);
            end;
        if pos=0 then
            tete := del_b(tete)
        else if pos=len(tete) then
            del_e(tete)
            else del_m(tete,pos);
        Exit(tete);
    end;

    function menu_del_3(tete:ptr_noeud):ptr_noeud;
    var val,pos:integer;
        b:boolean;
    begin
        write('Entrez la valeur à effacer du tableau',#10,'> ');readln(val);
        b := True;
        while b do begin
            pos := search(tete,val);
            // writeln('  #',pos,' trouvé');
            // display(tete,'   ');
            if pos=-1 then b:=False
            else if pos=0 then
                tete := del_b(tete)
            else if pos=len(tete) then
                del_e(tete)
                else del_m(tete,pos);
        end;
        Exit(tete);
    end;

    function menu_duplicate(tete:ptr_noeud):ptr_noeud;
    var i:integer;
        node:ptr_noeud;
    begin
        node := tete;
        for i:=1 to len(tete) do begin
            insert_e(tete,node^.valeur);
            node := node^.suivant;
            end;
        Exit(tete)
    end;

    function menu_reverse(tete:ptr_noeud):ptr_noeud;
    var l:array of integer;
        node:ptr_noeud;
        i:integer;
    begin
        SetLength(l,len(tete));
        i := 0;
        node := tete;
        while node<>Nil do begin
            l[i] := node^.valeur;
            node := node^.suivant;
            i := i+1
            end;
        node := tete;
        i := i-1;
        while node<>Nil do begin
            node^.valeur := l[i];
            node := node^.suivant;
            i := i-1
            end;
        Exit(tete)
    end;

    function menu_clear(tete:ptr_noeud):ptr_noeud;
    var node:ptr_noeud;
        i,pos:integer;
    begin
        if len(tete)<2 then Exit(tete);
        node := tete^.suivant;
        i := 0;
        while node<>Nil do begin
            if node^.suivant<>Nil then // si on n'est pas à la fin de la liste
                pos := search(node^.suivant,node^.valeur) // on détecte si la valeur est représentée plus loin dans la liste
            else break;
            if (pos=-1) and (node^.valeur <> tete^.valeur) then begin // Si non, on passe
                node := node^.suivant;
                i := i+1;
                continue
                end;
            node := node^.suivant;
            del_m(tete,i)
            end;
        Exit(tete)
    end;

    procedure menu;
    var tete:ptr_noeud;
        choice:integer;
        useless_b:boolean;
    begin
        tete := Nil;
        while True do begin
        writeln('Choisissez l''action à effectuer :',#10,'  1 - Insérer une valeur',#10,'  2 - Rechercher une valeur',#10,'  3 - Supprimer une case',#10,'  4 - Supprimer une valeur',#10,'  5 - Supprimer toutes les occurences d''une valeur',#10,'  6 - Dupliquer la liste',#10,'  7 - Inverser la liste',#10,'  8 - Supprimer les doublons',#10,'  9 - Ajouter des cases aléatoires',#10,'  10 - Afficher le programme de test',#10,'  0 - Quitter');
        write('> ');readln(choice);
        if (choice<0) or (choice>10) then begin
            writeln('Saisie invalide',#10);
            continue;
            end
        else if choice=0 then break;
        if (choice>1) and (choice<8) and (len(tete)=0) then begin
            writeln('Impossible de rechercher ou de supprimer une valeur dans un tableau vide !');
            continue;
            end;
        case choice of
            1: tete := menu_insert(tete);
            2: tete := menu_search(tete);
            3: tete := menu_del(tete);
            4: tete := menu_del_2(tete);
            5: tete := menu_del_3(tete);
            6: tete := menu_duplicate(tete);
            7: tete := menu_reverse(tete);
            8: tete := menu_clear(tete);
            9: tete := menu_random(tete);
            10: useless_b := test;
        end;
        if len(tete)>0 then display(tete,#10+'Valeur actuelle: ');
        writeln;
        end;
    end;

    begin
        randomize;
        menu;
        writeln(#10,'--- Fin du programme ---',#10)
    end.
