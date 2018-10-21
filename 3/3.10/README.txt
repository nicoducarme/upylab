Écrivez un mini jeu : le programme génère de manière (pseudo-) aléatoire un nombre naturel (nombre secret) dans l'intervalle entre 0 et 100.
Ensuite, le joueur doit deviner ce nombre en utilisant le moins d'essais possible.
A chaque tour le joueur peut faire un essai et le programme doit donner une parmi les réponses suivantes:
"Trop grand" : Si le nombre secret est plus petit et qu'on n'est pas au maximum d'essais
"Trop petit" : Si le nombre secret est plus grand et qu'on n'est pas au maximum d'essais
"Gagné en n essais !" : Si le nombre secret est trouvé
"Perdu ! Le secret était", nombre : Si vous avez fait 6 essais sans trouver le nombre secret
Le joueur a maximum 6 essais ; s'il ne devine pas le secret après 6 essais, le programme s'arrête après avoir écrit "Perdu ! Le secret était", nombre"
Exemple d’exécution (après la génération du nombre à deviner):
50
Trop grand
8
Trop petit
20
Trop petit
27
Gagné en 4 essais !
Pour qu'Upylab puisse tester si votre solution est correcte, il faut que vous respectiez strictement cette séquence. Si par exemple, vous n'affichez pas Trop petit ou Trop grand, le nombre suivant ne sera pas fourni par le système et votre solution sera considérée comme incorrecte
En pratique, vous devez débuter votre code comme suit :
import random
NB_ESSAIS_MAX = 6
secret = random.randint(0,100)
et ne pas faire d'autre appel à randint ou à une autre fonction de random
Conseil pour le débogage de votre code: le programme test d'UpyLaB utilise l'argument entier affiché en sortie, comme seed du module random. Cela signifie qu'après avoir importé random, l'instruction :
random.seed(argument)
est réalisé par UpyLaB avant de réaliser l'instruction :
secret = random.randint(0,100)
qui fournit le nombre à deviner.
Attention: l'argument n'est donc pas le nombre à deviner, mais bien ce qui permet au programme de le générer.

En faisant de même, vous pouvez répliquer une exécution test