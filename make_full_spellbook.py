from misc import *

spellbooks = Items.FindAllByID(0x0EFA,0,Player.Backpack.Serial,0)
book_list = []
for spellbook in spellbooks:
    props = Items.GetPropStringList(spellbook)
    if int(props[1].split(' ')[0]) == 0:
        book_list.append(spellbook)

pages = [8, 15, 22, 29]
level_one_spells = [ 2,  9, 16, 23, 30, 37,  44,  51]
level_two_spells = [58, 65, 72, 79, 86, 93, 100, 107]

level_three_spells = [ 2,  9, 16, 23, 30, 37,  44,  51]
level_four_spells =  [58, 65, 72, 79, 86, 93, 100, 107]

level_five_spells = [ 2,  9, 16, 23, 30, 37,  44,  51] 
level_six_spells =  [58, 65, 72, 79, 86, 93, 100, 107]

level_seven_spells = [ 2,  9, 16, 23, 30, 37,  44,  51]
level_eight_spells = [58, 65, 72, 79, 86, 93, 100, 107]

def get_pen():
    pen = Items.FindByID(0x2051,-1, Player.Backpack.Serial,1)
    if not pen:
        make_pen()
        pen = Items.FindByID(0x2051,-1, Player.Backpack.Serial,1)
        if not pen:
            Misc.Beep()
            halt
    return pen

def make_spell(tab, spell, book):
    Restock.ChangeList("inscribe")

    while True:
        while Player.Mana < 50:
            Player.UseSkill("Meditate")
            Misc.Pause(10500)
            
        Restock.FStart()
        while Restock.Status():
            Misc.Pause(500)
        Misc.Pause(1000)
        
        pen = get_pen()
        Items.UseItem(pen)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, tab)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, spell)
        Gumps.WaitForGump(949095101, 1000)
        if  Gumps.LastGumpTextExist("don't have that spell"):
            break
        Gumps.SendAction(949095101, 0)
        Misc.Pause(3000)

        for item in Player.Backpack.Contains:
            if "scroll" in item.Name and not "blank" in item.Name:
                weight = Player.Backpack.Weight
                while Player.Backpack.Weight == weight:
                    Items.Move(item, book, 1)
                    Misc.Pause(1000)
                break
        else:
            continue
        break

            
triplets = [
    (8,  level_one_spells, level_two_spells), 
    (15, level_three_spells, level_four_spells), 
    (22, level_five_spells, level_six_spells),
    (29, level_seven_spells, level_eight_spells),
    ]
for tab, low_spells, high_spells in triplets:
    for spell in low_spells:
        for book in book_list:            
            make_spell(tab, spell, book)

    for spell in high_spells:
        for book in book_list:            
            make_spell(tab, spell, book)
            
Misc.Beep()

