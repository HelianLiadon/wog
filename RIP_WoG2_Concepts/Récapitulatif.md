# Contexte

## TODO

* Nom du jeu et de l'univers

## Background
* Pas Géocron
* Reste à définir
	

## Interface graphique et code
### Interface général
* Image d'un bureau vu depuis le fauteuil comme si on y était assis.
* Indicateurs placés sur le bureau donnant les indications comme les messages, les crédits, les points de mouvements, etc.
* Elements cliquable sur le bureau menant aux différents sous menus.
* Possibilité de prévoir un skin light avec les barres d'indicateurs comme l'ancien Geocron, ou même de les inclure de base.

### Interface Salle de commande
* Accès à la carte Stellaire affichant par défaut le système solaire actuel et possibilité d'afficher les autres.
* Accès aux commandes de mouvements propulseurs et hyper propulsion.

### Interface Passerelle de combat
* Accès à la console de tir et de ciblage.

### Interface Salle des machines
* Accès à la salle des moteurs, de réparation, de recharge des accumulateurs et des boucliers.
		
### Notes et autre
* Koko aime les stats, il en veut partout.

		
# Diplomatie

## Formation des factions
* Semi-liberté de choix pour les joueurs
* Blocage des factions trop puissantes
* Bouton "inscris moi dans la faction qui en a le plus besoin"

## Factions
* 5 factions
* 2 super-factions
  * Pour changer de super-faction il faut l'acceptation des membres de la super-faction rejointe

## Lead
* Un joueur est élu (réélection) tous les 20 jours, il a les pouvoirs de décision quant à la faction
* Les joueurs changent leur vote quand bon leur semble 

## Gain du jeu
* Il existe différentes conditions de victoire
  * Une super faction contrôle X% de l'univers
  * Contrôle de certains lieux/objets particuliers
  * Construction d'un bâtiment spécial

## Récompenses
* Les 2 meilleurs factions de la super-faction victorieuse ont un gain, les autres pas
* Les gains sont distribués aux joueurs et non aux factions


## TODO
* Interactions entre joueurs
* Association de joueurs
* Association de factions
	
	
# Gameplay
	
## Géographie
* Galaxie de systèmes reliés par des portes de saut
  * Carte à déterminer (NB. Elle dépend du gameplay pour être intéressante)
*Systèmes
  * Grillage hexagonal
  * Entre 20 et 40 cases de largeur (càd 7 à 14 cases de côté si le système est un hexagone). TODO: Définir la taille exacte, déterminer si la taille est la même pour tous les systèmes.
  * Soleil infranchissable au centre
  * Plusieurs planètes colonisation. TODO: taille des planètes, déplacement ou non des planètes, nombre de planète par système.
  * Autres éléments de géographie (ex. Champs d'astéroïdes)
  * Portes de saut vers d'autres systèmes (NB. Le nombre de porte est définit par la carte générale)
			
## Gestion des comptes
* Un compte par personne auquel peuvent être reliés plusieurs amiraux
* Certaines caractéristiques communes aux deux comptes (crédits, compétences, peut-être expérience)
* Limitation au nombre de compte d'une certaine classe par joueur. TODO: Définir les limitations exactes.
		
## Expérience
* Le gain d'xp dépend (par exemple, reste à déterminer) de l'xp des autres joueurs actifs, du gain moyen des autres joueurs
* Respécialisation possible pour un coût en xp
	
## Classes. TODO: Trouver un meilleur nom (ex. Division, section, spécialisation)
* Les amiraux doivent choisir une classe
* La classe détermine l'accès aux
  * Compétences
  * Vaisseaux
  * Modules
  * Upgrades
* La classe limite les choix de développements
  * Upgrades
  * Vaisseaux
  * Modules
  * Pas de limitation quant aux compétences

### Classes
* Combat
  * Léger
  * Lourd
  * Vitesse
  * Siphon
  * Bombardement
* Logistique
  * Terraformeur
  * Constructions spatiales
  * Transport lourd/express
* Soutien
  * Radar
  * Jammer
  * Changelin
  * Bouclier
  * Ravitaillement (?)
NB : Les "sous-classes" (ex. Bombardement) sont déterminées par des choix du joueurs (vaisseaux, compétences), mais n'ont pas d'existence officielle.
		
## Vaisseaux
* Comportent des modules dépendant du type de vaisseau
* Peuvent être détruits (si pas de modules d'urgence)
* Système de tonnage
* Marques de vaisseaux
* Coût
  * Crédits
  * Ressources
  * Possibilité de compenser un manque de ressource par un surplus de crédits
* Restriction
  * Classe
  * ? Compétences
  * ? Pallier d'ordre à atteindre
* ? Composition
  * ? Vaisseaux de faction
* ? Possibilité d'avoir des modules à choix
		
## Modules
* Pas par chrono-poste
* Les modules peuvent être internes ou externes (cf. "Combat")
### Modules
* Coque
  * Protège les modules internes
* Propulseur
  * ? Différence entre propulseur pour avancer et pour tourner
 * Pulseur
* Réacteur
  * Fournit passivement les autres modules en énergie
* Distributeur d'énergie
  * Permet de choisir quel module est alimenté en énergie prioritairement
  * Pas sur tous les vaisseaux
* Radar
  * Permet de voir
  * ? Scan des vaisseaux adverses
  * ? Scan des planètes
* Réparation
  * ? Différents modules pour la réparation de la coque, des modules externes et pour les modules internes
  * ? Sur tous les vaisseaux
  * ? Possibilité de réparer en dehors des planètes ou bases de réparation
* Armement
  * ? Armes spéciales tirant uniquement sur certains modules
  * ? Tout
* Défenses
  * ? Tout
* Soute
* Module de constructions
  * ? Différents modules pour les constructions terrestres et spatiales
* Téléport d'urgence
  * Empêche la destruction du vaisseau en le téléportant sur la planète mère
  * La garanti du constructeur fournis un vaisseau de rechange le temps des réparations
* ? Jamming
* ? Changelin
* ? Siphon
* ? Bombardement
* ? Autres

### A déterminer
* Coût et restrictions
* Modules de factions
* Différentes "marques de vaisseaux"
* Incidents (NB. Pas forcément facile à rendre intéressants)
* Quels modules sont internes/externes
	
## Combat spatial
* Nécessité d'être sur la même case que le vaisseau qu'on attaque
* Nécessité de détruire la coque adverse pour pouvoir toucher ses modules internes
  * Syphon (surcharge d'énergie)
  * ? Armes spéciales
* Types d'armement
  * Tourelles pour tous
  * Chaque "sous-classe" a des modules d'armement spécifiques
* Coût et limitations d'un tir
  * Coût en ordre
  * Temps de rechargement
  * Ravitaillement
  * Tourelle (armement de base) ne consommant pas de ravitaillement
* Possibilité de choisir le module touché
  * ? Pas en upgrade ou en compétence
* Combat contre les bases spatiales
  * Traiter les bases spatiales comme des vaisseaux

## Combat planétaire
### TODO
Tout.
		
## Déplacement
* Porte de saut entre les systèmes. TODO : trouver un meilleur nom.

### Propulseur
* Au sein d'un système
* Peut être gêné par des cases ou effets spéciaaux (ex. champs d'astéroïde, champs de mines spatiales)
* Coût et limitations
  * Coût en ordres
  * Rechargement
  * Eventuellement ravitaillement pour propusleurs avancés
* Avantager le fait d'aller tout droit

### Pulseur
* Au sein d'un système
* TODO : principe, temps d'attente avant/après le saut planoforme, risques
			
## Constructions

### Ressources
* TODO : Tout.

### Constructions sur les planètes
  * ? Uniquement sur les planètes de la faction
  * ? Quoi

### Constructions sur les cases spatiales
*  Possibilité de nombreuses constructions pour permettre de redéfinir la géographie d'un secteur
* Mines
* Bases spatiales
  * Radar
  * Réparation
  * Défenses
  * Manoeuvre
  * Changement de module
  * ? Autre