import turtle

# =======================
# VARIABLES GLOBALES
# =======================
pen = None
LARGEUR_ECRAN = 0
HAUTEUR_ECRAN = 0

LARGEUR_ROUTE = 120
ROND_POINT = 40
MARGE = 10


# =======================
# INITIALISATION FENÊTRE
# =======================
def initialiser_fenetre():
    global pen, LARGEUR_ECRAN, HAUTEUR_ECRAN

    screen = turtle.Screen()
    screen.title("Carrefour routier - Simulation")
    screen.setup(width=1.0, height=1.0)  # plein écran
    screen.bgcolor("white")

    LARGEUR_ECRAN = screen.window_width()
    HAUTEUR_ECRAN = screen.window_height()

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    return screen


# =======================
# OUTILS DE DESSIN
# =======================
def dessiner_rectangle(x, y, largeur, hauteur, couleur):
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(couleur)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(largeur)
        pen.right(90)
        pen.forward(hauteur)
        pen.right(90)
    pen.end_fill()
    pen.penup()


# =======================
# ROUTES
# =======================
def dessiner_route_carrefour():
    # Route verticale
    dessiner_rectangle(
        -LARGEUR_ROUTE / 2,
        HAUTEUR_ECRAN / 2,
        LARGEUR_ROUTE,
        HAUTEUR_ECRAN,
        "dimgray"
    )

    # Route horizontale
    dessiner_rectangle(
        -LARGEUR_ECRAN / 2,
        LARGEUR_ROUTE / 2,
        LARGEUR_ECRAN,
        LARGEUR_ROUTE,
        "dimgray"
    )


# =======================
# ROND-POINT CENTRAL
# =======================
def dessiner_rond_point_central():
    pen.goto(0, -ROND_POINT)
    pen.color("white")
    pen.begin_fill()
    pen.pendown()
    pen.circle(ROND_POINT)
    pen.end_fill()
    pen.penup()


# =======================
# MARQUAGES CENTRAUX
# =======================
def dessiner_marquage_central():
    pen.color("white")
    pen.width(4)

    # Vertical haut
    pen.goto(0, HAUTEUR_ECRAN / 2 + HAUTEUR_ECRAN /20)
    pen.setheading(270)
    pen.pendown()
    pen.forward(HAUTEUR_ECRAN / 2  - HAUTEUR_ECRAN /20)
    pen.penup()

    # Vertical bas
    pen.goto(0, -ROND_POINT - MARGE + HAUTEUR_ECRAN /20)
    pen.pendown()
    pen.forward(HAUTEUR_ECRAN / 2 - ROND_POINT - MARGE - HAUTEUR_ECRAN /20)
    pen.penup()

    # Horizontal gauche
    pen.goto(-LARGEUR_ECRAN / 2, 0)
    pen.setheading(0)
    pen.pendown()
    pen.forward(LARGEUR_ECRAN / 2 - ROND_POINT - MARGE)
    pen.penup()

    # Horizontal droite
    pen.goto(ROND_POINT + MARGE, 0)
    pen.pendown()
    pen.forward(LARGEUR_ECRAN / 2 - ROND_POINT - MARGE)
    pen.penup()


# =======================
# PASSAGES PIÉTONS
# =======================
def dessiner_passages_pietons():
    pen.color("white")
    pen.width(7)

    nb_bandes = 10
    espacement = 10
    longueur_bande = 20

    largeur_utile = LARGEUR_ROUTE - (nb_bandes - 1) * espacement
    largeur_bande = largeur_utile / nb_bandes

    offset = ROND_POINT + MARGE + longueur_bande

    # Routes verticales
    x_depart = -LARGEUR_ROUTE / 2 - longueur_bande / 2
    for y in [offset, -offset]:
        x = x_depart
        for _ in range(nb_bandes):
            pen.goto(x, y)
            pen.setheading(270)
            pen.pendown()
            pen.forward(longueur_bande)
            pen.penup()
            x += largeur_bande + espacement

    # Routes horizontales
    y_depart = -LARGEUR_ROUTE / 2 - longueur_bande
    for x in [offset, -offset]:
        y = y_depart
        for _ in range(nb_bandes):
            pen.goto(x, y)
            pen.setheading(0)
            pen.pendown()
            pen.forward(longueur_bande)
            pen.penup()
            y += largeur_bande + espacement


# =======================
# CARREFOUR COMPLET
# =======================
def dessiner_carrefour():
    dessiner_route_carrefour()
    dessiner_rond_point_central()
    dessiner_marquage_central()
    dessiner_passages_pietons()


# =======================
# PROGRAMME PRINCIPAL
# =======================
screen = initialiser_fenetre()
dessiner_carrefour()
screen.mainloop()
