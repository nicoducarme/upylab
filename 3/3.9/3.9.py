#declaration de variables
somme = 0
n = 0
i = 0
while i != -1: #repeter tant que i est different de -1
    i = int(input())
    if i != -1: #verifier si i est different de -1 pour le dernier input
        somme = somme + i
        n = n + 1
print(somme/n)
