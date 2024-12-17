Bonjour chers amis fidèle de LinuxFR,



J'aimerais vous parler d'un projet de **Home Energy Management System**. Mais comme j'imagine que cela ne vous dis sans doute pas grand chose, disons que c'est de la Domotique.

La Domotique
============

Le [Home Energy Management System](https://www.otovo.fr/blog/le-solaire-et-vous/home-energy-management-system/) ou HEMS est la partie de la domotique qui cherche à piloter la consommation et la production électrique (Quand c'est possible) pour l'optimiser.


Vous savez sans doute que la Domotique consiste à mettre des capteurs et actionneurs dans la maison pour la rendre "intelligente" ou plutôt pour l'informatiser. Le principe est simple, c'est qu'avec des processeurs, donc du code, on est capable de récupérer des information de capteurs et de lancer des actionneurs.


Mais pour beaucoup la domotique se limite à la présence de capteurs/actionneurs activés manuellement depuis une jolie interface sur internet. On entends par là tous les appareils dit "connectés". On peut tout de même automatiser un peu certaines tâches via ces interfaces (sur timers ou déclencheurs) ou même y interagir via des API ce qui permet de faire de véritables programme. Seulement ce n'est pas à la portée de beaucoup mais certains s'y lance.

Peut-être, pour vous, soucieux de l'open-source et de votre vie-privé, cela se gère via [Home-Assistant](https://www.home-assistant.io/) ou [Jeedom](https://www.jeedom.com/) ou d'autres encore. Dans la suite de l'article, je parlerais d'Home-Assistant pour parler de ces logiciels de domotique car c'est le plus complet et répandu. Ces logiciels permettent de gérer des appareils connecté mais pas pas nécessairement connectés à internet directement. Ces appareils peuvent être connectés via des réseaux moins énergivores comme ZigBee et Matter. Ils ne sont alors accessible depuis internet que si votre Home-Assitant l'est.

Via cette domotique on peut gérer, on peut ainsi gérer la sécurité (serrure intelligentes, vidéo-surveillance, alarmes... ), son confort (lumière, chauffage)...

En fait on peut voir Home-Assistant comme le Système d'Exploitation de la maison au même titre que Linux l'est sur votre PC. Il comporte des "drivers" pour l'ensemble des appareils connectés qu'il gère. Et par dessus on peut ajouter des logiciels, qui permettent de donner des fonctionnalités supplémentaires. De base,  il exise "Home-Assistant OS" (installable hélas que sur le Raspberry PI) qui en quelque sorte est livré avec des "intégration" installables qui sont des logiciels qui ajoutent des fonctionnalités.

L’Énergie
=========

Ici, on s'intéresse à ce qui concerne l'énergie dans la maison plus précisément la consommation électrique. On va chercher à améliorer la maîtrise de la facture électrique en optimisant la consommation.


Le principe est de différer une partie significative de la consommation électrique. Clairement, on adapte rarement la production (Les panneaux solaires ou éoliennes ne sont pas pilotables). On pourrait se poser la question pour les batteries ou il pourrait en théorie être parfois intéresant de les charger aux heures creuses pour les décharger aux heures pleines.

Évidemment pour la plupart des appareils du quotidiens on ne peut pas retarder ou avancer leur utilisation. Four micro-onde, télévisions et ordinateurs ne sont pas concernés. Mais la pluspart des appareils gros consommateurs le sont au moins en partie. Pour ma part, cela concerne, le lave-linge, sèche-linge, lave-vaisselle, la charge de la voiture électrique, le four pour la cuisson du pain. Notons aussi qu'il y a les charges des appareils électrique autonomes ou à batterie (tondeuse, aspirateur). C'est répandu même si je n'en dispose pas. Chacun doit faire son analyse.

But recherché
-------------

* Si vous disposez d’un forfait à prix du kilowatt-heure variable, on va chercher à déclencher les appareils aux heures creuses. Cela va mécaniquement rentabiliser ces heures creuses et baisser la facture. NB: Pour que les heures creuses soit rentable, il faut d'après les études que j'ai vu arriver, à peu près, à 50% de consommation en heures creuses. Suivant votre configuration, c'est plus ou moins facile.

* Si vous disposez de panneaux solaires, d’une éolienne ou de tout autre système de production électrique on va chercher a déclencher les appareils au moment ou la production dépasse la consommation. Cela à 2 but: limiter la revente qui n’est jamais avantageuse financièrement et limiter les cycles de charge/décharge des batteries qui les usent et sont donc à éviter.

Les moyens disponibles
----------------------

Outre le fait de disposer d'un appareils que l'on peut théoriquement différé, encore faut-il pouvoir le piloter depuis un programme. Autrement dit il va faloir en faire un appareils "connecté".

* Certains le sont de base sur le réseau, c’est notamment le cas des appareils dit « connectés » tels certains lave-linge ou lave-vaisselles modernes. Hélas, ils sont souvent connecté en WiFi, qui est certes une solution polyvalente, mais relativement beaucoup consommatrice d’électricité par ailleurs, surtout pour une utilisation H24, et encore plus si l'appareil est loin de la box internet.

* Pour tout appareil capable de se mettre en marche dès que le courant est disponible, on peut le brancher sur une prise connecté (ou relai pour les plus énergivores). Cela concerne les anciennes machine (sans software ou très peu), les voiture électriques, pompe à chaleur...

* Certains appareils sont sur batterie comme des aspirateur ou tondeuses, ou un système nettoyeur de piscine a fortiori les appareils automatique.

* Le cas du chauffe-eau est à part. Si on est en heures creuses, c'est automatique. S’il est résistif, on pourra mettre un routeur photovoltaïque type [F1ATB](https://f1atb.fr/fr/routeur-photovoltaique-simple-a-realiser/). Le routeur photovoltaïque permet par hachage de la tension d'envoyer une portion adaptative du courant. Autrement dit, il peut consommer autant de watt que l'on veut. Cela permet de maintenir en permanence la consommation électrique à 0. Sinon on pourra se contenter d'une simple prise connecté.

PS : Dans l'HEMS, ou plutôt EMS, il existe toute une partie qui n'est pas vraiment domotique : La gestion à l'échelle des énergéticiens ou a minima des imeubles. C'est le cas d'[OpenEMS](https://github.com/OpenEMS/openems) ou [MyEMS](https://github.com/MyEMS/myems).

Remarques
---------

Pour lancer les appareils électriques en heures creuses seulement, on peut se contenter d'un [contacteur heures-creuse](https://particuliers.alpiq.fr/guide-energie/entretien-et-equipements/contacteur-heures-creuses) mais alors on a aucun contrôle ssur la puissance et donc si trop d'appareils sont dessus, on risque de faire sauter les plombs. Ensuite on dispose d'aucun contrôle sur la durée. En ce qui me concerne, je ne voulais pas que ma voiture électrique se recharge à plus de 80% pour préserver la batterie.

Pour les panneaux solaires, il existe bien des solutions commerciales, mais outre ce côté non-libre, à ma connaissance elle n'offre aucun contrôle sur les paramètres (Quand sont lancé quoi, ce sont des boites noires). Et en plus souvent elles demande d'avoir tout l'ensemble des appareils de la même marques (a minima les batteries, panneaux solaires, gestionnaire...)

La solution OpenHEMS
====================

Présentation générale
---------------------

[OpenHEMS](https://github.com/abriotde/openhems-sample/) est une solution open-source sous licence GPLv3 qui ambitionne de le faire. On peut l'installer depuis les sources à l'aide de [scripts shell](https://github.com/abriotde/openhems-sample/blob/main/scripts/openhems.sh) ou plus simplement à l'aide d'un container docker avec l'image ghcr.io/abriotde/openhems-sample:main encore faut il auparavent installer Home-Assistant. Sinon on peut commander l'[appareil préinstallé sur le site](https://openhomesystem.com/product/openhems-server/)

L'application est développée en Python et s'appuie entre autre sur 2 projets Open-Source (En Python) qui réalisent une partie du travail:

* Home-Assistant que je n'ai plus besoin de présenter. Il sert de "driver" pour interagir sur les appareils via son API. Il serait conceptuellement possible d'implémenter directement les drivers dans OpenHEMS. Cela aurait l'avantage, de consommer moins de ressource mais empêcherait de disposer de l'interface conviviale de Home-Assistant.

* [Emhass](https://github.com/davidusb-geek/emhass), un des projet Open-Source, sous licence MIT, qui, selon mes recherche est ce qui est le plus abouti dans le domaine HEMS. Et puis il est développé par un français. Il a l'avantage de bien gérer les panneaux solaires avec une IA et une recherche des prévisions météo... mais la mise en place et la gestion des appareils est manuelle après.


Fonctionnalités
---------------

Voici les principales fonctionnalités importantes disponibles sur OpenHEMS:

* IHM : Une intégration à Home-Assistant est fournie (même si elle est encore imparfaite) et permet de demander aux appareils pilotables de fonctionner. C'est aussi disponible sur l'interface de l'application mobile Home-Assistant. La limitation principale actuelle est que l'on doit être dans le réseau de la maison. Depuis l'extérieur c'est possible en payant (Fournisseur d'Home-Assistant) ou plus simplement en ouvrant les ports de sa box internet (et configurant HTTPS) mais ce n'est pas à la portée de tous et peut-être pas parfait point de vue sécurité.

* La configuration du réseau se fait via un fichier YAML unique. Il serait sans doute possible de faire une auto-détection partielle des appareils disponible mais ce n'est pas fait. Et la configuration n'est pas encore possible via IHM. C'est un gros chantier qui serait utile.

* 2 modes sont disponible: Un mode heure-creuse (offpeak), et un mode "panneaux solaire" (emhass). Il y a beaucoup de mode que l'on pourrait rajouter mais ce n'est plus vraiment ma priorité (Ce n'est pas l'envie qui me manque).

* Et d'autres dont l'envoi de notification sur l'IHM Home-Assistant pour être prévenu en cas de problèmes.


**Fonctionnalités à venir**


* J'aimerai aussi ajouter la possibilité de programmer des appareils "manuels". Je m'explique. Imaginons que l'on ai un bon vieux lave-vaisselle que l'on ne peut donc pas mettre dans l'application. mais on pourrait dire "Je veuxc mettre 2 heures d'appareil manuel" sur l'IHM. Et alors l'application enverrai  un rappel sous forme de notification à l'application Home-Assistant au moment opportun. (Peut-être à l'avenir aussi autrement: jouer de la musique sur l'enceinte connecté, envoyer un mail...)

* J'ai commencé a travaillé sur une fonctionnalités d'extinction d'appareils suite a des questions du style "J'ai compris, genre il éteint la box la nuit?". C'est peu utile à priori et assez complexe mais commercialement je pense que c'est nécéssaire.

Pour le reste cf [todo.md](https://github.com/abriotde/openhems-sample/blob/main/todo.md)

Conclusion
==========

Il y aurait encore beaucoup a dire et plus encore à faire. Mais je vais en rester là. N'hésitez pas à revenir vers moi en commentaires ou par mail.

Si j'ai fais journal, je le concède c'est aussi pour faire la promotion de la solution OpenHEMS que je développe. Ce que j'aimerais, c'est que certains d'entre vous s'y intéresse pour pouvoir me faire des retours. Ce qui m'intéresse, c'est entre-autre que vous êtes dans l'ensemble capable de l'installer, de le configurer et d'investiguer seul en cas de problème. Idéalement j'aimerais donc, des personnes qui l'installeraient. Mais a défauts, si certains pouvaient me faire des retours sur leurs propres alternatives ou solutions, pouvaient analyser le code ou encore pouvaient en faire la promotion autour d'eux ce serait bien.


PS: Je pense que je ferais par la suite un journal, plus bref, sur Python...
