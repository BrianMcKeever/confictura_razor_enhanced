
while True:
    Spells.CastMagery("Greater Heal")
    Target.WaitForTarget(3000, False)
    Target.TargetExecute(0x13DF5)
    Misc.Pause(2000)