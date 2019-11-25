# coding=utf-8

import sys
import sqlite3

class Weapon:

    def __init__(self, name, damage, durability):
        self.n = name
        self.da = damage
        self.du = durability

    def get_name(self):
        return self.n

    def get_damage_amount(self):
        return self.da

    def get_durability(self):
        return self.du

def UPDATE():

    print("")
    print("UPDATE")
    for player in inlife_players:

        print("Le joueur ", player.get_name(), " a ", player.get_health(), " points de vie, ", player.get_attack(),
              " points d'attaque et ", player.get_armor(), "points d'armure.")
        if player.get_durability() == "None" or type(player.get_durability()) != str:

            print("Il n'a pas d'arme")

        else:

            print("Son arme a ", player.get_durability(), " de durabilité et ", player.w.get_damage_amount(),
                  " d'attaque.")

    if len(dead_player) != 0:
        if len(dead_player) > 1:
            print ("\nLes joueur morts sont :\n")

        else:
            print ("\nUn joueur est mort, c'est :\n")

        for player in dead_player:
            print(player.get_name(), " qui avait ", player.get_attack(),
                  " points d'attaque et ", player.get_armor(), "points d'armure.")

    x = input("")
    MENU()

def SAVE():

    connection = sqlite3.connect("BaseP.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM iai_player')

    for player in inlife_players:
        player_name = str(player.n)
        player_health = int(player.h)
        player_attack = int(player.a)

        if player.w != "None":
            player_weapon = str(player.w)
        else:
            player_weapon = "None"

        player_armor = int(player.ar)
        player_durability = int(player.d)

        cursor.execute('INSERT INTO iai_player (player_name, player_health, player_attack, player_weapon, player_armor, player_durability, player_life) values (?, ?, ?, ?, ?, ?, 1)', (player_name, player_health, player_attack, player_weapon, player_armor, player_durability))

    for player in dead_player:
        player_name = str(player.n)
        player_attack = int(player.a)
        player_armor = int(player.ar)

        cursor.execute('INSERT INTO iai_player (player_name, player_health, player_attack, player_weapon, player_armor, player_durability, player_life) values (?, 0, ?, ?, ?, 0, 0)', (player_name, player_attack, "None", player_armor))

    x = input("Données sauvegardées\nTappez ENTRER pour retourner au menu\n")
    connection.commit()
    MENU()

def QUIT():

    INPUT = input("Toute données non sauvegardées sera suprimée !\nOK : [ok]\nRETOUR : [autre touche]\n")

    if INPUT == "ok":
        sys.exit("A Bientôt")

    else:
        MENU()

def DELETE_DEAD():

    ALERT = input("étes vous sur de vouloir suprimer la liste des morts ?\n"
                  "Cette action est irreversible !!!\n"
                  "Tappez [YES] pour suprimer.\n"
                  "Pour retourner au menu tappez ENTRER")

    if ALERT == "YES":
        connection = sqlite3.connect("BaseP.db")
        cursor = connection.cursor()
        cursor.execute('DELETE FROM iai_player WHERE player_life = 0')
        connection.commit()
        x = input("Morts Suprimée ...\n")
        del dead_player[:]

    MENU()

def CREATE_PLAYER():

    x = input("IN PROGRESS ...\nTappez ENTRER pour revenir au menu\n")
    MENU()

def MENU():
    INPUT = input("Si vous voulez une update, tappez [u]\n"
                  "Si vous voulez quitter, tappez [q]\n"
                  "Si vous voulez Détruire la liste des morts, tappez [d]\n"
                  "Si vous voulez créer une personnage, tappez [p]\n"
                   "Si vous sauvegarde les données, tappez [s]\n"
                   "Si vous voulez retourné au combat, tapper [c]\n"
                  "Puis tapper ENTRER\n")
    print("\n\n")

    if INPUT != "c":

        if INPUT == "u":
            UPDATE()

        if INPUT == "s":
            SAVE()

        if INPUT == "q":
            QUIT()

        if INPUT == "d":
            DELETE_DEAD()

        if INPUT == "p":
            CREATE_PLAYER()

        if INPUT != "u" and INPUT != "s" and INPUT != "q" and INPUT != "d" and INPUT != "p":
            print("Entrer une commande valide\n")
            MENU()


def set_weapon_to_player(player, weapon):

    player.set_weapon(weapon)

    if weapon != None:
        print(player.n, " a maintenant un(e) ", weapon.n)

def attack(attaquant, victim):

    attaquant.attack_player(victim)
    print (attaquant.get_name(), "attaque", victim.get_name())
    x = input("")

def start_UPDATE_weapon():

    for weapon in create_weapon:
        print("Création de l'arme : ", weapon.get_name(), "/ Durabilitée de base :", weapon.get_durability(), "/ Attaque:",
          weapon.get_damage_amount())

    print("")

def start_UPDATE_player():

    for player in inlife_players:
        print("Bienvenue au joueur", player.get_name(), "/ Points de vie:", player.get_health(), "/ Attaque:",
          player.get_attack(), "/ Armure:", player.ar)

    print("")

def start_UPDATE_DEAD_player():

    for player in dead_player:
        print("Le joueur", player.get_name(), " est mort, il avait ", player.a, " d'attaque et ", player.ar, " d'armure")

    print("")

def start_UPDATE_gave_weapon():

    for player in inlife_players:
        if player.has_weapon() != None:
            print("Le joueur ", player.n, " a un(e) ", player.w, " comme arme")

        else:
            print("Le joueur ", player.n, " n'a pas d'arme")

    print("")

def isAlive():

    for player in inlife_players:

        playerHp = player.get_health()

        if playerHp <= 0:
            print(player.n, " est mort")
            x = input("")
            inlife_players.remove(player)
            dead_player.append(player)
            return 0

    return 1

def one_survivor():

    if len(inlife_players) <= 1:
        return 1

    else:
        return 0

def Attack_input():

    while one_survivor() == 0:
        print("Quelle joueur attaque ? \n")
        nmoppu = 1

        for player in inlife_players:
            print("le joueur n°: ", nmoppu, " dénomé : ", player.n)
            nmoppu += 1

        true_attack_player = 0
        true_input = 0

        while true_attack_player != 1 :

            if true_input == 0:
                attack_player_input = input("\nInserez un n° : ")

            else:
                attack_player_input = input("\nInserez un autre n° : ")

            if not ( attack_player_input.isdigit()):
                attack_player_input = len(inlife_players) + 1

            nm_of_il_player = len(inlife_players)

            if int(attack_player_input) <= nm_of_il_player:
                true_attack_player = 1

            else:
                print("\n Ce n'est pas un nombre valide")
                true_input = 1

        attack_player = inlife_players[int(attack_player_input)-1]
        attack_player_n = attack_player.n

        print("\nVous avez choisi : ", attack_player_n)

        print("\nQuelle joueur se fait attaquer ? \n")
        nmoppu = 1

        for player in inlife_players:
            if player.n != attack_player_n:
                print("le joueur n°: ", nmoppu, " dénomé : ", player.n)
            nmoppu += 1

        true_input = 0
        fals_input = 0

        while true_input != 1:

            if fals_input == 0:
                victim_player_input = input("\nInserez un n° : ")

            else :
                victim_player_input = input("\nInserez un autre n° : ")

            if not ( victim_player_input.isdigit()):
                victim_player_input = len(inlife_players) + 1

            if int(victim_player_input) > nm_of_il_player:
                print("\n Ce n'est pas un nombre valide")
                true_input = 0
                fals_input = 1

            if victim_player_input == attack_player_input:
                print ("\nLe joueur ne peut pas s'attaquer lui même !")
                true_input =  0
                fals_input = 1

            if victim_player_input != attack_player_input and int(victim_player_input) <= nm_of_il_player:
                victim_player = inlife_players[int(victim_player_input)-1]
                victim_player_n = victim_player.n
                true_input = 1


        print("\nVous avez choisi : ", victim_player_n, "\n")

        attack(attack_player, victim_player)
        isAlive()
        MENU()


    print(inlife_players[0].n, " a gagné(e) !!!\n")
    print("Voila la liste des joueurs mort :\n")

    nd = 0
    for dead in dead_player:
        print(dead.n)
        nd += 1

inlife_players = []
dead_player = []
create_weapon = []

connection = sqlite3.connect("BaseW.db")
cursor = connection.cursor()

cursor.execute('select * from iai_weapon;')
info = cursor.fetchall()

for weapon in info:
    weapon_name = str(weapon[1])
    weapon_attack = int(weapon[2])
    weapon_durability = int(weapon[3])
    weapon_name_code = str(weapon[4])
    weapon_name_code = Weapon(weapon_name, weapon_attack, weapon_durability)
    create_weapon.extend([weapon_name_code])

start_UPDATE_weapon()

class Player:

    def __init__(self, name, health, attack, weapon, armor, durability):

        self.n = name
        self.h = health
        self.a = attack
        self.w = weapon
        self.ar = armor
        self.d = durability

    def get_name(self):

        return self.n

    def get_health(self):

        return self.h

    def get_attack(self):

        return self.a

    def get_durability(self):

        return self.d

    def damage(self, damage):

        if damage > self.ar:
            damage -= self.ar
            self.h -= damage

    def has_weapon(self):

        if self.w != "None":
            return self.w is not None

        else:
            return None

    def attack_player(self, target_player):

        damage = self.a
        if self.has_weapon() != None:
            damage += self.w.get_damage_amount()
            self.d -= 1
            if self.d <= 0:
                print("L'arme de", self.get_name(), "est détruite car")
                self.w = "None"
                self.d = 0

        target_player.damage(damage)

    def set_weapon(self, weapon):

        self.w = weapon

        if weapon != None:
            self.d = self.w.get_durability()

    def get_armor(self):

        return self.ar

connection = sqlite3.connect("BaseP.db")
cursor = connection.cursor()

cursor.execute('select * from iai_player where player_life = 1;')
info = cursor.fetchall()

for player in info:
    player_ID = int(player[0])
    player_name = str(player[1])
    player_health = int(player[2])
    player_attack = int(player[3])
    player_weapon = str(player[4])
    player_armor = int(player[5])
    player_durability = player[6]
    p = "player"
    id = str(player_ID)
    player_id = (p+id)
    player_id = Player(player_name, player_health, player_attack, player_weapon,player_armor, player_durability)
    inlife_players.extend([player_id])

start_UPDATE_player()
connection.close()

connection = sqlite3.connect("BaseP.db")
cursor = connection.cursor()

cursor.execute('select * from iai_player where player_life = 0;')
info = cursor.fetchall()

for player in info:
    player_ID = int(player[0])
    player_name = str(player[1])
    player_health = int(player[2])
    player_attack = int(player[3])
    player_weapon = str(player[4])
    player_armor = int(player[5])
    player_durability = player[6]
    p = "player"
    id = str(player_ID)
    player_id = (p+id)
    player_id = Player(player_name, player_health, player_attack, player_weapon,player_armor, player_durability)
    dead_player.extend([player_id])

start_UPDATE_DEAD_player()
connection.close()

def info():

    print("\n\n\nINFO : Les personnages attaquent avec leur attaque et l'attaque de leurs armes combinées, \n "
        "les personnages perdent autant de points de vie que vu précédamment, \n"
        "attaque à laquelle on soustrait l'armure de la victime \n\n\n")

print(create_weapon)
print(inlife_players)
print(dead_player)
info()
MENU()
Attack_input()

'''
Le probléme est que le nom "d'appelle" de l'object que donne les varible de type "player_id" ne sont pas bien
 interprété par le créateur d'objet qui leur donne un nom de type : 
 <__main__.Player object at 0x0000021F2C437610>
'''