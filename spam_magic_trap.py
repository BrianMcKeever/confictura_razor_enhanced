while True:
    Spells.CastMagery("Magic Trap")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(0x4043D500)
    Misc.Pause(1000)