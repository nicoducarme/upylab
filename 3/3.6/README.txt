Les mises possibles et les retours correspondants quand le pari est gagné sont donnés ci-dessous
Mise	retour si gagné
Numéro exact (0 à 12)	12 fois la mise	
Pair ou Impair	2 fois la mise
Rouge ou Noir	2 fois la mise
Pour simplifier, on suppose que le zéro est ni rouge ni noir, mais est pair.
Écrire un programme qui lit ce que mise le joueur parmi :
0, 1, ..., 12
13 pour "Pair"
14 pour "Impair"
15 pour "Rouge"
16 pour "Noir"
et qui, après avoir actionné la roulette avec la commande x = roulette() où x reçoit le nombre entre 0 et 12 tiré par la roulette, imprime le retour correspondant: 0 si le pari est perdu, ou la valeur indiquée si la pari est gagné. Par exemple si la pari est 14 ("Impair") et que 7 est sorti par la roulette, le résultat est : 2
Votre code à tester par upylab ne doit pas avoir de paramètre dans l'input. Exemple: a = input() plutôt que a = input("Quel pari faites-vous ? : "))
Pour tester votre code, vous devez remplacer x = roulette() par x = int(input()) pour entrer ce que la roulette a tiré. Les deux premières lignes du code sont donc :
a = int(input()) # pari du joueur entre 0 et 16

x = int(input()) # tirage entre 0 et 12