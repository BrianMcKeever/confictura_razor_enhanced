Journal.Clear()
while True:
    if Player.HitsMax - 50 > Player.Hits: 
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
        continue
    if Journal.Search("You missed") or Journal.Search("You inflict"):
        Journal.Clear()
        Misc.Pause(1000)
    if Player.Mana > 30 and not Journal.Search("You prepare"):
        Spells.CastNinjitsu("Death Strike Strike")
        Misc.Pause(1000)
    
