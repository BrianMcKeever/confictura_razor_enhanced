startX = Player.Position.X
startY = Player.Position.Y
while True:
    if Player.Hits < 50:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3500)
        continue
    if Player.Mana < 15 and Player.GetSkillValue("Ninjitsu") < 85:
        Player.UseSkill("Meditation")
        while Player.Mana < Player.ManaMax:
            Misc.Pause(500)
        continue     
    if Player.GetSkillValue("Ninjitsu") < 37.5:
        Spells.CastNinjitsu("Animal Form")
        Gumps.WaitForGump(3027724650, 1000)
        Gumps.SendAction(3027724650, 11)
        Misc.Pause(2000)
        continue
    if Player.GetSkillValue("Ninjitsu") < 57.5:
        Spells.CastNinjitsu("Mirror Image")
        Misc.Pause(1000)
        fil = Mobiles.Filter()
        fil.Enabled = True
        fil.RangeMax = 1
        #fil.Notorieties = List[Byte](bytes([3,4,5,6]))
        fil.IsGhost = False
        fil.Friend = False
        mobs = Mobiles.ApplyFilter(fil)

        if len(mobs) > 0:
            nearest = Mobiles.Select(mobs,'Nearest')
            Player.Attack(nearest)
        continue
    if Player.GetSkillValue("Ninjitsu") < 85:
        if Player.Visible:
            Player.UseSkill("Hiding")
            Misc.Pause(10500)
            if Player.Visible:
                continue
            if not Player.Visible:
                Player.UseSkill("Stealth")
                Misc.Pause(10500)
                if Player.Visible:
                    continue
        Spells.CastNinjitsu("Shadowjump")
        Target.WaitForTarget(10000, False)
        if Player.Position.X == startX and Player.Position.Y == startY:
            Target.TargetExecute(Player.Position.X, Player.Position.Y -1,Player.Position.Z)
        else:
            Target.TargetExecute(startX, startY,Player.Position.Z)
        Misc.Pause(2000)
        continue
    if Player.GetSkillValue("Ninjitsu") < 100 and Player.Mana > 30:
        if Journal.Search("You inflict") or Journal.Search("You missed"):
            Journal.Clear()
            Misc.Pause(1000)
            Spells.CastNinjitsu("Death Strike")
            Misc.Pause(1000)
        elif Journal.Search("You prepare"):
            pass
        elif Player.Mana > 30:
            Spells.CastNinjitsu("Death Strike")
            Misc.Pause(1000)
        continue
        

