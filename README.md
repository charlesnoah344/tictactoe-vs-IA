# Tic Tac Toe avec IA

Projet Tic Tac Toe en Python avec une interface graphique `pygame` et une IA basee sur l'algorithme minimax.

Le joueur choisit d'incarner `X` ou `O`, puis affronte l'ordinateur, qui joue de maniere optimale.

## Fonctionnalites

- Partie jouable en interface graphique.
- Choix du camp au demarrage: `X` ou `O`.
- IA utilisant `minimax` pour trouver le meilleur coup.
- Detection automatique de la victoire, du match nul et de la fin de partie.

## Démo vidéo



## Pre requis

- Python 3.10 ou superieur.
- `pygame` installe.

Le projet utilise aussi la police `OpenSans-Regular.ttf`. Le fichier doit se trouver dans le meme dossier que `runner.py` pour que l'interface se lance correctement.

## Installation

Depuis le dossier du projet:

```bash
pip install -r requirements.txt
```

## Lancer le jeu

```bash
python runner.py
```

Une fenetre s'ouvre. Vous pouvez alors:

1. Choisir de jouer en `X` ou en `O`.
2. Cliquer sur une case vide pour jouer.
3. Laisser l'ordinateur repondre automatiquement.
4. Relancer une partie avec le bouton `Play Again` a la fin.

## Lancer les tests

Les tests unitaires verifient la logique du jeu: etat initial, joueur courant, actions possibles, victoire, fin de partie et utilite.

```bash
pytest test.py
```

## Structure du projet

- `tictactoe.py`: logique du jeu et IA minimax.
- `runner.py`: interface graphique avec `pygame`.
- `test.py`: tests unitaires.
- `requirements.txt`: dépendances Python.

## Remarque

Ce projet correspond a la version CS50 AI du morpion. Si vous deplacez les fichiers, pensez a garder `runner.py`, `tictactoe.py`, `test.py` et `OpenSans-Regular.ttf` dans le meme dossier ou a adapter les chemins dans le code.
