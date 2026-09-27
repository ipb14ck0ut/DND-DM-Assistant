import copy
from utils.dice import roll_dice # הפונקציה שכתבתם קודם
from models.monsters import Monster

def spawn_monster(monster_id: str, monsters_db: dict) -> Monster:
    """יוצר עותק של מפלצת מהמאגר עם נקודות החיים הקבועות שהוגדרו ב-JSON"""
    base_monster = monsters_db.get(monster_id)
    if not base_monster:
        raise ValueError(f"Monster ID '{monster_id}' not found in database.")
    
    # העתקה עמוקה מאפשרת לנו להוריד למפלצת הזו HP בקרב בלי לשנות את ה-14 המקורי ב-JSON
    spawned_monster = base_monster.model_copy(deep=True)
    
    return spawned_monster