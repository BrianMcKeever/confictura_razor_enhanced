Journal.Clear()
while True:
    Spells.CastNecro("Curse Weapon")
    Misc.Pause(1000)
    if not Journal.Search("You have"):
        break
    Journal.Clear()
while True:
    Spells.CastNecro("Vampiric Form")
    Misc.Pause(1000)
    