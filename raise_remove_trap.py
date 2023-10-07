while True:
    if Player.Hits < 250:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
        continue
    Spells.CastMagery("Magic Trap")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(0x40467955)
    Misc.Pause(1000)
    Items.UseItem(0x40467955)
    Misc.Pause(1000)