from util import *
source_container = 0x403CAD9A
trash_barrel = 0x403F569B

trash_items = [
    0x105B, #axle
    0x103E, #flour sifter
    ]

Items.UseItem(source_container)
Misc.Pause(1000)
while Player.GetRealSkillValue("Tinkering") < Player.GetSkillCap("Tinkering"):
    ingots = Items.FindByID(0x1BF2, 0, Player.Backpack.Serial)
    if not ingots or ingots.Amount < 10:
        ingots = Items.FindByID(0x1BF2, 0, source_container)
        Items.Move(ingots, Player.Backpack, 100)
        Misc.Pause(1000)
    boards = Items.FindByID(0x1BD7, 0, Player.Backpack.Serial)
    if Player.GetSkillValue("Tinkering") < 0 + 50 and (not boards or boards.Amount < 10):
        boards = Items.FindByID(0x1BD7, 0, source_container)
        Items.Move(boards, Player.Backpack, 100)
        Misc.Pause(1000)
        
    for item in trash_items:
        trash = Items.FindByID(item, 0, Player.Backpack.Serial)
        if trash:
            Items.Move(trash, trash_barrel, 1)
            Misc.Pause(1000)
            
    tool = get_tinker_tool()
    Items.UseItem(tool)
    #Misc.Pause(1000)
    if Player.GetSkillValue("Tinkering") < 0 + 50: #NOT SURE ABOUT 50
        Gumps.WaitForGump(949095101, 2000)
        Gumps.SendAction(949095101, 50)
        Gumps.WaitForGump(949095101, 2000)
        Gumps.SendAction(949095101, 30) #axle
        Gumps.WaitForGump(949095101, 2000)
        #Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Tinkering") < 10 + 50 and len(Player.Backpack.Contains) <= 100:
        Gumps.WaitForGump(949095101, 2000) 
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 2000)
        Gumps.SendAction(949095101, 177) #tinker tools
        Gumps.WaitForGump(949095101, 2000)
        #Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Tinkering") < 45 + 50:
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
        continue
    if Player.GetSkillValue("Tinkering") < 50 + 50:
        Gumps.WaitForGump(949095101, 2000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 2000)
        Gumps.SendAction(949095101, 23) #flour sifter
        Gumps.WaitForGump(949095101, 2000)
        #Gumps.SendAction(949095101, 0)
        continue
    Misc.Beep()
    halt


