class Being(object):
    """tengo pensado meter otras clases mas adelante"""
    def __init__(self, name, hp, strenght, defense):
        self.name = name
        self.hp = hp  # health
        self.strenght = strenght
        self.defense = defense  # reduce el ataque recibido. Si es 0.25, damage = ###*0.75

    def attack(self, other):
        """
        Lo mas basico por ahora.
        self va a atacar a other, y pertenecen ambos al menos a la clase being
        Incluye el resultado del ataque en la pantalla
        """
        print(self.name, "attacks", other.name)
        damage = self.strenght*(1.-other.defense)
        print("damage: ", damage)
        other.hp -= damage
        print(other.name+"'s remaining health: ", other.hp,)
        print("----------")


# definimos a los participantes
Andrew = Being("Andrew", 50., 8., 0.1)
Borja = Being("Borja", 60., 7., 0.09)
# fight!!
while True:
    Andrew.attack(Borja)
    if Borja.hp <= 0:
        print(Borja.name, "died")
        break
    Borja.attack(Andrew)
    if Andrew.hp <= 0:
        print(Andrew.name, "died")
        break
