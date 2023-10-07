while True:
    bark = Items.FindByID(0x318F,-1, Player.Backpack.Serial)
    if bark:
        Items.Move(bark, 0x403E49A0, 400)
        Misc.Pause(1000)
        
    logs = Items.FindByID(0x1BE0,0,Player.Backpack.Serial,1)
    if not logs:
        logs = Items.FindByID(0x1BE0,0,0x403CAD9A,1)
        if not logs:
            Misc.Beep()
            halt
        Items.Move(logs, Player.Backpack.Serial, 200)
        Misc.Pause(1000)
    plane = Items.FindByID(0x1030,-1, Player.Backpack.Serial)
    if not plane:
        Misc.Beep()
        halt
    Items.UseItem(plane)
    Gumps.WaitForGump(949095101, 5000)
    Gumps.SendAction(949095101, 16)
    Gumps.WaitForGump(949095101, 5000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)
    
