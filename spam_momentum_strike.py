
while True:
    if Player.HitsMax - 50 > Player.Hits: 
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
        continue
    if Journal.Search("You transfer"):
        Journal.Clear()
        Misc.Pause(1000)
    if Player.Mana > 13 and not Journal.Search("You prepare"):
        Spells.CastBushido("Momentum Strike")
        Misc.Pause(1000)
    
