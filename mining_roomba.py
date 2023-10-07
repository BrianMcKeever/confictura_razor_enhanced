from System import Random
from System.Collections.Generic import List
from System import Int32

dir = ['North', 'Northeast', 'East', 'Southeast', 'South', 'Southwest', 'West', 'Northwest']

touch_timer = Timer.Create("last_touched",60*1000)

def Direction(ignored = ""):
    dir = Player.Direction
    if dir == "Down":
        return "Southeast"
    if dir == "Up":
        return "Northwest"
    if dir == "Left":
        return "Southwest"
    if dir == "Right":
        return "Northeast"
    return dir
    
def Undirection(direction):
    if direction == "Southeast":
        direction = "Down"
    elif direction == "Northwest":
        direction = "Up"
    elif direction == "Southwest":
        direction = "Left"
    elif direction == "Northeast":
        direction = "Right"
    return direction


def Walk(direction):
    direction = Undirection(direction)
    return Player.Walk(direction)
    
def Turn(direction):
    return Walk(direction)
    
def GetDirectionDropOffset():
    if Direction('self') == 'North':
        offset_x = 0
        offset_y = -1
    elif Direction('self') == 'Northeast':
        offset_x = 1
        offset_y = -1
    elif Direction('self') == 'East':
        offset_x = 1
        offset_y = 0
    elif Direction('self') == 'Southeast':
        offset_x = 1
        offset_y = 1
    elif Direction('self') == 'South':
        offset_x = 0
        offset_y = 1
    elif Direction('self') == 'Southwest':
        offset_x = -1
        offset_y = 1
    elif Direction('self') == 'West':
        offset_x = -1
        offset_y = 0
    elif Direction('self') == 'Northwest':
        offset_x = -1
        offset_y = -1
    return offset_x, offset_y

def move_ore():
    ore = getOreOnGround()
    if ore != None:
        offset_x, offset_y = GetDirectionDropOffset()
        Items.MoveOnGround(ore,-1,Player.Position.X + offset_x,Player.Position.Y + offset_y, 0)
        Misc.Pause(1000)   
        touch_timer = Timer.Create("last_touched",60*1000)
        
#Roomba Walk, turn a random directions and contiue
def Roomba():
    int = Random().Next(8) # 0-7

    if not Walk(Direction('self')):
        Player.ChatSay(dir[int])
        print(dir[int])
        Turn(dir[int])

    else:
        move_ore()
    return

#Did you walk out of the cave?
def OutofCave():
    if (Direction('self') == "North"):
        Turn("South")
        BackinCave()
    elif (Direction('self') == "Northeast"):
        Turn("Southwest")
        BackinCave()
    elif (Direction('self') == "East"):
        Turn("West")
        BackinCave()
    elif (Direction('self') == "Southeast"):
        Turn("Northwest")
        BackinCave()
    elif (Direction('self') == "South"):
        Turn("North")
        BackinCave()
    elif (Direction('self') == "Southwest"):
        Turn("Northeast")
        BackinCave()
    elif (Direction('self') == "West"):
        Turn("East")
        BackinCave()
    elif (Direction('self') == "Northwest"):
        Turn("Southeast")
        BackinCave()
    return

#walk 6 steps to get back into the cave
def BackinCave():   
    print("back in cave")
    for x in range(6):
        Walk(Direction('self'))
    return

#Make a shovel when none are left
def MakeShovel ():
    tinkerTools = Items.FindByID(0x1EB8,-1, Player.Backpack.Serial,0)
    if tinkerTools:
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,29)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,93)
        Gumps.WaitForGump(0x38920abd,5000)
        Gumps.SendAction(0x38920abd,0)
    else:
        Player.ChatSay("Out of tinker tools")
        halt
    return
    
def getOreOnGround():
    filter = Items.Filter()
    filter.Graphics = List[Int32]([0x19b9,])
    #filter.Graphics = [0x19b9,]
    filter.OnGround = 1
    filter.RangeMax = 1
    oreList = Items.ApplyFilter(filter)
    
    if len(oreList) > 0:
        ore = oreList[0]
    else:
        ore = None
    return ore

#Smelt ore in mobile forge
def Smelt():
    print("smelt")
    
    ore = getOreOnGround()
    
    backpackOre = Items.FindByID(0x19b9, 0, Player.Backpack.Serial, 0)
    if ore:
        Items.UseItem(backpackOre)
        Target.WaitForTarget(2000)
        Target.TargetExecute(ore)

    else:
        offset_x, offset_y = GetDirectionDropOffset()
        if backpackOre:
            Items.MoveOnGround(backpackOre, -1,Player.Position.X + offset_x, Player.Position.Y + offset_y,0)
    Misc.Pause(2000)
    
#Main loop
while not Player.IsGhost:
    if not Timer.Check("last_touched"):
        print("touching")
        move_ore()
    #Look for Shovel or Pickaxe
    shovel = Items.FindByID(0x0F3A,-1, Player.Backpack.Serial,0) #ore spade
    if shovel == None:
        MakeShovel()
        continue
        
    Items.UseItem(shovel)
    Target.WaitForTarget(5000)

    #dig in front of you
    if (Direction() == "North"):
        Target.TargetExecute(Player.Position.X,Player.Position.Y -1,0,1341)
    elif (Direction() == "Northeast"):
        Target.TargetExecute(Player.Position.X + 1,Player.Position.Y-1,0)
    elif (Direction() == "East"):
        Target.TargetExecute(Player.Position.X + 1,Player.Position.Y,0)
    elif (Direction() == "Southeast"):
        Target.TargetExecute(Player.Position.X + 1,Player.Position.Y + 1,0)
    elif (Direction() == "South"):
        Target.TargetExecute(Player.Position.X,Player.Position.Y + 1,0)
    elif (Direction() == "Southwest"):
        Target.TargetExecute(Player.Position.X-1,Player.Position.Y +1,0)
    elif (Direction() == "West"):
        Target.TargetExecute(Player.Position.X-1,Player.Position.Y,0)
    elif (Direction() == "Northwest"):
        Target.TargetExecute(Player.Position.X-1,Player.Position.Y-1,0)
    Misc.Pause(1000)

    #Move when there is nothing to mine or when a wall is hit
    if Journal.Search("There is no metal here to mine") or Journal.Search("Target cannot be seen")  or Journal.Search("You can't mine that"):
        Journal.Clear() 
        Roomba()
    #Turn around if you try to mine something other than cave floor
    #if not (Journal.Search("You loosen") or Journal.Search("You dig")):
    if Journal.Search("You can't mine there"):
        Journal.Clear()
        OutofCave()
    elif not (Journal.Search("You loosen") or Journal.Search("You dig")):
        Journal.Clear() 
        Roomba()
    #Smelt when it gets to heavy    
    if Player.Weight > Player.MaxWeight or Player.Weight >= 370:
        Smelt()
