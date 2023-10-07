Timer.Create("skill",1)
while True:
    Misc.Pause(1000)
    
    if Timer.Check("skill"):
        Player.UseSkill("Detect Hidden")
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(0x4B759)
        Timer.Create("skill",10000)