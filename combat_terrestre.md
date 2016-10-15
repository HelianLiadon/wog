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
+ Exponentielle : `(Dégâts bonus) += Nbr * 2 ^ (jour du combat)`
+ Logarithme : `(Dégâts bonus) += Nbr * log2(jour du combat)`

Avec `(Dégâts finaux) = (Dégâts théoriques) + (Dégâts bonus)`

Chaque élément `elt` du calcul étant potentiellement remplacé par `f(elt)`, où f est une fonction linéaire (de la forme `y = a * x + b`)

Lorsqu'une troupe tombe à 0 de nombre, son bonus aux dégâts est ramené à 0.

# Combat terrestre - données
