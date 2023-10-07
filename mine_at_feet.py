from util import get_ore_spade, make_ore_spade
deposit = 0x40324B52
while True:
    #tool = Items.FindByID(0x0F3A,0x096d,Player.Backpack.Serial) #ore spade
    #tool = Items.FindByID(0x0E86,0x0000,Player.Backpack.Serial) #pickaxe
    #tool = Items.FindByID(0x0F39,0,Player.Backpack.Serial) #shovel
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