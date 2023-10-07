while True:
    kindling = Items.FindByID(0x0DE1,-1,Player.Backpack.Serial)
    if kindling:
        Items.UseItem(kindling)
    Misc.Pause(1000*60*5 + 2000)