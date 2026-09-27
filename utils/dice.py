import random
import re

def roll_dice(dice_string: str) -> int:
    """
    מקבל מחרוזת קוביות (למשל '1d8', '2d6+2' או '1+1') ומחזיר תוצאה.
    אם חסר 'd', מניח שמדובר בק"פ (Hit Dice) של מפלצת ומגלגל קוביות d8.
    """
    dice_string = str(dice_string).lower().strip()
    
    # טיפול ספציפי ב-Hit Dice ממשחקי OSR (חרבות וכשפים)
    if 'd' not in dice_string:
        if '+' in dice_string:
            parts = dice_string.split('+')
            dice_string = f"{parts[0].strip()}d8+{parts[1].strip()}"
        elif '-' in dice_string:
            parts = dice_string.split('-')
            dice_string = f"{parts[0].strip()}d8-{parts[1].strip()}"
        else:
            # מקרה של ספרה בודדת כמו "1" או "3"
            dice_string = f"{dice_string.strip()}d8"
            
    # כעת המחרוזת תמיד תהיה בפורמט תקין כמו "1d8" או "1d8+1"
    pattern = r'^(\d+)\s*d\s*(\d+)(?:\s*([+-])\s*(\d+))?$'
    match = re.match(pattern, dice_string)
    
    if not match:
        raise ValueError(f"Invalid dice format: '{dice_string}'")
    
    num_dice = int(match.group(1))
    dice_sides = int(match.group(2))
    
    # גלגול הקוביות
    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]
    total = sum(rolls)
    
    # הוספת או החסרת התוסף
    if match.group(3) and match.group(4):
        modifier = int(match.group(4))
        if match.group(3) == '+':
            total += modifier
        elif match.group(3) == '-':
            total -= modifier
            
    # מינימום נקודות פגיעה או נזק הוא תמיד 1
    return max(1, total)