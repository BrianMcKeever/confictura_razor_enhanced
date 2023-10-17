def get_least_charge_tool(item_id, color = 0):
    tools = Items.FindAllByID(item_id,color, Player.Backpack.Serial, 0)
    best_tool = None
    remaining_min = 99999
    for tool in tools:
        props = Items.GetPropStringList(tool)
        uses_remaining = -1
        for prop in props:
            if "uses remaining" in prop:
                uses_remaining = int(prop.split(" ")[2])
                break
        if uses_remaining < remaining_min:
            remaining_min = uses_remaining
            best_tool = tool
    return best_tool

def get_tinker_tool(make_if_necessary = True):
    while True:
        tinker_tools = Items.FindAllByID(0x1EB8,0, Player.Backpack.Serial, 0)
        tool = None
        remaining_min = 999
        for tinker_tool in tinker_tools:
            props = Items.GetPropStringList(tinker_tool)
            uses_remaining = -1
            for prop in props:
                if "uses remaining" in prop:
                    uses_remaining = int(prop.split(" ")[2])
                    break
            if uses_remaining < remaining_min:
                remaining_min = uses_remaining
                tool = tinker_tool
        if len(tinker_tools) == 1 and make_if_necessary:
            make_tinker_tool()
            continue
        return tool
    
def make_tinker_tool():
    print("make tinker tool")
    tool = get_tinker_tool(False)
    if not tool:
        Misc.Beep()
        print("no tinker tool")
        Misc.ScriptStopAll()
    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 29)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 177)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)


def make_jointing_plane():
    tool = get_tinker_tool()
    boards = Items.FindByID(0x1BD7,-1,Player.Backpack.Serial)
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
        
def make_pen():
    tinker = get_tinker_tool()
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
        
def make_woodworking_tools():
    tool = get_tinker_tool()
    ingots = Items.FindByID(0x1BF2,-1,Player.Backpack.Serial)
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
    tool = get_least_charge_tool(0x1030)
    if not tool:
        make_jointing_plane()
        tool = get_jointing_plane()
    return tool
    
def get_woodworking_tools():
    tool = get_least_charge_tool(0x4F52)
    if not tool:
        make_woodworking_tools()
        tool = get_woodworking_tools()
    return tool
    
def make_tongs():

    tool = get_tinker_tool()
    if tool:
        print("make tongs")
        Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 184)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0)
    else:
        Misc.ScriptStopAll(True)
        
def get_tongs():
    tool = get_least_charge_tool(0x0FBB)
    if not tool:
        make_tongs()
        tool = get_tongs()
    return tool
        
def tinker_hatchet():
    tool = get_tinker_tool()

    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 29)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 58)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 0)
    Misc.Pause(1000)
    
def make_ore_spade ():
    tinkerTools = get_tinker_tool()
    if tinkerTools:
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,29)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,93)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,0)
    else:
        Player.ChatSay("Out of tinker tools")
        halt
    return
    
def get_ore_spade():
    return get_least_charge_tool(0x0F3A, 0x096d)
