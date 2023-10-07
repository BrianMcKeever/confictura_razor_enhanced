def make_pen():
    tinker = Items.FindByID(0x1EB8, 0, Player.Backpack.Serial)
    if not tinker:
        Misc.Beep()
        halt
    Items.UseItem(tinker)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 29)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 128)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)
        
while True:
    if Player.GetSkillValue("Inscription") < 70:
        amount = 1
    else:
        amount = 200
    tinker = Items.FindByID(0x1EB8, 0, Player.Backpack.Serial)
    scroll = Items.FindByID(0x0EF3,0,Player.Backpack.Serial)
    if scroll:
        Items.Move(scroll, 0x40467955, -1)
        Misc.Pause(1000)
    
    bark = Items.FindByID(0x318F,0, Player.Backpack.Serial,1)
    if not bark:
        
        bark = Items.FindByID(0x318F,0,0x403CAD9A,1)
        if not bark:
            Misc.Beep()
            halt
        
        Items.Move(bark, Player.Backpack.Serial, amount)
        Misc.Pause(1000)
    pen = Items.FindByID(0x2051,-1, Player.Backpack.Serial,1)
    if not pen:
        make_pen()
        continue
        
    Items.UseItem(pen)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 43)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 2)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)
