On peut calculer approximativement le sinus de x (voir définition du sinus) en effectuant la sommation des n premiers termes de la série (c'est-à-dire la somme infinie) :
sin(x)=x-(x3^/3!)+(x^5/5!)-(x^7/7!)+...
où x est exprimé en radians. Réécrivez cette somme sous la forme :
sin(x)=somme f(i,x) avec i allant de 0 à l'infini
On vous demande donc de trouver f(i,x). Écrivez ensuite le code calculant de cette manière la valeur de sin(x) où x est lu sur input. Continuez l'addition des termes successifs dans la série jusqu'à ce que la valeur d'un terme devienne inférieure (en valeur absolue) à une constante e (prenez e=10^-6). Affichez ensuite l'approximation ainsi obtenue à l'écran.