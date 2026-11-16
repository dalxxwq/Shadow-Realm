player = {    "name": "Hero",    "class": "None",     "health": 100,    "max_health": 100,    "level": 1,    "experience": 0,    "experience_to_next_level": 100,    "attack": 10,    "defense": 5,   "ability": "None",   "ability_description": "None" }

enemy = {"name": "Shadow Creature", "health": 60, "max_health": 60, "attack": 8, "defense": 2, "experience_reward": 50}

def main():
    print(f"================================\n         SHADOW REALM     \n================================\n")
    name = input("Enter your name: ")
    player["name"] = name
    clas = input("Choose your class (Warrior, Mage, Rogue): ")

    while clas.lower() not in ["warrior", "mage", "rogue"]:
        print("Invalid class choice. Please choose from Warrior, Mage, or Rogue.")
        clas = input("Choose your class (Warrior, Mage, Rogue): ")
    else:
        player["class"] = clas.capitalize()

    if player["class"] == "Warrior":
        player["attack"] = 15
        player["defense"] = 10
        player["max_health"] = 120
        player["health"] = 120
        player["ability"] = "Shield Wall"
        player["ability_description"] = "A sturdy wall of defense that reduces incoming damage."
    elif player["class"] == "Mage":
        player["attack"] = 22
        player["defense"] = 3
        player["max_health"] = 80
        player["health"] = 80
        player["ability"] = "Fireball"
        player["ability_description"] = "A powerful fire-based spell that deals significant damage to a single target."
    elif player["class"] == "Rogue":
        player["attack"] = 18
        player["defense"] = 4
        player["max_health"] = 90
        player["health"] = 90
        player["ability"] = "Shadow Strike"
        player["ability_description"] = "A swift strike from the shadows that deals critical damage."

    print(f"\nWelcome, {player['name']}! Your journey begins now.\n")

    print(f"Your current stats:\nName: {player['name']}\nClass: {player['class']}\nHealth: {player['health']}/{player['max_health']}\nLevel: {player['level']}\nExperience: {player['experience']}\nExperience to Next Level: {player['experience_to_next_level']}\nAttack: {player['attack']}\nDefense: {player['defense']}\nAbility: {player['ability']}\nAbility Description: {player['ability_description']}\n")
    gain_experience(250)  # Example of gaining experience points
    show_enemy()  # Display enemy stats

def gain_experience(amount):
    player["experience"] += amount
    print(f"\nYou gained {amount} experience points!\n")
    level_up()

def level_up():
    while player["experience"] >= player["experience_to_next_level"]:
        player["level"] += 1
        player["experience"] -= player["experience_to_next_level"]
        player["experience_to_next_level"] = int(player["experience_to_next_level"] * 1.5)
        player["max_health"] += 10
        player["health"] = player["max_health"]
        player["attack"] += 2
        print(f"\nCongratulations! You've leveled up to Level {player['level']}!\n")

def show_enemy():
    print(f"Enemy: {enemy['name']}\nHealth: {enemy['health']}/{enemy['max_health']}\nAttack: {enemy['attack']}\nDefense: {enemy['defense']}\nExperience Reward: {enemy['experience_reward']}\n")

def battle():
    print("================================\n         BATTLE STARTS     \n================================\n")
    print(f"\nA wild {enemy['name']} appears!\n")
    while enemy["health"] > 0 and player["health"] > 0:
        action = input("Choose your action (attack, show stats, run away): ").lower()
        if action == "attack":
            player_attack()
        elif action == "show stats":
            print(f"\nYour stats:\nHealth: {player['health']}/{player['max_health']}\nAttack: {player['attack']}\nDefense: {player['defense']}\n")
        elif action == "run away":
            print("\nYou fled from the battle!\n")
            break
        else:
            print("\nInvalid action. Please choose again.\n")

def player_attack():
    damage = player["attack"] - enemy["defense"]
    damage = max(damage, 1)
    enemy["health"] -= damage
    enemy["health"] = max(enemy["health"], 0)
    print(f"\nYou attacked {enemy['name']} for {damage} damage!\nEnemy health is now {enemy['health']}/{enemy['max_health']}.\n")
    if enemy["health"] <= 0:
        print(f"{enemy['name']} has been defeated!\n")
        gain_experience(enemy["experience_reward"])
    else:
        enemy_attack()

def enemy_attack():
    damage = enemy["attack"] - player["defense"]
    damage = max(damage, 1)
    player["health"] -= damage
    player["health"] = max(player["health"], 0)
    print(f"{enemy['name']} attacked you for {damage} damage! Your health is now {player['health']}/{player['max_health']}.\n")
    if player["health"] <= 0:
        print("You have been defeated! Game Over.\n")

if __name__ == "__main__":
    main()