def makeTool():
    Misc.Beep()
    halt

    tool = Items.FindByID(0x1EB8,-1,Player.Backpack.Serial) #tinkering kit
    if tool:
        print("make tool")
        Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 135)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0)
    else:
        Misc.ScriptStopAll(True)
        
scissors = Items.FindByID(0x0F9F,-1,Player.Backpack.Serial) #scissors
if not scissors:
    print("no scissors")
    halt
    
#20.7 - 45.7 = +25
#74.6
while True:
    if Player.GetSkillValue("Tailoring") >= 40:# 10 + 25:
        Misc.Beep()
        done
        halt
    Misc.Pause(1000)
    tool = Items.FindByID(0x4C81,-1,Player.Backpack.Serial) #sewing kit
    if not tool:
        makeTool()
        continue


    recycleList = [0x1544, #skullcap 0
        0x2306, #flower garland 10
        0x153B, #half apron 20.7
        0x2794,0x279C,0x278F,0x279A,0x1515,0x1F00,0x153D,0x152E,0x152F]
    for smeltable in recycleList:
        item = Items.FindByID(smeltable,-1,Player.Backpack.Serial)
        if item:
            print("smelt")
            Items.UseItem(scissors)
            Target.WaitForTarget(5000, False)
            Target.TargetExecute(item)
            break
    else:
        print("Make last")
        Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 5000)
        Gumps.SendAction(949095101, 21) #make last
        Gumps.WaitForGump(949095101, 5000)
        Gumps.CloseGump(949095101)

       

