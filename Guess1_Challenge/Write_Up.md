# Capture the Flag (CTF) Write-Up: Guess1 Challenge
Introduction
Cet article documente mon expérience et mon approche dans la résolution du défi Guess1, qui faisait partie d'un événement Capture the Flag (CTF). Le défi consistait à deviner un numéro secret dans une plage donnée et à obtenir un indice lié à une plage d'adresses IP commune dans les réseaux privés.

## Aperçu du défi
Le défi Guess1 demandait aux participants de deviner un nombre entre 1 et 10. Après avoir deviné le bon nombre, une série de messages de félicitations s'affichaient, suivis d'un indice encodé au format Base64.

## Approche
J'ai abordé le défi en analysant le programme fourni et en comprenant sa logique. Voici une ventilation de mon approche:

La fonction Guess1_number() a été appelée pour lancer le défi.
Le programme a généré un nombre secret aléatoire à l'aide de la fonction random.randint(), qui sélectionne un nombre entre 1 et 10 (inclus).
Une boucle while a été implémentée pour inviter en permanence l'utilisateur à deviner.
La conjecture de l'utilisateur a été comparée au numéro secret, et une rétroaction appropriée a été fournie.
Si la supposition correspondait au numéro secret, le programme affichait des messages de félicitations et un indice codé.
Détails techniques
Pour résoudre le défi, j'ai exécuté le script Python fourni et j'ai interagi avec lui en entrant des suppositions dans la console. Voici un exemple d'interaction réussie :
“Guess1 a number between 1 and 10: 5
Too high! Try again.
Guess1 a number between 1 and 10: 3
Too low! Try again.
Guess1 a number between 1 and 10: 4
Congratulations! You Guess1ed the correct number.
Number of attempts: 3
You have almost found the answer!
Think of a common IP address range BASE in private networks:
MDEyNTNDVEZ7aDFkM2QtRmw0Z30=”
L'indice codé fourni à la fin du défi était : MDEyNTNDVEZ7aDFkM2QtRmw0Z30=.

## Constatations et solutions
Après avoir réussi à deviner le numéro secret, j'ai reçu les informations suivantes :

Nombre de tentatives : 3
Indice : Pensez à une plage d'adresses IP commune BASE dans les réseaux privés : MDEyNTNDVEZ7aDFkM2QtRmw0Z30=
Pour obtenir l'indice réel, j'ai décodé la chaîne encodée en Base64, MDEyNTNDVEZ7aDFkM2QtRmw0Z30=, à l'aide d'un décodeur Base64. L'indice décodé était : 01253CTF{h1d3d3-Fl4g0}.

## Conclusion
Le défi Guess1 a fourni une occasion intéressante de tester nos compétences en devinettes. En analysant le script Python fourni et en interagissant avec lui, j'ai réussi à deviner le numéro secret et j'ai obtenu un indice encodé au format Base64. Le décodage de l'indice a révélé le drapeau : 01253CTF{h1d3d3-Fl4g0}.

Ce défi a été une excellente expérience d'apprentissage, soulignant l'importance de comprendre la logique du programme et d'appliquer les techniques appropriées pour résoudre les défis du CTF.
