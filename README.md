# Smart_Terrain- Stade intelligent développer avec Raspberry Pi et Arduino

Smart_Terrain est un projet intelligent basé sur Raspberry Pi, vision par ordinateur et Arduino, permettant de détecter automatiquement les buts dans un terrain miniature, d’enregistrer les actions, d’afficher le score en temps réel et de gérer un éclairage automatique.

Objectifs du projet :

Automatiser la détection des buts sans intervention humaine :
Enregistrer chaque but sous forme de vidéo
Afficher le score en temps réel
Fournir une interface simple et intuitive
Mettre en œuvre une solution IoT complète (Raspberry Pi + Arduino)

Architecture du système :

Raspberry Pi : traitement vidéo, détection et interface
Caméra Raspberry Pi : capture vidéo
OpenCV : détection du ballon
GPIO : gestion buzzer
Arduino + capteur PIR : éclairage automatique
Tkinter : interface graphique utilisateur

Fonctionnement du système :
Détection de but :

Capture vidéo via Picamera2
Détection du ballon par HoughCircles
Définition d’une zone de but virtuelle
Incrémentation automatique du score
Activation d’un buzzer
Enregistrement vidéo du but détecté

Interface graphique :

Affichage du score en temps réel
Liste des vidéos enregistrées
Lecture des vidéos via VLC
Rafraîchissement automatique chaque seconde

Éclairage automatique :

Capteur PIR pour détecter la présence
Allumage automatique de l’éclairage
Système indépendant mais intégré au projet global

Prérequis matériels :

Raspberry Pi (OS 64-bit recommandé)
Caméra Raspberry Pi
LED
Buzzer
Arduino Uno
Capteur PIR
Breadboard et câblage

Prérequis logiciels :

Python 3.10+
OpenCV
Picamera2
Tkinter
VLC Media Player
Arduino IDE

Équipe de projet

Réaliser par :

[@kadimAmina](https://github.com/kadimAmina)

[@JEFFALI-Wiam](https://github.com/JEFFALI-Wiam)

[@Malakmelaygi](https://github.com/Malakmelaygi)

[@fatimazahrabenhaddou24-prog](https://github.com/fatimazahrabenhaddou24-prog)

Encadré par :

Mr.AZIZI Mostafa
