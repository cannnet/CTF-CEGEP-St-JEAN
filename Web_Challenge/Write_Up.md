# Capture the Flag (CTF) Write-Up: Web Exploitation Challenge
## Introduction
Cet article documente mon approche et ma solution pour le défi de l'exploitation Web. Le défi consistait à accéder à une page Web hébergée sur un serveur et à inspecter le code source HTML pour localiser et extraire le drapeau caché, mettant en valeur les compétences en exploitation Web et en analyse de code source.

## Aperçu du défi
Le défi Exploitation Web demandait aux participants de naviguer vers une page Web hébergée sur un serveur et d'utiliser des outils d'inspection Web pour analyser le code source HTML et extraire l'indicateur caché.

## Approche
Pour résoudre le défi de l'exploitation Web, j'ai adopté l'approche suivante :

J'ai accédé à la page Web fournie dans le défi, soit en cliquant sur un lien fourni, soit en saisissant manuellement l'URL dans un navigateur Web.
Une fois sur la page Web, j'ai fait un clic droit sur la page et sélectionné "Inspecter" ou utilisé les outils de développement du navigateur Web pour accéder au code source HTML.
Dans le code source HTML, j'ai soigneusement examiné les éléments, les attributs et les sections JavaScript pour identifier les zones potentielles où le drapeau pourrait être masqué.
En analysant le code, j'ai localisé la section JavaScript contenant une variable nommée "flag" affectée à la valeur “01253{HTTP cannot STOP you!}”. Cela indiquait que le drapeau était stocké dans le code JavaScript de la page Web.
J'ai copié la valeur de la variable "flag" (“01253{HTTP cannot STOP you!}”) et j'ai considéré que le défi était résolu.
Détails techniques
En inspectant le code source HTML de la page Web, j'ai identifié le drapeau intégré dans la section JavaScript. Le drapeau a été stocké dans une variable nommée "flag" avec la valeur “01253{HTTP cannot STOP you!}”.

## Constatations et solutions
En inspectant le code source HTML de la page Web, j'ai localisé le drapeau dans la section JavaScript. Le drapeau a été stocké dans une variable nommée "flag" avec la valeur “01253{HTTP cannot STOP you!}”.

## Conclusion
Le défi Exploitation Web a fourni l'occasion de démontrer sa maîtrise de l'analyse du code source HTML et de l'utilisation des outils d'inspection Web pour localiser les informations cachées. En accédant à la page Web, en inspectant le code source HTML et en identifiant la section JavaScript contenant la variable flag, j'ai réussi à récupérer le drapeau.

Ce défi a mis en évidence l'importance des techniques d'inspection Web et de l'analyse du code source dans l'exploitation Web, soulignant l'importance d'examiner en profondeur les applications Web pour détecter les informations cachées.
