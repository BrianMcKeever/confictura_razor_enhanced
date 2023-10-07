while True:
    Player.UseSkill("Detect Hidden")
    Target.WaitForTarget(1000, False)
    Target.Self()
    Misc.Pause(10000)