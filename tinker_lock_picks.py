from util import *
source_container = 0x403CAD9A

Items.UseItem(source_container)
Misc.Pause(1000)


while True:
    ingots = Items.FindByID(0x1BF2, 0, Player.Backpack.Serial)
    if not ingots or ingots.Amount < 10:
        ingots = Items.FindByID(0x1BF2, 0, source_container)
        Items.Move(ingots, Player.Backpack, 100)
        Misc.Pause(1000)
            
    tool = get_tinker_tool()
    Items.UseItem(tool)

    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 29)
    Gumps.WaitForGump(949095101, 2000) 
    Gumps.SendAction(949095101, 72) #lockpick
    Gumps.WaitForGump(949095101, 2000)
    #Gumps.SendAction(949095101, 0)
    if Player.Weight > Player.MaxWeight or Player.Weight > 400:
        lockpicks = Items.FindByID(0x14FC, 0, Player.Backpack.Serial)
        if lockpicks:
            Items.Move(lockpicks, source_container, -1)
            Misc.Pause(1000)
