# Projet développement web

## Table of Contents
1. [Software Description ](#software-description)
2. [Repository Organization](#repository-information)
3. [Tutoriel](#tutoriel)
4. [Installation et technologies](#technologies)
5. [Collaboration](#collaboration)

### Software Description
***
Cette page web a pour objectif de représenter le tourisme en France. Nous avons présenté les 10 villes les plus touristiques de France métropolitaine : Paris, Lyon, Marseille, Toulouse, Bordeaux, Lille, Saint Malo, Nice, Chamonix et Strasbourg. Pour chacune des villes, nous allons représenter la Culture, la Gastronomie, l'Histoire et les activités correspondantes. Nous avons aussi représenter une page contact afin de conserver les coordonnées de notre agence de Tourisme : RTML.  

### Repository Organization
***
Le dossier templates contient tous les fichiers html qui définissent la structure du logiciel : acceuil,base,contact,ville et ville_indiv.
Le dossier images_tutorial contient les photos nécessaires à la réalisation de notre tutoriel.
Le dossier static contient les images que nous avons utilisés au cours de notre projet
App.py App.py et config.py contiennent les fichiers python qui permettent l'éxecution de notre projet.


### Tutoriel
***
Dans un premier temps, nous avons la représentation de notre page d'acceuil avec la présentation du premier pays touristique au monde : La France.
Il y a une barre de recherche représentant le nom des 10 villes que nous décrivons.  
<p align="center">
<img src="images_tutorial/image_a.png" alt="1" width="400"/>
</p>

Ensuite si nous cliquons sur Paris depuis la barre de recherche nous obtenons directement un lien vers la description de la ville. Ici pour Paris nous obtenons les informations concernant : la Gastronomie, les activités, l'historique et la culture.

Cette étape peut aussi être réalisé depuis la page d'acceuil, en cliquant sur Ville. Il y aura une liste des 10 villes les plus touristiques qui va s'afficher et l'utilisateur pourra donc cliquer sur la ville qui l'intéresse et donc accéder aux informations.

Enfin en cliquant depuis la page d'acceuil sur "Contact". Il y aura une page qui représentera toutes les informations (numéro de téléphone, adresses) concernant notre agence de voyage.

### Installation et Technologies
***
Pour accéder à notre page web vous devez utiliser un environnement python, et vous devez vérifier la version de python. Ensuite vous devez vous rendre sur le lien suivant : https://github.com/CHARFImerieme/PROJETDEVWEB, et copier le lien de la clé SSH.
Ensuite vous devez vous rendre sur votre terminal linux et tapper les commandes suivantes :   
```
$ git clone cle_SSH
$ cd PROJETDEVWEB/projet
$ ./do serve
Récupérer l'adresse html qui s'affiche dans le terminal
Puis suivre les instructions présenté dans la partie tutoriel

On peut aussi téléchargé le fichier ZIP puis accéder au dossier via le terminal est utilisé la commande suivantes :
$ ./do serve
Récupérer l'adresse html qui s'affiche dans le terminal
Puis suivre les instructions présenté dans la partie tutoriel

Voici la liste des logiciels utilisés durant notre projet :
python3: Version 3.7.3
Flask : Version  2.1.1 $ pip install Flask
```
### Collaborations
***
Notre projet est en format publique depuis githb, vous pouvez directement collaborer avec nous.
