while True:
    Player.UseSkill("Taste ID")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(0x40093012)
    Misc.Pause(2000)