

treeTypes = [3323, 3320, 3326, 3329, 3296, 3492, 3484, 3476, 3496, 3488, 3275, 3300, 3282, 3284, 3290, 3289, 3279, 3278, 3303]
buggedTreeTypes = [3230]

storage = 0x405B018E
normal_wood_only = False

axe_id = 0x0F43
    

from rail_lib import Rail
file = "Scripts/shipwreck_grotto_front_lumber.txt"
rail = Rail(file)
def use_axe():
    held = Player.GetItemOnLayer("LeftHand")
    Items.UseItem(held)
    Target.WaitForTarget(1000, False)
    
    
shrooms = [
    0x2230,
    0x2231,
    0x222F,
    0x222E,
    0xD12,
    0xD0E,
    0xD14,
    0xD0D,
    0xD10,
    0xD16,
    0xD19,
    0xD17,
    0xD15,
    0xD11,
    0xD0C,
    0xD0F,
    0xD18,
    0xD13,
]
    
def find_tree():
    positions = [
        (0, 1),
        (0,-1),
        (1, 0),
        (1,1),
        (1, -1),
        (-1,0),
        (-1,1),
        (-1,-1),
        ]
    for x, y in positions:
        s = Statics.GetStaticsTileInfo(Player.Position.X+x, Player.Position.Y +y, Player.Map)
        for info in s:
            print(info.StaticID)
            if info.StaticID in buggedTreeTypes:
                Player.ChatSay("bugged tree type")
            if info.StaticID in treeTypes:
                return Player.Position.X+x, Player.Position.Y+y, info.StaticID
        #else:
            #Player.ChatSay("unknown tree type")
    return None
    
def hit_tree():
    use_axe()
    tree = find_tree()
    if tree:
        x, y, static_id = tree
        Target.TargetExecute(x, y, Player.Position.Z, static_id)
        Misc.Pause(1000)
        return True
    return False

if Player.CheckLayer("RightHand"):
    Player.UnEquipItemByLayer("RightHand", 1000)
    Misc.Pause(1000)
    
if Player.CheckLayer("LeftHand"):
    Player.UnEquipItemByLayer("LeftHand", 1000)  
    Misc.Pause(1000)

    
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
            print(uses_remaining)
            if uses_remaining < remaining_min:
                remaining_min = uses_remaining
                tool = tinker_tool
        if len(tinker_tools) == 1 and make_if_necessary:
            make_tinker_tool()
            continue
        return tool
    
def make_tinker_tool():
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
    
while True:
    rail.advance()
        
    if not Player.CheckLayer("LeftHand"):
        axe = Items.FindByID(axe_id,-1, Player.Backpack.Serial)
        if axe:
            Player.EquipItem(axe)
            Misc.Pause(1000)
        else:
            tinker_hatchet()
            continue
            
    Journal.Clear()
    
    if not find_tree():
        continue
    
    while True:
        if Player.Weight > Player.MaxWeight - 50 or Player.Weight > 400:
            logs = Items.FindByID(0x1BE0, -1, Player.Backpack.Serial)
            while logs:
                Items.Move(logs,storage,-1)
                Misc.Pause(1000)
                logs = Items.FindByID(0x1BE0, -1, Player.Backpack.Serial)
        if Player.GetSkillStatus("Lumberjacking") == 0 and Player.GetRealSkillValue("Lumberjacking") == 99.9:
            Player.SetSkillStatus("Lumberjacking",2)    
        hit_tree()
        Misc.Pause(1000)
        if Journal.Search("There's not enough") or not Player.CheckLayer("LeftHand"):
            break
        if not (Journal.Search("You hack") or Journal.Search("You chop")):
            break
        Journal.Clear()

