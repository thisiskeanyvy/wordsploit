# WordSploit ![visitors](https://visitor-badge.glitch.me/badge?page_id=page.id=thisiskeanyvy.wordsploit) [![wordsploit](https://img.shields.io/github/languages/top/thisiskeanyvy/wordsploit)](https://github.com/thisiskeanyvy/wordsploit) [![wordsploit](https://img.shields.io/github/license/thisiskeanyvy/wordsploit)](https://github.com/thisiskeanyvy/wordsploit)
Programme de brute force amélioré en récursif

## Utilisation de WordSploit

![programme cli](https://zupimages.net/up/20/48/eiey.png)

## Programme de déchiffrement
### Les familles d'attaques cryptanalytiques
Il existe plusieurs familles d'attaques cryptanalytiques, les plus connues étant l'analyse fréquentielle, la cryptanalyse différentielle et la cryptanalyse linéaire.

- L'analyse fréquentielle :  
Elle, examine les répétitions des lettres du message chiffré afin de le déchiffrer.

- L'indice de coïncidence :  
Il, permet de calculer la probabilité de répétitions des lettres d'un message chiffré. Il est souvent couplé avec l'analyse fréquentielle, ce qui lui permet de connaître le type de chiffrement d'un message ainsi que la longueur probable du message déchiffré.

- L'attaque par mot probable :  
Elle consiste à supposer l'existence d'un mot probable dans le message chiffré. Il est donc possible d'en déduire le message déchiffré si le mot choisi est correct.

- L'attaque par dictionnaire :  
Elle consiste à tester tous les mots d'une liste comme mot clef. Elle est souvent couplée à l'attaque par force brute.

- L'attaque par force brute :  
Elle consiste à tester toutes les solutions possibles de mots de passe ou de combinaisons. Elle est peu utilisée pour des mots de passe possédant un très grand nombre de caractères car le temps nécessaire au déchiffrement devient alors trop important.

- Attaque par paradoxe des anniversaires :  
C'est un résultat probabiliste qui est utilisé dans les attaques contre les fonctions de hachage. Ce paradoxe permet de donner une borne supérieure de résistance aux collisions d’une telle fonction. Cette limite est de l'ordre de la racine de la taille de la sortie.

Dans notre cas, la méthode d'attaque cryptanalytique utilisée pour trouver le message déchiffré est l'attaque par force brute en récursif car le programme est conçu en Python. Il permet ainsi de déchiffrer un message chiffré avec n'importe qu'elle méthode tout en testant toutes les combinaisons rapidement et efficacement.
