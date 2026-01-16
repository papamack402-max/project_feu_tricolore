# feux.py
import turtle

# =========================
# BOÎTIERS OVALES
# =========================
def dessiner_boitier_ovale_horizontal(pen, x, y, largeur, hauteur, couleur):
    """
    Dessine un boîtier de forme ovale horizontale.
    x, y : coin supérieur gauche du boîtier
    largeur : largeur horizontale
    hauteur : hauteur verticale
    couleur : couleur du boîtier
    """
    # Centre de l'ovale
    x_centre = x + largeur / 2
    y_centre = y - hauteur / 2

    pen.goto(x_centre, y_centre)
    pen.color(couleur)
    pen.begin_fill()
    pen.pendown()
    pen.turtlesize(stretch_wid=hauteur/20, stretch_len=largeur/20)  # élargit horizontalement
    pen.shape("circle")
    pen.stamp()
    pen.end_fill()
    pen.penup()


def dessiner_boitier_ovale_vertical(pen, x, y, largeur, hauteur, couleur):
    """
    Dessine un boîtier de forme ovale verticale.
    x, y : coin supérieur gauche du boîtier
    largeur : largeur horizontale
    hauteur : hauteur verticale
    couleur : couleur du boîtier
    """
    # Centre de l'ovale
    x_centre = x + largeur / 2
    y_centre = y - hauteur / 2

    pen.goto(x_centre, y_centre)
    pen.color(couleur)
    pen.begin_fill()
    pen.pendown()
    pen.turtlesize(stretch_wid=hauteur/20, stretch_len=largeur/20)  # vertical
    pen.shape("circle")
    pen.stamp()
    pen.end_fill()
    pen.penup()

# =========================
# FEUX
# =========================
def dessiner_feu_ovale_horizontal(x, y):
    """
    Dessine un feu tricolore horizontal.
    x, y : coin supérieur gauche du boîtier
    """
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    # Dimensions du boîtier
    largeur = 90
    hauteur = 40
    rayon_lumiere = 10

    # Boîtier
    dessiner_boitier_ovale_horizontal(pen, x, y, largeur, hauteur, "black")

    # Feux alignés horizontalement
    couleurs = ["red", "orange", "green"]
    marge_laterale = 6
    espacement_horizontal = (largeur - 2 * marge_laterale) / len(couleurs)

    for i, couleur in enumerate(couleurs):
        x_cercle = x + marge_laterale + (i + 0.5) * espacement_horizontal
        y_cercle = y - hauteur / 2
        pen.goto(x_cercle, y_cercle)
        pen.color(couleur)
        pen.begin_fill()
        pen.pendown()
        pen.circle(rayon_lumiere)
        pen.end_fill()
        pen.penup()


def dessiner_feu_ovale_vertical(x, y):
    """
    Dessine un feu tricolore vertical.
    x, y : coin supérieur gauche du boîtier
    """
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    # Dimensions du boîtier
    largeur = 40
    hauteur = 90
    rayon_lumiere = 10

    # Boîtier
    dessiner_boitier_ovale_vertical(pen, x, y, largeur, hauteur, "black")

    # Feux alignés verticalement
    couleurs = ["red", "orange", "green"]
    marge_haut_bas = 6
    espacement_vertical = (hauteur - 2 * marge_haut_bas) / len(couleurs)

    for i, couleur in enumerate(couleurs):
        x_cercle = x + largeur / 2
        y_cercle = y - marge_haut_bas - (i + 0.5) * espacement_vertical
        pen.goto(x_cercle, y_cercle)
        pen.color(couleur)
        pen.begin_fill()
        pen.pendown()
        pen.circle(rayon_lumiere)
        pen.end_fill()
        pen.penup()
