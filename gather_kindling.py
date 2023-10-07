treeTypes = [3296, 3492, 3484, 3476, 3496, 3488, 3275, 3300, 3282, 3284, 3290, 3289, 3279, 3278, 3303]
buggedTreeTypes = [3230]
while True:
    Items.UseItem(0x4054317A)
    Target.WaitForTarget(10000, False)
    s = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y - 1, Player.Map)
    print("new")
    for info in s:
        print(info.StaticID)
        if info.StaticID in buggedTreeTypes:
            Player.ChatSay("bugged tree type")
            break
        if info.StaticID in treeTypes:
            z = Statics.GetLandZ(Player.Position.X,Player.Position.Y,Player.Map)
            print(z)
            Target.TargetExecute(Player.Position.X, Player.Position.Y - 1, 0, info.StaticID)
            break
    else:
        Player.ChatSay("unknown tree type")
    Misc.Pause(1000)