from create_food import fuel
Timer.Create("skill",1)
while Player.GetSkillValue("Bushido") < 100:
    if Player.Hits < 50:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3500)
        continue
    fuel()
    if Player.Mana > 10:
        if Player.GetSkillValue("Bushido") < 60:
            Spells.CastBushido("Confidence")
        elif Player.GetSkillValue("Bushido") < 75:
            Spells.CastBushido("Counter Attack")
        elif Player.GetSkillValue("Bushido") < 100:
            Spells.CastBushido("Evasion")
    Misc.Pause(2000)
