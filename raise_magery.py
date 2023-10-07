from create_food import fuel
while Player.GetSkillValue("Magery") < 100:
    fuel()
    if Player.Hits < 50:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3500)
        continue
    if Player.Mana < 24:
        Player.UseSkill("Meditation")
        Misc.Pause(10000)
        continue
        

    if Player.GetSkillValue("Magery") < 20:
        Spells.CastMagery("Weaken")
        Target.WaitForTarget(500, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Magery") < 30:
        Spells.CastMagery("Cure")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Magery") < 40:
        Spells.CastMagery("Wall of Stone")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Magery") < 60:
        Spells.CastMagery("Curse")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Magery") < 85:
        Spells.CastMagery("Invisibility")
        Target.WaitForTarget(6000, False)
        Target.Self()
        Misc.Pause(1500)
        continue
    if Player.GetSkillValue("Magery") < 100:
        Spells.CastMagery("Energy Field")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(1000)
        continue        
