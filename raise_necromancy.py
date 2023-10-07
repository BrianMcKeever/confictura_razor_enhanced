from create_food import fuel

while Player.GetSkillValue("Necromancy") < 20:
    Spells.CastNecro("Curse Weapon")
    Misc.Pause(1000)
while Player.GetSkillValue("Necromancy") < 60:
    fuel()
    if Player.Hits > 100:
        Spells.CastNecro("Pain Spike")
        Target.WaitForTarget(5000)
        Target.Self()
    Misc.Pause(2000)
while Player.GetSkillValue("Necromancy") < 70:
    fuel()
    Spells.CastNecro("Horrific Beast")
    Misc.Pause(1000)
Spells.CastNecro("Wraith Form")
while Player.GetSkillValue("Necromancy") < 90:
    fuel()
    Spells.CastNecro("Wither")
    Misc.Pause(1000)
while Player.GetSkillValue("Necromancy") < 100:
    fuel()
    if Player.Hits < 100:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
    else:
        Spells.CastNecro("Lich Form")
        Misc.Pause(1000)

