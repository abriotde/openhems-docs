
Script:

Bonjour et bienvenue, 

1. Présentation

Voici une petite vidéo pour vous présenter rapidement la prise en main
 du boitier OpenHEMS de OpenHomeSystem.


Il sert a piloter automatiquement certains appareils électriques
 pour optimiser la consommation électrique.
 Cela rentre dans les champs d'applications
 de la domotique pour rendre la maison intelligente.


2. Implémentation chez moi

Concrètement, Voici l'implémentation dans ma maison.

C'est un écran Home-Assistant tout a fait classique que j'ai configuré simplement.

On peut voir 

* l'historique de ma consommation. On note la forte hausse la nuit.

* A droite, la météo,

* Le tarif EDF du jour car j'ai un contrat tempo
 (C'est un peu compliqué a configurer) mais c'est faisable,
 et Home-Assistant permet d'à peu près tout ajouter si l'on s'y penche un peu.

* Et on voit que la charge de ma voiture est éteinte.

* En dessous on a accès au widget OpenHEMS.
 Il me permet de demander à OpenHEMS de charger ma voiture.
 Par exemple, je peux lui demander 6h de charge.
 Je sauve mes modifications en clickant sur l'icone de disquette.


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


3. Configuration

Maintenant voyons comment on configure l'appareil.

a) 1ere étape: configurer Home-Assistant

* Ajouter les appareils. Dans `Parametres`/`Appareils et services` click `Ajouter une integration`.

* Ajouter les tableaux de bords `Parameters`/`Taleaux de botrd` click `Ajouter un tableau de bord`.

 * `Tableau de bord Defaut` Tableau de bord complet avec tout.

 * Tableau de bord avec un component URL pour avoir la programmation des appareil : http://192.168.1.202:8000/?n=1

 * `Web page` "http://192.168.1.202:8000/".


Generate an Home-Assistant long_lived_token in Menu: User profile / Security / long lived token / Create token. Save it preciously, it's like a password for OpenHEMS access.




b) 2ème étape configurer OpenHEMS

Pour cela le plus simple est de se rendre directement sur l'URL OpenHEMS. 
