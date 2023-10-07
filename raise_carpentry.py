resource_container = 0x403CAD9A
jointing_plane_id = 0x1030
boards_id = 0x1BD7
ingots_id = 0x1BF2
trash_can = 0x40173954 #merchant crate
trash_can = 0x400AA292


def make_jointing_plane():
    tool = Items.FindByID(0x1EB8,-1,Player.Backpack.Serial) #tinkering kit
    boards = Items.FindByID(boards_id,-1,Player.Backpack.Serial)
    if tool and boards and boards.Amount > 6 :
        print("make tool")
        Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 50)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 2)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 0)     
    else:
        Misc.Beep()
        Misc.ScriptStopAll(True)
        
def make_woodworking_tools():
    tool = Items.FindByID(0x1EB8,-1,Player.Backpack.Serial) #tinkering kit
    ingots = Items.FindByID(ingots_id,-1,Player.Backpack.Serial)
    if tool and ingots and ingots.Amount > 6 :
        print("make woodworking tools")
        Items.UseItem(tool)
       
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 212)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 0)
    else:
        Misc.Beep()
        Misc.ScriptStopAll(True)

def get_jointing_plane():
    tool = Items.FindByID(jointing_plane_id,-1,Player.Backpack.Serial)
    if not tool:
        make_jointing_plane()
        tool = get_jointing_plane()
    return tool
    
def get_woodworking_tools():
    tool = Items.FindByID(0x4F52,-1,Player.Backpack.Serial)
    if not tool:
        make_woodworking_tools()
        tool = get_woodworking_tools()
    return tool
    
#20.7 - 45.7 = +25
#74.6
while True:
    Misc.Pause(1000)
    boards = Items.FindByID(0x1BD7,0,Player.Backpack.Serial)
    if not boards or boards.Amount < 30:
        boards = Items.FindByID(0x1BD7,0,resource_container)
        if not boards:
            print("out of boards")
            Misc.Beep()
            halt
        Items.Move(boards,Player.Backpack.Serial,1000)
        Misc.Pause(1000)

    trash_list = [0x09AA, 0x1DB8, 0x14F0,0x0E3F,0x27A8,0x13F8,0x0E89]
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
        Misc.Beep()
        halt



