while True:
    tools = Items.FindByID(0x1EB8,0,Player.Backpack.Serial)
    Items.UseItem(tools)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 21)
