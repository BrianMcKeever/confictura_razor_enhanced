from util import get_tinker_tool, get_ore_spade, make_ore_spade

storage = 0x405B018E #bag of holding

    
from rail_lib import Rail
file = "Scripts\grey_mine_route.txt"

rail = Rail(file)
    
    
while True:
    rail.advance()
    Journal.Clear()
    
    while True:
        tool = get_ore_spade()
        if not tool:
            make_ore_spade()
            continue
        Items.UseItem(tool)
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(Player.Position.X,Player.Position.Y,0,1341)
        Misc.Pause(1000)
        
        if Player.Weight > Player.MaxWeight - 50 or Player.Weight > 400:
            ore = Items.FindByID(0x19B9, -1,Player.Backpack.Serial)
            while ore:
                Items.Move(ore, 0x405B018E, 999) #bag of holding
                Misc.Pause(1000)
                ore = Items.FindByID(0x19B9, -1,Player.Backpack.Serial)
        Misc.Pause(1000)
        if Journal.Search("no metal"):
            break
        Journal.Clear()

