from util import *
source_container = 0x403CAD9A
trash_barrel = 0x403F569B
wait_delay = 4000

Items.UseItem(source_container)
Misc.Pause(1000)
def smelt():
    smeltList = [
        0x2677, #dagger
        0x268C, #mace
        0x2681, #mace
        0x0F5D, #mace
        0x0F5C, #mace
        0x1441, #cutlass
        0x268E, #cutlass
        0x13B6, #scimitar
        0x268F, #scimitar
        0x1401, #kryss
        0x13FF, #katana
        0x2CFF, #katana
        0x2680, #katana
        0x27A4, #waikazashi
        0x1413, #plate gorget
        0x1414, #plate gloves
        0x1412, #plate helm
        0x2649, #plate helm
        0x0306, #plate arms
        0x1417, #plate arms
        0x0303, #plate arms
        0x0304, #plate arms
        0x1410, #plate arms
        0x0305, #plate arms
        0x27A2, #no daichi
        


        ]
    print("smelt")
    for smeltable in smeltList:
        item = Items.FindByID(smeltable,-1,Player.Backpack.Serial)
        while item:
            if Gumps.CurrentGump() != 949095101:
                tool = get_tongs()
                Items.UseItem(tool)
                Gumps.WaitForGump(949095101, wait_delay)
            
            Gumps.SendAction(949095101, 14) #smelt
            Target.WaitForTarget(wait_delay, False)
            Target.TargetExecute(item)
            Gumps.WaitForGump(949095101, wait_delay)

            item = Items.FindByID(smeltable,-1,Player.Backpack.Serial)
            if not item:
                Gumps.SendAction(949095101, 0)
                Misc.Pause(1000)
smelt()
while Player.GetRealSkillValue("Blacksmithing") < Player.GetSkillCap("Blacksmithing"):
    ingots = Items.FindByID(0x1BF2, 0, Player.Backpack.Serial)
    if not ingots or ingots.Amount < 20:
        ingots = Items.FindByID(0x1BF2, 0, source_container)
        Items.Move(ingots, Player.Backpack, 1000)
        Misc.Pause(1000)
    tool = get_tongs()
    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, wait_delay)

    if len(Player.Backpack.Contains) > 100 or Player.Weight > Player.MaxWeight or Player.Weight > 400:
        smelt()
        continue
    print("smith something")
    if Player.GetSkillValue("Blacksmithing") < 0 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 51) #dagger
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 14.5 + 49.6:
        Gumps.SendAction(949095101, 64)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 23) #mace
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 24.3 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 44) #cutlass
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 31.7 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 128) #scimitar
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 36.7 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 72) #kryss
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 44.1 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 65) #katana
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 50 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 163) #wakizashi
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 56.4 + 49.6:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 16) #plate gorget
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 58.9 + 49.6:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 9) #plate gloves
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 62.6 + 49.6:
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 30) #plate helmet
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
    if Player.GetSkillValue("Blacksmithing") < 66.3 + 49.6:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 2) #plate arms
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue 
    if Player.GetSkillValue("Blacksmithing") < 75 + 49.6:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 156) #no daichi
        Gumps.WaitForGump(949095101, wait_delay)
        Gumps.SendAction(949095101, 0)
        continue
smelt()
Misc.Beep()
