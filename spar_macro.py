while True:
    
    Player.AttackLast()
    if Player.Hits < 100:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
    Misc.Pause(1000)