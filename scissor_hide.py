
while True:
    Misc.Pause(1000)
    hide = Items.FindByID(0x1079, -1, Player.Backpack.Serial)
    if hide != None:
        scissors = Items.FindByID(0x0F9F, -1, Player.Backpack.Serial)
        Items.UseItem(scissors)
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(hide)