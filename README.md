EXERCICE 1 (4 points) 

 
 
 
Écrire  une  fonction  moyenne  qui  prend  en  paramètre  un  tableau  non  vide  de  nombres 
flottants  et  qui  renvoie  la  moyenne  des  valeurs  du  tableau.  Les  tableaux  seront 
représentés sous forme de liste Python. 

EXERCICE 2 (4 points) 

On considère la fonction dec_to_bin ci-dessous qui prend en paramètre un entier positif 
a  en écriture décimale et qui renvoie son écriture binaire sous la forme d'une chaine de 
caractères.  

Exemples : 

>>> moyenne([1.0]) 
1.0 
 
>>> moyenne([1.0, 2.0, 4.0]) 
2.3333333333333335 
 
 
 
 

def dec_to_bin(a): 

    bin_a = ... 

    a = a//2 

    while a ... : 

        bin_a = ... + bin_a 

        a = ... 

    return bin_a 

Compléter la fonction dec_to_bin. 

Exemples :  

>>> dec_to_bin(83) 
'1010011' 
>>> dec_to_bin(127) 
'1111111' 

 

 

 

 

 2 / 2 

# sujet-16-bns
