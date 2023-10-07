water_type = 0x1847
food_types = [0x09F2, 0x09EA, 0x09D1, 0x09C9, 0x097D, 0x09D0, 0x097B, 0x09B7, 0x09C0]

def cast_food_and_eat():
    Spells.CastMagery("Create Food")
    Misc.Pause(1000)
    water = Items.FindByID(water_type,0,Player.Backpack.Serial)
    if water:
        Items.UseItem(water)
        Misc.Pause(1000)
    water = Items.FindByID(water_type,0,Player.Backpack.Serial)
    Items.DropItemGroundSelf(water,1)
    Misc.Pause(1000)
    for food_type in food_types:
        print(food_type)
        food = Items.FindByID(food_type,0,Player.Backpack.Serial)
        if food:
            Items.UseItem(food)
            Misc.Pause(1000)
            break

def am_i_hungry():
    try:
        Player.ChatSay("[hunger")
        Gumps.WaitForGump(1712486629,4000)
        data = Gumps.LastGumpGetLineList()
        hunger = int(data[0].split(' ')[1])
        thirst = int(data[1].split(' ')[1])
        if hunger < 20 or thirst < 20:
            return True
    except whatever:
        return True
    return False

def fuel():
    while am_i_hungry():
        cast_food_and_eat()
        
fuel()
