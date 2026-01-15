import random
from typing import override

# Soldier
class Soldier:
    def __init__(self, health: int | float, strength: int | float) -> None:
        self.health = health
        self.strength = strength
    
    def attack(self) -> int | float:
        return self.strength

    def receiveDamage(self, damage: int | float) -> str | None:
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name: str, health: int | float, strength: int | float) -> None:
        super().__init__(health=health, strength=strength)

        self.name = name

    def battleCry(self) -> str:
        return "Odin Owns You All!"

    @override
    def receiveDamage(self, damage) -> str:

        self.health -= damage

        if self.health > 0 :
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    def __init__(self, health: int | float, strength: int | float) -> None:
        super().__init__(health=health, strength=strength)

    @override
    def receiveDamage(self, damage: int | float) -> str:

        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
# Davicente

class War():
    def __init__(self) -> None:
        self.vikingArmy:list[Viking] = []
        self.saxonArmy:list[Saxon]= []


    def addViking(self, viking: Viking) -> None:
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon) -> None:
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self) -> str:

        # Get soldiers involved in the attack
        random_saxon, random_viking = self.get_random_soldiers()

        viking_damage = random_viking.attack()
        message = random_saxon.receiveDamage(viking_damage)
        
        # remove dead saxons from army
        if "died"in message:
            self.saxonArmy.remove(random_saxon)

        return message

    def saxonAttack(self) -> str:

        # Get soldiers involved in the attack
        random_saxon, random_viking = self.get_random_soldiers()

        saxon_damage = random_saxon.attack()
        message = random_viking.receiveDamage(saxon_damage)
        
        # remove dead saxons from army
        if "died"in message:
            self.vikingArmy.remove(random_viking)

        return message

    def showStatus(self):

        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >=1:
            return "Vikings and Saxons are still in the thick of battle."

        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        
    def get_random_soldiers(self) -> tuple[Saxon, Viking]:

        try:
            random_saxon = random.choice(self.saxonArmy)
        except IndexError:
            raise Exception("There is no one on the saxon army!")
    
        try:
            random_viking = random.choice(self.vikingArmy)
        except IndexError:

            raise Exception("There is no one on the viking army!")
        
        return (random_saxon, random_viking)
