import random
from random import randint


#Constants
gameStarted = False
#Robot
bot_hp = 750
bot_energy = 500
#Attacks
crane_damage = 200
touch_damage = 100
sound_damage = 50
crane_consume = 300
touch_consume = 150
sound_consume = 50
#Cures
cure1_recovered_hp = 100
cure2_recovered_hp = 200
cure3_recovered_hp = 400
cure1_consume = 200
cure2_consume = 300
cure3_consume = 400
#Enemies
tank_force = 200
artillery_force = 500
infantry_force = 100
tank_nr_attacks = 2
artillery_nr_attacks = 1
infantry_nr_attacks = 3
tank_hp = 200
artillery_hp = 50
infantry_hp = 100

defender_moves = 6
attackers_moves = 7

enemy_slots = []

total_moves_left = defender_moves + attackers_moves

def ChooseYourDestiny() : 
    generated_order = random.sample(range(0, 6), 6)
    print(generated_order)
    
    for x in range(0, 6) :
        dice1 = randint(1, 6)
        if (dice1 == 1) or (dice1 == 2)  :
            aux_enemy = "Tank"
        elif (dice1 == 3) or (dice1 == 4) :
            aux_enemy = "Art"
        elif (dice1 == 5) or (dice1 == 6) :
            aux_enemy = "Inf"

        dice2 = generated_order[x]
        enemy_slots.insert(dice2, aux_enemy)
        print("Inserted " + str(aux_enemy) + " in slot " + str(dice2+1))
        
        x += 1
    print("EnemySlots :----  " + str(enemy_slots))

class Defender() :
    hp = 750
    energy = 500

    def info(self) :
        print("______________________")
        print("_____DEFENDER-BOT_____\n")
        print("HP : " + str(self.hp))
        print("ENERGY : " + str(self.energy))
        print("\n\n")
        print("______________________")


    class Attack() :
        damage = 0
        consumption = 0

        def __init__(self, damage, consumption) :
            self.damage = damage
            self.consumption = consumption

        def do(self, enemy) :
            print("Damaged the Enemy with")
            enemy.hp -= self.damage

        def info(self) :
            print("______________________")
            print("_____ATTACK_____\n")
            print("DAMAGE : " + str(self.damage))
            print("CONSUMPTION : " + str(self.consumption))
            print("\n\n")
        print("______________________")

            
    class Cure() :
        recovered_life = 0
        consumption = 0

        def __init__(self, recovered_life, consumption) :
            self.recovered_life = recovered_life
            self.consumption = consumption
    
    

class Enemy() :
    hp = 0
    strenght = 0
    nr_of_attacks = 0
    impact_attack = 0
    def __init__(self, hp, strenght, nr_of_attacks) :
        self.strenght = strenght
        self.nr_of_attacks = nr_of_attacks
        self.hp = hp
        self.impact_attack = hp/strenght
    
    def info(self) :
        print("______________________")
        print("_____ENEMY_____\n")
        print("HP : " + str(self.hp))
        print("STRENGHT : " + str(self.strenght))
        print("NR_OF_ATTACKS : " + str(self.nr_of_attacks))
        print("IMPACT ATTACK : " + "I/A Formula needed")
        print("\n\n")
        print("______________________")
        

def main():

    #Defining all attacks, cures and enemies
    gameStarted = True
    if gameStarted == True :

        Defender_Bot = Defender()

        Crane_Attack = Defender_Bot.Attack(crane_damage, crane_consume)
        Touch_Attack = Defender_Bot.Attack(touch_damage, touch_consume)
        Sound_Attack = Defender_Bot.Attack(sound_damage, sound_consume)

        Cure_1 = Defender_Bot.Cure(cure1_recovered_hp, cure1_consume)
        Heal_2 = Defender_Bot.Cure(cure2_recovered_hp, cure2_consume)
        Heal_3 = Defender_Bot.Cure(cure3_recovered_hp, cure3_consume)

        Tank = Enemy( tank_hp, tank_force, tank_nr_attacks)
        Art = Enemy(artillery_hp, artillery_force, artillery_nr_attacks)
        Inf = Enemy(infantry_hp, infantry_force, infantry_nr_attacks)
        #________________________________________________________________

        ChooseYourDestiny()
        # RandEnemies()

if __name__ == '__main__':
   main()
