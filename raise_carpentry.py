from util import *

resource_container = 0x403CAD9A
jointing_plane_id = 0x1030
boards_id = 0x1BD7
ingots_id = 0x1BF2
trash_can = 0x40173954 #merchant crate
trash_can = 0x403F569B
    
#20.7 - 45.7 = +25
#74.6
while True:
    Misc.Pause(1000)
    boards = Items.FindByID(0x1BD7,0,Player.Backpack.Serial)
    if not boards or boards.Amount < 150:
        boards = Items.FindByID(0x1BD7,0,resource_container)
        if not boards:
            print("out of boards")
            Misc.Beep()
            halt
        Items.Move(boards,Player.Backpack.Serial,1000)
        Misc.Pause(1000)
        
    ingots = Items.FindByID(0x1BF2, 0, Player.Backpack.Serial)
    if not ingots or ingots.Amount < 50:
        ingots = Items.FindByID(0x1BF2, 0, resource_container)
        Items.Move(ingots, Player.Backpack, 1000)
        Misc.Pause(1000)

    trash_list = [0x09AA, 0x1DB8, 0x14F0,0x0E3F,0x27A8,0x13F8,0x0E89, 0x0F65, 0x27A6,0x2811,0x14F0]
    for trash_type in trash_list:
        trash = Items.FindByID(trash_type,-1,Player.Backpack.Serial)
        if trash:
            Items.Move(trash,trash_can,1)
            Misc.Pause(1000)
            break
    else:
        if Player.GetSkillValue("Carpentry") < 11 + 25:
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 1)
            Gumps.WaitForGump(949095101, 1000) #barrel lids
            Gumps.SendAction(949095101, 30)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 15.7 + 25:
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 43) #dart board south
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 37)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 21 + 25:
            tool = get_woodworking_tools()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 2)        #wooden box
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 47.3:
            tool = get_woodworking_tools()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 22)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 9)       #medium crate
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 47.3 + 25:
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 43)        #ballot box
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 51)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 70 + 25:
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 29)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 2)     #bokuto
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 73.6 + 25:
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 22)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 23)     #quarter staff
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 78.9 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 22)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 30)     #gnarled staff
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 80 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 29)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 16)     #tetsubo
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 86.8 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 1)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 51)     #easel south
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 90 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_woodworking_tools()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 37)     #wooden footlocker
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 94.7 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 71)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 37)     #water trough
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        if Player.GetSkillValue("Carpentry") < 100 + 25 and Player.GetRealSkillValue("Carpentry") < Player.GetSkillCap("Carpentry"):
            tool = get_jointing_plane()
            Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 43)
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 58)     #pentagram
            Gumps.WaitForGump(949095101, 1000)
            Gumps.SendAction(949095101, 0)
            continue
        Misc.Beep()
        halt

