while Player.GetSkillValue("Magery") < 100:
    current_magery = Player.GetSkillValue("Magery")
    while Player.GetSkillValue("Magery") == current_magery:
        if Player.Hits < 50:
            Player.UseSkill("Spirit Speak")
            Misc.Pause(3500)
            continue
        if Player.Mana < 50:
            Player.UseSkill("Meditation")
            Misc.Pause(10000)
            continue
            

        if Player.GetSkillValue("Magery") < 20:
            Spells.CastMagery("Heal")
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
            Spells.CastMagery("Bless")
            Target.WaitForTarget(5000, False)
            Target.Self()
            Misc.Pause(1000)
            continue
        if Player.GetSkillValue("Magery") < 60:
            Spells.CastMagery("Greater Heal")
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
            Spells.CastMagery("Mass Dispel")
            Target.WaitForTarget(5000, False)
            Target.Self()
            Misc.Pause(1000)
            continue     
            
    for i in range(50):
        while Player.Mana < 50:
            Player.UseSkill("Meditation")
            Misc.Pause(10000)
        Spells.CastMagery("Magic Lock")
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(0x40399290)
        Misc.Pause(2000)
