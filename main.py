import os
from models.monsters import load_monsters
from game_loop import spawn_monster
from utils.dice import roll_dice

def main():
    # הגדרת נתיב אמין לקובץ ה-JSON
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'json', 'monsters.json')
    
    try:
        # טעינת מסד הנתונים של המפלצות
        monsters_db = load_monsters(json_path)
        print("Monsters loaded successfully!")
        
        # שליפת האורק והדפסת נתונים לבדיקה
        current_enemy = monsters_db.get("orc_base")
        if current_enemy:
            print(f"Enemy encountered: {current_enemy.name}")
            print(f"HP: {current_enemy.hp}")
            print(f"Attack with: {current_enemy.attacks[0].weapon} for {current_enemy.attacks[0].damage} damage")
            
        room_1_enemies = [
            spawn_monster("orc_base", monsters_db),
            spawn_monster("orc_base", monsters_db)
        ]
        # שליפת האורק הראשון מהחדר
        orc = room_1_enemies[0]

        # בחירת ההתקפה הראשונה שלו מתוך המערך (חנית)
        spear_attack = orc.attacks[0] 

        # גלגול הנזק בפועל מתוך המחרוזת "1d6"
        damage_dealt = roll_dice(spear_attack.damage)

        print(f"The {orc.name} attacks with {spear_attack.weapon}!")
        print(f"It deals {damage_dealt} damage to the player.")
    except FileNotFoundError:
        print(f"Error: Could not find the JSON file at {json_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()