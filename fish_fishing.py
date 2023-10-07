from System.Collections.Generic import List
from System import Byte
hatch = 0x40434A29
trash = 0x400AA292
knife_in_house = 0x40203DFC
storage = 0x40467955
ship_key = 0x40434A2C
refill_water_rune = 0x404A166E
#buy_fishing_poles_rune = 0x404A16F6
#fisherman = 0x0000E6F1
#shipwright = 0x0000E6F6
fishing_pole_chest = 0x40399290
fish_keep_basket = 0x400542EF

friendlies = [
    0x00048BAF, #Paavu
    0x000607DC, #Fudly
    0x0003341D, #Oscar Foul
    0x00033251, #Shady Waters
    0x00032FDD, #Salty Pete
    ]
friendly_names = ["Paavu", "Fudly", "Oscar Foul", "Shady Waters", "Salty Pete"]

for n in friendlies:
    Misc.IgnoreObject(n)
    
from rail_lib import Rail
file = "house_to_trashcan.txt"
rail = Rail(file, False)
    
watered_cloth = ["soaked", "drenched", "wet ", "dripping", "waterlogged", "soggy", "sopping"]
rusty_armor = ["rusty"]
junk = ["seaweed", "skeletal bones", "sea chest", "the bones of", "weed covered", "skeletal remains", "body of"]
fish_types = [0x09CF, 0x09CE, 0x09CD, 0x09CC]
fish_to_keep = [
        0x22AC, #herring
        0x44C5, #fin
        0x22AB, #goby
        0x531E, #walleye
        0x52DE, #sea horse
        0x4305, #crappie
        0x44C6, #hake
        0x52DD, #barbel
        0x22A7, #catalufa
        0x4305, #other hake
        0x4304, #gill
    ]

storage_types = [
    0x0EED, #gold
    0x0EF0, #silver
    0x0EF0, #copper
    0x097A, #raw_fish
    ]

isCaptain = Player.Name == "Fudly" or Player.Name == "Salty Pete"

def recall(rune):
    location = Player.Position
    while location == Player.Position:
        Player.ChatSay("[EVoid")
        Target.WaitForTarget(4000)
        Target.TargetExecute(rune)
        Misc.Pause(2000)

def travel_to_house():
    rune = Items.FindByID(0x1F14,-1,Player.Backpack.Serial,0)
    if not rune:
        print("no home rune")
        Misc.Beep()
        halt
    recall(rune)
    print("recalled")
    
    rail.reset() 
    while rail.advance(): #walk to trashcan
        Misc.Pause(2000)
        pass
    
def dump_backpack():
    print("dump backpack")
    travel_to_house()  
    
    print("cutting fish")
    for fish_type in fish_types:
        fish = Items.FindByID(fish_type, 0, Player.Backpack.Serial)
        if fish and len(fish.Name) >= 4 and fish.Name.lower()[-4:] == "fish" :
            Items.UseItem(knife_in_house)
            Target.WaitForTarget(1000)
            Target.TargetExecute(fish)
            Misc.Pause(1000)
    
    print("storing stuff")
    for storage_type in storage_types:
        item = Items.FindByID(storage_type, -1, Player.Backpack.Serial)
        if item:
            Items.Move(item,storage,-1)
            Misc.Pause(1000)   
    
    for item in Player.Backpack.Contains:
        props = Items.GetPropStringList(item)
        for prop in props:
            if prop == "An Exotic Fish":
                Items.Move(item,fish_keep_basket,1)
                Misc.Pause(1000) 
        
    print("trashing")
    for item in Player.Backpack.Contains:
        for trash_name in watered_cloth + rusty_armor + junk:
            if trash_name in item.Name.lower():
                Items.Move(item,trash,1)
                Misc.Pause(1000)
    

            
def restock():
    print("restock")
    Items.OpenAt(storage,0,0)
    Misc.Pause(1000)
    
    fish_steaks = Items.FindByID(0x097B,-1, storage)
    if fish_steaks:
        Journal.Clear()
        while not Journal.Search("too full"):
            Items.UseItem(fish_steaks)
            Misc.Pause(1000)
    
    Restock.RunOnce("fishing_poles",fishing_pole_chest, Player.Backpack.Serial,1000)   
    while Restock.Status():
        Misc.Pause(1000)
            
    recall(refill_water_rune)
    Journal.Clear()
    while not Journal.Search("too quenched"):
        waterskin = Items.FindByID(0x098F, 0, Player.Backpack.Serial) #waterskin
        if waterskin:
            Items.UseItem(waterskin)
            Misc.Pause(1000)
            
    travel_to_house()
  

def recall_to_boat():       
    print("recall to boat")
    recall(ship_key)
    
    h = Items.FindBySerial(hatch)
    if not h:
        Misc.Beep()
        halt
    print("before", h.Position.X, h.Position.Y, Player.Position.X, Player.Position.Y)
    while Player.Position.X != h.Position.X or Player.Position.Y != h.Position.Y:
        if Player.Stam == Player.StamMax:
            Player.PathFindTo(h.Position)
        Misc.Pause(2000)
        h = Items.FindBySerial(hatch)
        Items.WaitForProps(h, 10000)
    print("after", h.Position.X, h.Position.Y, Player.Position.X, Player.Position.Y)
    


def handle_vitals():
    power = min(Player.Stam, Player.Mana)
    if Player.Poisoned and power > 7:
        Player.ChatSay("[Epurge")
        Target.WaitForTarget(3000)
        Target.Self()
        Misc.Pause(1000)
    if Player.Hits < Player.HitsMax - 50 and not Player.Poisoned and Player.Mana > 10:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(3000)
    if Player.Mana < 24:
        Player.UseSkill("Meditation")
        Misc.Pause(2000)

def count_backpack():
    return len(Player.Backpack.Contains) + 10
if isCaptain:
    Player.ChatSay("Raise Anchor")
    
    
def restart():
    print("restart")
    dump_backpack()
    restock()
    recall_to_boat()
   
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
        h = Items.FindBySerial(hatch)
        if not h or (Player.Position.X != h.Position.X or Player.Position.Y != h.Position.Y):
            restart()
            
        filter = Mobiles.Filter()
        filter.CheckIgnoreObject = True
        filter.RangeMax = 10
        filter.IsGhost = False
        filter.Notorieties = List[Byte](bytes([3,4,5,6]))
        
        mobs = Mobiles.ApplyFilter(filter)
        handle_vitals()
        while len(mobs) > 0:
            if isCaptain:
                Misc.Beep()
            power = min(Player.Stam, Player.Mana)
            handle_vitals()
            if mobs[0].Name in friendly_names:
                Misc.IgnoreObject(mobs[0])
                mobs = Mobiles.ApplyFilter(filter)
                continue
            if power > 24 and Player.Hits > Player.HitsMax - 50 and not Player.Poisoned:
                Player.ChatSay("[Estorm")
                Target.WaitForTarget(3000)
                Target.TargetExecute(mobs[0])               
                Misc.Pause(2000)
            else:
                Player.UseSkill("Meditation")
                Misc.Pause(2000)
            mobs = Mobiles.ApplyFilter(filter)
                
        if Player.CheckLayer('RightHand') == 0:
            pole = Items.FindByID(0x0DC0,-1,Player.Backpack.Serial)
            if pole:
                Player.EquipItem(pole)
                Misc.Pause(1000)
        if Player.GetSkillStatus("Fishing") == 0 and Player.GetRealSkillValue("Fishing") >= 79.9:        
            Player.SetSkillStatus("Fishing", 2)
        Items.UseItem(Player.GetItemOnLayer('RightHand'))
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(Player.Position.X + x, Player.Position.Y + y,-5)
        Misc.Pause(10000)
        if Journal.Search("!reload"):
            print("reloading")
            Misc.ScriptRun("fish_fishing")
        if Journal.Search("be biting"):
            Journal.Clear()
            if isCaptain:
                for i in range(8):
                    Player.ChatSay("forward one")
                    Misc.Pause(1000)
            
    Misc.Pause(1000)
    if isCaptain and Journal.Search("we've stopped"):
        Player.ChatSay("turn left")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("forward one")
        Misc.Pause(1000)
        Player.ChatSay("turn left")
        Misc.Pause(1000)
        Journal.Clear()
    
    if Player.Weight > Player.MaxWeight - 10 or count_backpack() > 120 or len(Items.FindAllByID(0x0DC0,0, Player.Backpack.Serial, 0)) == 0 and Player.CheckLayer('RightHand') == 0:
        restart()

        

