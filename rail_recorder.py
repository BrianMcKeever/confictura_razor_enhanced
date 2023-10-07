file_name = "route.txt"
f = open(file_name, 'a')
Journal.Clear()
route = []
while True:
    if Journal.Search("HERE"):
        Journal.Clear()
        route.append(Player.Position)
        Player.HeadMessage(0, "recorded")
    if Journal.Search("FINISH"):
        Player.HeadMessage(0, "finishing")
        break
    Misc.Pause(200)

i = 0
for point in route:
    line = "%s %s %s %s\n"%(i, point.X, point.Y, point.Z)
    #Misc.AppendToFile(file_name, line)
    f.write(line)
    print(line)
    i += 1
f.close()