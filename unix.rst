================
Suite du TP Unix
================

----
TP 2
----


Exercice 1
----------

.. code-block:: bash

    $ pwd
  /cergy/homee/b/blaisearth
  
    $ cd /
    $ ls
  bin    dev   initrd.img      lib64       mnt   root  srv  usr      vmlinuz.old
  boot   etc   initrd.img.old  lost+found  opt   run   sys  var      vms
  cergy  home  lib             media       proc  sbin  tmp  vmlinuz
  
    $ cd ~ 'ou' cd /cergy/homee/b/blaisearth 'ou' cd
    
    $ mkdir Info
    
    $ mkdir Info/SGF
    
    $ cd Info/SGF
    
    $ mkdir tmp
    
    $ cd tmp
    
    $ touch toto 'ou' > toto
    
    $ find ../.. | sed 's/[^/]*\//| /g;s/| *\([^| ]\)/+--- \1/'
  1/'
  +--- ..
  | +--- SGF
  | | +--- tmp
  | | | +--- toto
    $ ls -lR ..
  ..:
  total 1
  drwxr-xr-x 2 blaisearth users 3 nov.  19 14:28 tmp

  ../tmp:
  total 1
  -rw-r--r-- 1 blaisearth users 0 nov.  19 14:28 toto
    
    $ cd ..
    
    $ rmdir tmp
  rmdir: impossible de de supprimer 'tmp': Le dossier n'est pas vide
    $ rm -r tmp 'ou' rmdir --ignore-fail-on-non-empty tmp
    
    $ head ~/2050.txt -n 15
    
    $ more -9 ~/2050.txt
    
    $ head -n 9 ~/2050.txt | tail -n 5 > tmp1.txt
    $ head -n 13 ~/2050.txt | tail -n 2 > tmp2.txt
    $ cat tmp1.txt tmp2.txt > ~/data.txt
    
    $ cat ~/2050.txt
    $ more ~/2050.txt
    #La commande cat affiche le texte d'un coup, alors que more le fait défiler ligne par ligne
    
    $ more +/vautours ~/2050.txt
    $ more +/FFME ~/2050.txt
    
    $ mkdir tmp
    
    $ cp ~/2050.txt ./tmp
    
    $ cd tmp
    $ mv 2050.txt Escalade2050.txt
    
    $ mv Escalade2050.txt ~/
    
    $ ls ~/
    
    $ ln -s "/cergy/homee/b/blaisearth/Escalade2050.txt" Escalade2050
    
    $ ls -A --author -F -h -H -i -s
  total 512
  83135077 512 Escalade2050@
  

Exercice 2
----------

.. code-block:: bash

    $ head -n 5 2050.txt
    
    $ head -n 5 2050.txt > toto
    
    $ tail -n 5 2050.txt >> toto
    
    $ sort -b toto
    
    $ head -c 20 toto #affiche les 20 premiers caractères du fichier
    
    $ cp toto tata
    
    $ cat toto >> tata
    
    $ sort -u tata > tata2
    $ cat tata2 > tata
    $ rm tata2
    
    $ sed -i 's/ //g' tata
    

Exercice 3
----------

..code-block:: bash

    $ rm ~/Escalade2050.txt
    
    $ ls ./Info/SGF/tmp
  Escalade2050 #(en rouge)
  #La couleur rouge indique que le lien n'est plus valide, la source a disparu
