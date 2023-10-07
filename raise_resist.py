
while Player.GetSkillValue("Magic Resist") < 100:
    Spells.CastMagery("Weaken")
    Target.WaitForTarget(500, False)
    Target.Self()
    Misc.Pause(1000)
    if Player.Hits < 100:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
