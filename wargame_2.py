import random 
from vikingsClasses import Viking, Saxon, War
from rich.progress import Progress

class NewWar(War):
    def __init__(self) -> None:
        super().__init__()

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


        return message + f" by the hand of {random_viking.name}. He said: " + random_viking.battleCry()


def viking_name_generator():
    first_names = ["Bjorn", "Astrid", "Einar", "Ingmar", "Xander", "Sven", "Olaf", "Arn", "Frida", "Helga", "Hervor"]
    last_names = ["Anderson", "Hansen", "Snake-in-the-Eye", "Erikson", "Falk", "Berg", "Odinson", "Varangr"]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return name

    
huge_war = NewWar()

# generate viking army
viking_army_size = random.randint(0, 100)
saxon_army_size = random.randint(0, 100)

top_health = 200
top_strength = 200

for i_soldier in range(viking_army_size):
    name = viking_name_generator()
    viking_soldier = Viking(name,
                            random.randint(0,top_health),
                            random.randint(0, top_strength))
    
    huge_war.addViking(viking_soldier)

# generate saxon army
for i_soldier in range(saxon_army_size):
    saxon_soldier = Saxon(random.randint(0,top_health),
                          random.randint(0, top_strength))
    
    huge_war.addSaxon(saxon_soldier)



total_attacks = 0
armies = ["vikings", "saxons"]
prob_peace = 0.02
peace = False

with Progress() as progress:
    n_alive_vikings = progress.add_task("[red]Viking Army Soldiers", total=viking_army_size)
    n_alive_saxons = progress.add_task("[green]Saxon Army Soldiers", total=saxon_army_size)

    while huge_war.showStatus() == "Vikings and Saxons are still in the thick of battle." and not peace:
        attacking_army = random.choice(armies)

        try: 
            if attacking_army == "vikings":
                message = huge_war.vikingAttack()
                progress.console.print("[red]" + message)

            else:
                message = huge_war.saxonAttack()
                progress.console.print("[green]" + message)
        except: 
            pass

        progress.update(n_alive_vikings, completed=len(huge_war.vikingArmy))
        progress.update(n_alive_saxons, completed=len(huge_war.saxonArmy))
        # print(f"Attacks: {total_attacks} // Viking army: {len(huge_war.vikingArmy)} warriors",f"and Saxon army: {len(huge_war.saxonArmy)} warriors")
        # print(huge_war.showStatus())
        # total_attacks +=1
        
        # peace?
        random_peace = random.random()
        if random_peace <= prob_peace:

            if abs(len(huge_war.vikingArmy)-len(huge_war.saxonArmy)) <= 10:
                peace = True
                progress.console.print("[bold white]We reached peace!!!!!")
                break

        
        progress.console.print("[yellow]" + huge_war.showStatus())

