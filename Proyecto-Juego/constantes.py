from clases import *


JUGADOR = "imagenes/jugador.png"
MIKE = "imagenes/1.png"
MUHAMMED = "imagenes/2.png"
BRUCE = "imagenes/3.png"
CONOR = "imagenes/4.png"
FLOYD = "imagenes/5.png"
MANNY = "imagenes/6.png"
ANDERSON = "imagenes/7.png"


TITULO = "TORNEO DE LEYENDAS"

JUGADOR_1 = Jugador("Nombre",
                    salud=100,
                    ataque=1000,
                    defensa=7,
                    imagen=JUGADOR)

nombres_peleadores = [
    "Mike Tyson",
    "Muhammad Ali",
    "Bruce Lee",
    "Conor McGregor",
    "Floyd Mayweather Jr.",
    "Manny Pacquiao",
    "Anderson Silva"
]

objetoMIKE = Objeto("Guantes de Mike Tyson", 4, 0)
objetoMUHAMMAD = Objeto("Pantalones de Muhammad Ali", 0, 5)
objetoBRUCE = Objeto("Nunchakus de Bruce Lee", 5, 0)
objetoCONOR = Objeto("Sombrero de Conor McGregor", 2, 2)
objetoFLOYD = Objeto("Anillo de Floyd Mayweather Jr.", 3, 2)
objetoMANNY = Objeto("Vendas de Manny Pacquiao", 2, 7)
objetoANDERSON = Objeto("Rodilleras de Anderson Silva", 4, 10)

objetos = [
    objetoMIKE,
    objetoMUHAMMAD,
    objetoBRUCE,
    objetoCONOR,
    objetoFLOYD,
    objetoMANNY,
    objetoANDERSON
]

historias = [
    "Mike Tyson es un exboxeador profesional estadounidense considerado uno de los mejores pesos pesados de todos los\
    tiempos.Conocido por su poderoso golpe y estilo agresivo, Tyson se convirtió en el campeón mundial más joven de la\
    historia de los pesos pesados.Su carrera estuvo llena de éxitos y controversias, y se le recuerda como uno de los\
    mayores noqueadores en la historia del boxeo.",
    "Muhammad Ali, nacido como Cassius Clay, fue un legendario boxeador estadounidense. Reconocido como uno de los mejores boxeadores de todos los tiempos, "
    "Ali fue conocido por su velocidad, agilidad y habilidades defensivas. Ganó el título mundial de pesos pesados en varias ocasiones y se destacó por su "
    "personalidad carismática y su activismo político y social.",
    "Bruce Lee fue un actor y artista marcial chino-estadounidense. Considerado una de las mayores figuras en la historia de las artes marciales, "
    "Lee desarrolló su propio estilo de combate llamado Jeet Kune Do. Además de su influencia en el cine de artes marciales, "
    "Lee promovió la filosofía de la automejora, la autenticidad y la expresión personal en las artes marciales.",
    "Conor McGregor es un peleador de artes marciales mixtas (MMA) irlandés. Es conocido por su personalidad extrovertida y su estilo de lucha agresivo."
    "McGregor ha competido en la UFC (Ultimate Fighting Championship) en varias categorías de peso y se ha convertido en "
    "una de las figuras más reconocibles y exitosas en el mundo de las MMA.",
    "Floyd Mayweather Jr. es un exboxeador estadounidense y uno de los más exitosos en la historia del deporte. "
    "Es conocido por su habilidad defensiva y su estilo de lucha técnico. Mayweather se retiró invicto en su carrera profesional, "
    "habiendo ganado múltiples títulos mundiales en diferentes categorías de peso y enfrentado a algunos de los mejores boxeadores de su generación.",
    "Manny Pacquiao es un boxeador y político filipino. Es considerado uno de los mejores boxeadores en la historia del peso welter. "
    "Pacquiao ha ganado títulos mundiales en múltiples categorías de peso y ha participado en peleas memorables contra algunos de los nombres más importantes del boxeo. "
    "También ha incursionado en la política y es conocido por su filantropía en Filipinas.",
    "Anderson Silva es un expeleador brasileño de artes marciales mixtas. Conocido por su estilo fluido y preciso, "
    "Silva fue considerado uno de los mejores peleadores de la UFC en su época. Ganó el título de peso medio de la UFC y "
    "estableció récords de defensa de título y de victorias consecutivas. Silva también ha destacado en otras disciplinas de combate, como el muay thai y el jiu-jitsu brasileño."

]

l_imagenes = [MIKE,
          MUHAMMED,
          BRUCE,
          CONOR,
          FLOYD,
          MANNY,
          ANDERSON
]


ENEMIGOS = []
salud_base = 50
ataque_base = 15
defensa_base = 7

for i in range(len(nombres_peleadores)):
    nombre = nombres_peleadores[i]
    salud = salud_base + (i * 10)
    ataque = ataque_base + (i * 5)
    defensa = defensa_base + (i * 2)
    objeto = objetos[i]
    imagen = l_imagenes[i]
    historia = historias[i]

    ENEMIGOS.append(Enemigo(nombre, salud, ataque, defensa, objeto, imagen, historia))


Historia1 = "Eres un valiente guerrero cuyo espiritu indomable lo ha llevado a enfrentar grandes desafios. Desde joven,\n" \
            "sonabas con convertirte en el campeon definitivo, aquel cuyo nombre resonaria en los corazones de todos los\n" \
            "que presenciaron sus hazanas. Has recorrido tierras lejanas, entrenando incansablemente para perfeccionar tus\n" \
            "habilidades marciales. Tu determinacion y dedicacion han forjado tu cuerpo y mente en un arma letal, capaz de\n" \
            "derrotar cualquier obstaculo que se interponga en tu camino. Ahora, te encuentras ante el desafio supremo:\n" \

Historia2 = "El TORNEO DE LEYENDAS. Un evento legendario que reune a los guerreros mas formidables del mundo. \n" \
            "Sabes que en esta arena de batalla, tus habilidades seran puestas a prueba al limite."


textosderrotas = []
derrota1 = "Puedes celebrar tu triunfo momentáneo, pero no te engañes pensando que esto marca el fin. Mi derrota hoy solo alimenta mi determinación para resurgir con más fuerza. \n" \
           "Estudiaré tus debilidades, trazaré nuevas estrategias y cuando menos lo esperes, estaré de vuelta para cobrar venganza. \n" \
           "No te duermas en tus laureles, porque te aseguro que mi sed de revancha no descansará hasta verte caer en la oscuridad de la derrota definitiva. Este no es el final, es solo un capítulo más en nuestra eterna rivalidad."
derrota2 = "No te regodees en tu victoria, solo has tenido suerte esta vez. La próxima vez que nos enfrentemos, te aplastaré sin piedad."
derrota3 = "Tu triunfo de hoy solo es un espejismo. Me levantaré más fuerte, más audaz y con sed de venganza. Prepárate para enfrentar mi ira desatada."
derrota4 = "No te engañes creyendo que esta derrota te hace invencible. Cada caída nos enseña valiosas lecciones. La próxima vez que nos crucemos, estaré preparado para superarte."
derrota5 ="Celebra tu momentáneo triunfo, pero ten en cuenta que mi determinación no se debilita. Cada golpe que recibes solo fortalece mi determinación para verte caer."
derrota6 ="Hoy has vencido, pero el destino es caprichoso. Mañana podría ser yo quien risueñamente celebre tu caída. Esta batalla no ha terminado, es solo un episodio más en nuestra eterna contienda."
derrota7 ="Disfruta de tu victoria efímera mientras puedas, pues pronto me levantaré de las cenizas. Con cada derrota, mi sed de venganza se intensifica. Prepárate para el día en que mi resurgimiento te haga temblar."
derrota8 = "Tu victoria es solo un engaño momentáneo. Mi espíritu indomable se fortalece con cada derrota. No te confíes, pues cuando menos lo esperes, estaré de vuelta para reclamar mi lugar y borrar tu triunfo de la faz de la tierra."

textosderrotas.append(derrota1)
textosderrotas.append(derrota2)
textosderrotas.append(derrota3)
textosderrotas.append(derrota4)
textosderrotas.append(derrota5)
textosderrotas.append(derrota6)
textosderrotas.append(derrota7)
textosderrotas.append(derrota8)

FUENTETEXTO = "VCRosdNEUE"

textoinformacion = """
El relato de un valiente guerrero cuyo espíritu indomable lo lleva a enfrentar grandes desafíos es una base fantástica para una aventura llena de acción y heroísmo. 
Desde joven, el protagonista sueña con convertirse en el campeón definitivo, un nombre que resonará en los corazones de todos aquellos que presencien sus hazañas.
A lo largo de la trama, el guerrero recorrerá tierras lejanas, entrenando incansablemente para perfeccionar sus habilidades marciales. 
Su determinación y dedicación lo convertirán en un arma letal, capaz de superar cualquier obstáculo en su camino. 
Y ahora, se enfrenta al desafío supremo: el Torneo de Leyendas, un evento legendario que reúne a los guerreros más formidables del mundo.
En esta arena de batalla, el protagonista sabe que sus habilidades serán puestas al límite. El jugador se embarcará en una serie de desafíos y combates emocionantes, 
donde deberá utilizar las habilidades marciales del guerrero para enfrentarse a oponentes poderosos y demostrar su valía. 
A medida que avanza en el torneo, el protagonista ganará reconocimiento y se acercará cada vez más a convertirse en el campeón definitivo.
Con gráficos impresionantes, mecánicas de juego desafiantes y una historia envolvente, este juego ofrecerá una experiencia llena de emoción y aventura para los jugadores. 
¡Que comience el Torneo de Leyendas y que el nombre del valiente guerrero se convierta en una leyenda!
"""


formadecombate = '''
Torneo de Leyendas es un juego RPG por turnos. A continuacion se muestra el funcionamiento de los botones:
JAB: Utilizalo para hacer daño al oponente
DEFENDER: Aumenta tu defensa
GANCHO: Utilizalo para hacer un ataque con X2 de daño! (Puedes utilizarlo cada 3 turnos)

Los objetos que obtengas tambien de daran habilidades especiales, solo puedes usar uno cada 2 turnos!
'''

ESTADO_BOTON = "disabled"