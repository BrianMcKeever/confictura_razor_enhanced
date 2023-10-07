
weapons = {
    "Fudly": 0x4041C6E1,
    "Paavu": 0x40479758
    }
hold = 0x405929DE

friendlies = [
    0x00048BAF, #Paavu
    0x000607DC, #Fudly
    0x0003341D, #Oscar Foul
    0x00033251, #Shady Waters
    0x00032FDD, #Salty Pete
    
    ]
for n in friendlies:
    Misc.IgnoreObject(n)

isCaptain = Player.Name == "Fudly" or Player.Name == "Oscar Foul"

if isCaptain:
    Player.ChatSay("Raise Anchor")
while True:
    spots = [
        (4, 4),
        (-4, -4),
        (4, -4),
        (-4, 4),
    ]
    fish = Items.FindByID(0x0DD6,-1,Player.Backpack.Serial) #wonderous fish
    if fish:
        Items.UseItem(fish)
        Misc.Pause(1000)
    for x, y in spots:
        filter = Mobiles.Filter()
        filter.CheckIgnoreObject = True
        
        mobs = Mobiles.ApplyFilter(filter)
        if len(mobs) > 0:
            Player.UnEquipItemByLayer("RightHand",1000)
            Misc.Pause(1000)
            
            Player.EquipItem(weapons[Player.Name])
            Misc.Pause(1000)
            while len(Mobiles.ApplyFilter(filter)) > 0:
                if IsFudly:
                    Misc.Beep()
                if Player.Hits < Player.HitsMax - 50 and not Player.Poisoned:
                    Player.UseSkill("Spirit Speak")
                    Misc.Pause(3000)
                Misc.Pause(1000)
            Player.UnEquipItemByLayer("RightHand",1000)
            Misc.Pause(1000)
        elif Player.CheckLayer('RightHand'):
            equipped = Player.GetItemOnLayer('RightHand')
            if equipped.Serial == weapons[Player.Name]:
                Player.UnEquipItemByLayer("RightHand",1000)
                Misc.Pause(1000)
                
        if Player.CheckLayer('RightHand') == 0:
            pole = Items.FindByID(0x0DC0,-1,Player.Backpack.Serial)
            if pole:
                Player.EquipItem(pole)
                Misc.Pause(1000)
        Items.UseItem(Player.GetItemOnLayer('RightHand'))
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(Player.Position.X + x, Player.Position.Y + y,-5)
        Misc.Pause(10000)
    if isCaptain:
        Player.ChatSay("forward one")
    Misc.Pause(1000)
    
    if Player.Weight > Player.MaxWeight - 10:
        Player.ChatSay("Lower Anchor")
        Misc.Pause(1000)
        Items.UseItem(hold)
        Misc.Pause(1000)
        Organizer.RunOnce("fishing",Player.Backpack.Serial,hold,1000)
        Misc.Pause(10000)
        Player.ChatSay("Raise Anchor")
        Misc.Pause(1000)