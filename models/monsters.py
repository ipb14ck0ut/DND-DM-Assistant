import json
from pydantic import BaseModel
from typing import List

class Attack(BaseModel):
    weapon: str
    damage: str
    type: str

class Monster(BaseModel):
    id: str
    name: str
    hit_dice: str
    hp: int
    attacks: List[Attack]
    saving_throw: int
    movement: int
    alignment: str
    challenge_rating: int
    xp_value: int

def load_monsters(filepath: str) -> dict[str, Monster]:
    """קורא את קובץ ה-JSON ומחזיר מילון של אובייקטי מפלצות"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return {m["id"]: Monster(**m) for m in data["monsters"]}