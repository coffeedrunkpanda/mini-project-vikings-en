import random
from typing import override

# Soldier
class Soldier:  
    """A Soldier capable of attacking and receiving damage. 

    Attributes:
        health (int | float): Soldiers health value.
        strength (int | float): Soldiers strength value.
    """    
    
    def __init__(self, health: int | float, strength: int | float) -> None:
        """Initialize the soldier with specific health and strength.

        Args:
            health (int | float): Soldiers health value.
            strength (int | float): Soldiers strength value.
        """
        self.health = health
        self.strength = strength
    
    def attack(self) -> int | float:
        """Attack strength.

        Returns:
            int | float: The strength of the attack/damage.
        """        
        return self.strength

    def receiveDamage(self, damage: int | float) -> str | None:
        """Apply damage to the soldier.

        Args:
            damage (int | float): Damage received.
        """        
        self.health -= damage


# Viking
class Viking(Soldier):
    """A viking soldier.

    The soldier is capable of attacking, receiving damage, and yelling a battle cry phrase. 

    Attributes:
        name (str): Viking soldier's name.
        health (int | float): Soldiers health value.
        strength (int | float): Soldiers strength value.
    """    
    def __init__(self, name: str, health: int | float, strength: int | float) -> None:
        """Initialize the viking soldier.

        Args:
            name (str): Viking soldier's name.
            health (int | float): Soldiers health value.
            strength (int | float): Soldiers strength value.
        """        
        super().__init__(health=health, strength=strength)

        self.name = name

    def battleCry(self) -> str:
        """Return the soldier's battle cry phrase. """        
        return "Odin Owns You All!"

    @override
    def receiveDamage(self, damage:int | float) -> str:
        """Apply damage to the soldier and return their current status.

        Args:
            damage (int | float): Amount of damage to apply to the soldier.

        Returns:
            str: Status message describing the soldier's condition after receiving the damage.
        """         
        self.health -= damage

        if self.health > 0 :
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    """A saxon soldier.

    The soldier is capable of attacking, and receiving damage.

    Attributes:
        health (int | float): Soldiers health value.
        strength (int | float): Soldiers strength value.
    """   
    def __init__(self, health: int | float, strength: int | float) -> None:
        """Initialize the saxon soldier with specific health and strength.

        Args:
            health (int | float): Soldiers health value.
            strength (int | float): Soldiers strength value.
        """   
        super().__init__(health=health, strength=strength)

    @override
    def receiveDamage(self, damage: int | float) -> str:
        """Apply damage to the soldier and return their current status.

        Args:
            damage (int | float): Amount of damage to apply to the soldier.

        Returns:
            str: Status message describing the soldier's condition after receiving the damage.
        """   
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
# Davicente

class War():
    """A simulation of the conflict between Vikings and Saxons.
    
    Attributes:
        vikingArmy (list[Viking]): List of soldiers in the Viking army.
        saxonArmy (list[Saxon]): List of soldiers in the Saxon army.
    """    
             
    def __init__(self) -> None:
        """Initialize empty army lists"""        
        self.vikingArmy:list[Viking] = []
        self.saxonArmy:list[Saxon]= []

    def addViking(self, viking: Viking) -> None:
        """Add Viking soldier to the army list.

        Args:
            viking (Viking): Viking soldier to be added to the army.
        """        
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon) -> None:
        """Add Saxon soldier to the army list.

        Args:
            saxon (Saxon): Saxon soldier to be added to the army.
        """    
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self) -> str:
        """Execute an attack by a random Viking against a random Saxon.

        A random Viking is selected to attack a random Saxon. If the Saxon
        dies from the damage, the soldier is removed from the army.

        Returns:
            str: A status message from the Saxon after receiving damage.
        """
        # Get soldiers involved in the attack
        random_saxon, random_viking = self._get_random_soldiers()

        viking_damage = random_viking.attack()
        message = random_saxon.receiveDamage(viking_damage)
        
        # remove dead saxons from army
        if "died" in message:
            self.saxonArmy.remove(random_saxon)

        return message

    def saxonAttack(self) -> str:
        """Execute an attack by a random Saxon against a random Viking.

        A random Saxon is selected to attack a random Viking. If the Viking
        dies from the damage, the soldier is removed from the army.

        Returns:
            str: A status message from the Viking after receiving damage.
        """
        # Get soldiers involved in the attack
        random_saxon, random_viking = self._get_random_soldiers()

        saxon_damage = random_saxon.attack()
        message = random_viking.receiveDamage(saxon_damage)
        
        # remove dead saxons from army
        if "died" in message:
            self.vikingArmy.remove(random_viking)

        return message

    def showStatus(self) -> str:
        """Return a status message about the current war."""

        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >=1:
            return "Vikings and Saxons are still in the thick of battle."

        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "No Status!"
             
    def _get_random_soldiers(self) -> tuple[Saxon, Viking]:
        """Choose a Viking and a Saxon soldier randomly.

        Raises:
            ValueError: If the Saxon army is empty.
            ValueError: If the Viking army is empty.

        Returns:
            tuple[Saxon, Viking]: A random saxon and a random viking soldier.
        """
        try:
            random_saxon = random.choice(self.saxonArmy)
        except IndexError as e:
            raise ValueError("There is no one on the saxon army!") from e
    
        try:
            random_viking = random.choice(self.vikingArmy)
        except IndexError as e:

            raise ValueError("There is no one on the viking army!") from e
        
        return (random_saxon, random_viking)
