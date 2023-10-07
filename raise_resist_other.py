
while True:
    Spells.CastMagery("Weaken")
    Target.WaitForTarget(2500, False)
    Target.Last()
    Misc.Pause(2000)
    if Player.Hits < 100:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(1000)
