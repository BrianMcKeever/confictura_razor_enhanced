
while Player.GetSkillValue("SpellWeaving") < 100:
    power_cost = 5
    if Player.GetSkillValue("SpellWeaving") < 20 and Player.Mana > power_cost and Player.Stam > power_cost:
        Player.ChatSay(690, "[Emend")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    power_cost = 7 
    if Player.GetSkillValue("SpellWeaving") < 34.3 and Player.Mana > power_cost and Player.Stam > power_cost:
        Player.ChatSay(690, "[Eprotection")
        Misc.Pause(3000)
        continue
    power_cost = 10 
    if Player.GetSkillValue("SpellWeaving") < 48.6 and Player.Mana > power_cost and Player.Stam > power_cost:
        Player.ChatSay(690, "[Ewall")
        Target.WaitForTarget(3000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    power_cost = 14
    if Player.GetSkillValue("SpellWeaving") < 62.9 and Player.Mana > power_cost and Player.Stam > power_cost:
        Player.ChatSay(690, "[Erestoration")
        Target.WaitForTarget(3000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    power_cost = 19
    if Player.GetSkillValue("SpellWeaving") < 77.2 and Player.Mana > power_cost and Player.Stam > power_cost and Player.Hits > 150:
        Player.ChatSay(690, "[Eblast")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    if Player.GetSkillValue("SpellWeaving") < 91.5 and Player.Mana > power_cost and Player.Stam > power_cost and Player.Hits > 150:
        Player.ChatSay(690, "[Ebarrage")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    if Player.GetSkillValue("SpellWeaving") < 100 and Player.Mana > power_cost and Player.Stam > power_cost and Player.Hits > 150:
        Player.ChatSay(690, "[Edevastation")
        Target.WaitForTarget(5000, False)
        Target.Self()
        Misc.Pause(2000)
        continue
    if Player.Hits <= 150:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
        continue
    if Player.Stam < power_cost:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
        continue
    while Player.Mana < Player.ManaMax:
        Player.UseSkill("Meditation")
        Misc.Pause(10000)
