
Script:

Bonjour et bienvenue, 

1. Présentation

Voici une petite vidéo pour vous présenter rapidement la prise en main
 du boitier OpenHEMS de OpenHomeSystem.


Il sert a piloter automatiquement certains appareils électriques
 pour optimiser la consommation électrique.
 Cela rentre dans les champs d'applications
 de la domotique pour rendre la maison "intelligente".

Nous allons voir comment le configurer


2. Présentation de ma maison

Qu'est-ce qu'on a pour faire ça d'un point de vue matériel?

* Un serveur OpenHEMS bien sûr, branché sur une prise de courant d'une part
 et sur la box via un cable Ethernet : 2 cables.

* Une clé USB ZigBee branché sur OpenHEMS
 car j'ai choisi de communiqué avec les appareils en ZigBee
 (Mais on pourrait s'en passer).

* Une clé LIXEE branché sur le compteur Linky. Rien d'illégal là dedans,
 c'est pour remonter les information que l'on appel Télé Information Client.
 Elle est connecté en ZigBee bien entendu

* 2 prise connectées ZigBee que je peux piloter (Allumer ou éteindre a distance).


2. Home-Assistant

a) Ajouter nos appareils

* Ajouter les appareils. Dans `Parametres`/`Appareils et services` click `Ajouter une integration`.

b) Tableaux de bords

* Ajouter les tableaux de bords `Parameters`/`Taleaux de bord` click `Ajouter un tableau de bord`.

 * URL `Web page` "http://192.168.1.202:8000/".

 * Tableau vide

 * `Tableau de bord Defaut` Tableau de bord complet avec tout.

 * Generate an Home-Assistant long_lived_token in Menu: User profile / Security / long lived token / Create token. Save it preciously, it's like a password for OpenHEMS access.

3. Configuration
 
Maintenant voyons comment on configure l'appareil.


b) 2ème étape configurer OpenHEMS

Pour cela le plus simple est de se rendre directement sur l'URL OpenHEMS. 
