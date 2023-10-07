from misc import *

while True:
    pen = Items.FindByID(0x2051,-1, Player.Backpack.Serial,1)
    if not pen:
        make_pen()
        continue
    if pen:
        Items.UseItem(pen)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 21)
        Gumps.WaitForGump(949095101, 1000)
        Gumps.SendAction(949095101, 0)
        Misc.Pause(1000)
