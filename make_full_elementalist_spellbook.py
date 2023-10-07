from misc import *

spellbooks = Items.FindAllByID(0x6421,0,Player.Backpack.Serial,0)
book_list = []
for spellbook in spellbooks:
    props = Items.GetPropStringList(spellbook)
    if int(props[1].split(' ')[0]) == 0:
        book_list.append(spellbook)

pages = [1]
spell_buttons = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100, 107, 114, 121, 128, 135, 142, 149, 156, 163, 170, 177, 184, 191, 198, 205, 212, 219]



def get_inscribe_pen():
    pen = Items.FindByID(0x2051,0x0060, Player.Backpack.Serial,1)
    if not pen:
        make_pen()
        pen = Items.FindByID(0x2051,0x0060, Player.Backpack.Serial,1)
        if not pen:
            Misc.Beep()
            halt
    return pen

def get_scribed_scroll():
    for item in Player.Backpack.Contains:
        if "scroll" in item.Name.lower() and not "blank" in item.Name.lower():
            return item
    return None
    
    
def make_spell(spell_button, book):
    Restock.ChangeList("inscribe elementalist")

    while True:
        while Player.Mana < 50:
            Player.UseSkill("Meditate")
            Misc.Pause(10500)
            
        Restock.FStart()
        while Restock.Status():
            Misc.Pause(500)
        Misc.Pause(1000)
        
        pen = get_inscribe_pen()
        Items.UseItem(pen)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 1)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, spell_button)
        Gumps.WaitForGump(949095101, 1000)
        if  Gumps.LastGumpTextExist("don't have that spell"):
            break
        Gumps.SendAction(949095101, 0)
        Misc.Pause(3000)
        scroll = get_scribed_scroll()
        if scroll:
            while get_scribed_scroll():
                Items.Move(scroll, book, 1)
                Misc.Pause(2000)
            break


            
for spell in spell_buttons:
    for book in book_list:            
        make_spell(spell, book)
            
Misc.Beep()
