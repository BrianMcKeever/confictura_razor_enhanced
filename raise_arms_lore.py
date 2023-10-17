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
resource_container = 0x403CAD9A   
tong_box = 0x4042D937 

Items.UseItem(resource_container)
Misc.Pause(1000)
Items.UseItem(tong_box)

while True:
    #49.6 smithing for 100% dagger crafting
    if Player.GetSkillValue("Arms Lore") >= Player.GetSkillCap("Arms Lore"):
        halt
    Misc.Pause(1000)
    ingots = Items.FindByID(0x1BF2, 0, Player.Backpack.Serial)
    if not ingots or ingots.Amount < 50:
        ingots = Items.FindByID(0x1BF2, 0, resource_container)
        Items.Move(ingots, Player.Backpack, 1000)
        Misc.Pause(1000)
    tool = Items.FindByID(0x0FBB,-1,Player.Backpack.Serial) #tongs
    if not tool:
        if Player.GetSkillValue("Tinkering") > 30:
            makeTongs()
        else:
            tongs = Items.FindByID(0x0FBB, -1, tong_box)
            Items.Move(tongs, Player.Backpack.Serial, 1)
        continue
    Items.UseItem(tool)

    smeltList = [0x2677,0x0F52,0x27A4, 0x0F62,0x2CFF, 0x2680, 0x13FF, 0x143B, 0x268C, 0x0F5D, 0x0F5C, 0x2681, 0x268E, 0x1441]
    for smeltable in smeltList:
        item = Items.FindByID(smeltable,-1,Player.Backpack.Serial)
        if item:
            print("smelt")
            Player.UseSkill("Arms Lore")
            Target.WaitForTarget(3000)
            Target.TargetExecute(item)
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

       
