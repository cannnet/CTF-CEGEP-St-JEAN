# Capture the Flag (CTF) Write-Up: Guess2 Challenge
Introduction
Cet article documente mon approche et ma solution pour le défi Guess2, un défi Capture the Flag (CTF). Le défi consistait à utiliser des techniques de rétro-ingénierie et l'application Ghidra  pour récupérer le drapeau intégré à l'application sans nécessairement deviner correctement le numéro secret.

## Aperçu du défi
Le défi Guess2 demandait aux participants de tirer parti de l'outil d'ingénierie inverse Ghidra pour analyser le programme C fourni et trouver un moyen de récupérer l'indicateur stocké dans l'application, plutôt que de se concentrer uniquement sur la devinette du numéro secret.

## Approche
Pour résoudre le défi Guess2, j'ai adopté l'approche suivante, en utilisant l'outil de rétro-ingénierie Ghidra (ou d'autres applications telles que : IDA, Radare2, Binary Ninja, OllyDbg et etc) :

J'ai chargé le programme C fourni dans Ghidra et effectué une analyse approfondie de son code et de ses fonctionnalités.
En examinant le code décompilé, j'ai recherché toutes les références au drapeau ou aux mécanismes qui me permettraient de le récupérer.
J'ai prêté une attention particulière aux déclarations de variables, aux opérations d'entrée/sortie et à toute structure de flux conditionnel ou de contrôle qui pourrait fournir des conseils ou des indices sur le processus de récupération des drapeaux.
Grâce aux puissantes capacités d'analyse de Ghidra, j'ai identifié une section de code spécifique responsable de l'affichage du drapeau.
En examinant attentivement le segment de code pertinent, j'ai déterminé l'emplacement de la mémoire ou la fonction responsable du stockage et de l'impression du message drapeau.
En utilisant les capacités de débogage de Ghidra, j'ai suivi l'exécution du programme et surveillé les changements de mémoire pour identifier l'emplacement du drapeau.
Une fois l'adresse mémoire de l'indicateur identifiée, j'ai développé un script personnalisé ou utilisé les fonctionnalités de script de Ghidra pour lire et récupérer directement la valeur de l'indicateur dans la mémoire.
En exécutant le script ou en utilisant la fonctionnalité intégrée de Ghidra, j'ai réussi à obtenir le drapeau intégré à l'application.
Détails techniques
Grâce à l'utilisation des capacités d'ingénierie inverse de Ghidra, j'ai analysé le programme C fourni, identifié l'emplacement de la mémoire du drapeau et développé un script ou utilisé les fonctionnalités de script de Ghidra pour récupérer la valeur du drapeau directement à partir de la mémoire.

## Constatations et solutions
En procédant à l'ingénierie inverse du programme C fourni à l'aide de Ghidra et en tirant parti de ses capacités de script, j'ai réussi à récupérer l'indicateur intégré à l'application sans me fier à deviner correctement le numéro secret.

## Conclusion
Le défi Guess2 a fourni une excellente occasion d'appliquer des compétences en ingénierie inverse et d'utiliser l'application Ghidra pour découvrir des informations cachées dans le programme C fourni. En analysant le code, en identifiant l'emplacement de la mémoire du drapeau et en tirant parti des capacités de Ghidra, j'ai réussi à récupérer le drapeau sans me fier uniquement à deviner le numéro secret.

Ce défi a mis en évidence l'importance des outils et des techniques d'ingénierie inverse dans les compétitions CTF, mettant en évidence leur capacité à découvrir des informations cachées et à résoudre efficacement les défis.
