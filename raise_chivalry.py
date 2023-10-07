while True:
    if Player.Hits < 50:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3500)
        continue
    if Player.Mana < 50:
        Player.UseSkill("Meditation")
        Misc.Pause(10000)
        continue     
    if Player.GetSkillValue("Chivalry") < 15:
        Spells.CastChivalry("Close Wounds")
        Target.WaitForTarget(500, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Chivalry") < 40:
        Spells.CastChivalry("Consecrate Weapon")
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Chivalry") < 60:
        Spells.CastChivalry("Dispel Evil")
        Target.WaitForTarget(500, False)
        Target.Self()
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Chivalry") < 70:
        Spells.CastChivalry("Enemy of One")
        Target.WaitForTarget(500, False)
        Target.Self()
        Misc.Pause(1000)
        continue

    if Player.GetSkillValue("Chivalry") < 90:
        Spells.CastChivalry("Holy Light")
        Misc.Pause(1000)
        continue
    if Player.GetSkillValue("Chivalry") < 100:
        Spells.CastChivalry("Noble Sacrifice")
        Misc.Pause(1000)
        continue
        

