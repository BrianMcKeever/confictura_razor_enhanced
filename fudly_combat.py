reg_jars = [0x1005, 0x1006, 0x09C8, 0x1007]
scrolls = [0x4CC4, 0x4CC5,0x2267,0x1F30]
ided_scrolls = [0x1F6C,0x1F66,0x1F33,0x1F31,0x1F34,0x226A,0x1F64,0x226D,0x226C,0x1F46,0x1F32,0x2269,0x2270,0x1F6A,0x1F48,0x1F49,0x1F65,0x1F67, 0x226B,0x1F61, 0x1F62,0x1F68,0x1F4C,0x2267,0x1F30,0x226F,0x1F55,0x1F60,0x1F51,0x644C,0x644D,0x1F5E,0x1F3B,0x1F52,0x1F54,0x1F2D, 0x1F43, 0x1F3A, 0x1F45, 0x1F3F, 0x1F56, 0x1F5B, 0x1F4D, 0x1F4F, 0x1F4B]
unided_names = ["strange item", "weird item", "peculiar item", "curious item", "bizarre item", "odd item", "unusual item"]
spells_i_want = ["water e",]
while True:
    for reg_jar in reg_jars:
        jar = Items.FindByID(reg_jar,-1, Player.Backpack.Serial)
        if jar:
            if "of reagents" in jar.Name:
                Items.UseItem(jar)
                Misc.Pause(1000)
    for scroll in scrolls:
        s = Items.FindByID(scroll,-1, Player.Backpack.Serial)
        if s:
            if "magic scroll" in s.Name:
                Items.UseItem(s)
                Misc.Pause(1000)
    for ided_scroll in ided_scrolls:
        s = Items.FindByID(ided_scroll,-1, Player.Backpack.Serial)
        if s:
            for spell_name in spells_i_want:
                if spell_name in s.Name:
                    break
            else:
                print("drop", s.Name)
                Items.MoveOnGround(s,-1,Player.Position.X,Player.Position.Y+1,Player.Position.Z)
                Items.DropItemGroundSelf(s, -1)
                Misc.Pause(1000)

    for unided_name in unided_names:
        filter = Items.Filter()
        filter.Enabled = True
        filter.OnGround = 0
       
        items = Items.ApplyFilter(filter)
        for item in items:
            if item.Container != Player.Backpack.Serial:
                continue
            if unided_name in item.Name:
                Items.UseItem(item)
                Misc.Pause(1000)
    Misc.Pause(200)