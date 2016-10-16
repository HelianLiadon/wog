# Combat terrestre - concepts

## Objectif de durée :
1 semaine maximum par combat disputé. Plus la bataille dure, plus les troupes sont décimées, et les factions saignées (combat au résultat de plus en plus instable, et difficulté de tenir le rythme pour la production et le transport)


## Types de troupe :
3 types de troupes :
+ Blindé ( > Artillerie  ,  < Aviation)
+ Aviation ( > Blindé  ,  < Artillerie)
+ Artillerie ( > Aviation  ,  < Blindé)

Pour chaque type, une troupe de chaque rapidité de progression:
+ Logarithmique (Rapide au début, stagnante après un certain temps)
+ Exponentielle (Lente au début, très rapide après un certain temps)

## Déroulement du combat :
Tous les jours, les troupes de chaque camp passent une attaque simultanée. Les dégâts sont calculés pour chaque type d'adversaire présent. Chaque troupe apporte sa force dans des proportions différentes selon le type. Concrètement :
+ Dégâts anti-blindé : `X * (dégâts Artillerie) + Y * (dégâts Blindés) + Z * (dégâts Aviation)`
+ Dégâts anti-aviation : `X' * (dégâts Artillerie) + Y' * (dégâts Blindés) + Z' * (dégâts Aviation)`
+ Dégâts anti-infanterie : ...

## Augmentation des dégâts
Chaque jour, après les attaques effectuées par les troupes, toutes les troupes voient leur jet de dégât augmenter en fonction de leur nombre et leur fonction associée (logarithmique/exponentielle). Concrètement :
+ Exponentielle : `(Multiplicateur dégâts) = nbr_moyen * 2 ^ (jour du combat)`
+ Logarithme : `(Multiplicateur dégâts) = nbr_moyen * log2(jour du combat)`

Avec `(Dégâts finaux) = (Dégâts théoriques) * (Multiplicateur dégâts)`

Où `nbr_moyen` est la moyenne de la présence de l'unité depuis le début des combats.

Chaque élément `elt` du calcul étant potentiellement remplacé par `f(elt)`, où f est une fonction linéaire (de la forme `y = a * x + b`)

Lorsqu'une troupe tombe à 0 de nombre, son bonus aux dégâts est ramené à 0.

# Combat terrestre - données

Dégâts:
+ Blindés
    - Anti-blindé: 0.5
    - Anti-aviation: 0.1
    - Anti-artillerie: 0.75
+ Aviation
    - Anti-blindé : 0.75
    - Anti-aviation : 0.4
    - Anti-artillerie : 0.25
+ Artillerie
    - Anti-blindé : 0.1
    - Anti-aviation : 0.9
    - Anti-artillerie : 0.1


Fonction:
+ Exponentielle : `bonus += nbr_moyen * 2 ^ (jour - 8)`
+ Logarithmique : `bonus += nbr_moyen * log2(jour + 2) /4`

Où `nbr_moyen` est la moyenne de la présence de l'unité depuis le début des combats. Ex:
- Premier jour : 200 Tanks Exp
- Deuxième jour : 380 Tanks Exp
- Troisième jour : 540 Tanks Exp

Au troisième jour, au moment du calcul des dégâts, `nbr_moyen = (200 + 380 + 540) / 3 = 373.33...` 

Les chars auront alors des dégâts de base (non multipliés par le multiplicateur dépendant du type de la troupe adverse) `deg = 373.33 * 2 ^ (3 - 8) = 11.66`

Dans les mêmes circonstances, des Chars Logs feraient `deg = 373.33 * log2(3 + 2) / 4 = 216.52`
