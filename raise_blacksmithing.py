def makeTongs():

    tool = Items.FindByID(0x1EB8,-1,Player.Backpack.Serial) #tinkering kit
    if tool:
        print("make tongs")
        Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 184)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0)
    else:
        Misc.ScriptStopAll(True)
    

while True:
    if Player.GetSkillValue("Arms Lore") >= 100:
    #if Player.GetSkillValue("Blacksmithing") >= 100.3:
        halt
    Misc.Pause(1000)
    tool = Items.FindByID(0x0FBB,-1,Player.Backpack.Serial) #tongs
    if not tool:
        makeTongs()
        continue
    Items.UseItem(tool)

    smeltList = [0x2677,0x0F52,0x27A4, 0x0F62,0x2CFF, 0x2680, 0x13FF, 0x143B, 0x268C, 0x0F5D, 0x0F5C, 0x2681, 0x268E, 0x1441]
    for smeltable in smeltList:
        item = Items.FindByID(smeltable,-1,Player.Backpack.Serial)
        if item:
            print("smelt")
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 14) #smelt
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(item)
    else:
        print("Make last")
        Gumps.WaitForGump(949095101, 5000)
        Gumps.SendAction(949095101, 21) #make last
        Gumps.WaitForGump(949095101, 5000)
        Gumps.CloseGump(949095101)

       
