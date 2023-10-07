source = 0x403CAD9A
fire = 0x402E0A70

fish_steak_id = 0x097A
while True:
    steak = Items.FindByID(fish_steak_id,-1, Player.Backpack.Serial)
    if steak:
        Items.UseItem(steak)
        Target.WaitForTarget(2000)
        Target.TargetExecute(fire)
        Misc.Pause(3000)
    else:
        steak = Items.FindByID(fish_steak_id,-1, source)
        if steak:
            Items.Move(steak, Player.Backpack.Serial, 1)
    Misc.Pause(1500)