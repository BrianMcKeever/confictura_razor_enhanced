pole_chest_id = 0x40399290
resource_chest_id = 0x403CAD9A


def make_fishing_pole():
    plane = Items.FindByID(0x1030,0,Player.Backpack.Serial)
    if not plane:
        return False
    Items.UseItem(plane)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 1)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 86)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)
    return True
    
    
while True:
    pole_chest = Items.FindBySerial(pole_chest_id)
    print(len(pole_chest.Contains))
    if len(pole_chest.Contains) == 125:
        Misc.Beep()
        break
    
    pole = Items.FindByID(0x0DC0,0,Player.Backpack.Serial)
    if pole:
        Items.Move(pole,pole_chest_id,1)
        Misc.Pause(1000)
        continue
        
    make_fishing_pole()
        