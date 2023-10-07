while True:
    for i in range(10000):
        if Player.Hits < Player.HitsMax - 5:
            Player.UseSkill("Spirit Speak")
            Misc.Pause(3000)
        Misc.Pause(10)
    Player.UseSkill("Spirit Speak")
    Misc.Pause(3000)