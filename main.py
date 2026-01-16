import turtle
# Importation des fonctions depuis turtle_scene.py
from turtle_scene import initialiser_fenetre,dessiner_carrefour


screen = initialiser_fenetre()
dessiner_carrefour()
screen.update()  # Met à jour l'écran après le dessin
screen.mainloop()
