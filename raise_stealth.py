while True:
    if Player.Visible or Player.GetSkillValue("Hiding") < 30:
        Player.UseSkill("Hiding")
    else:
        Player.UseSkill("Stealth")
    Misc.Pause(10500)