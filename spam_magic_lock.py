while True:
    Spells.CastMagery("Magic Lock")
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(0x40399290)
    Misc.Pause(1000)