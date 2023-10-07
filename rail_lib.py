from os.path import exists

class Rail:            
    def load_rail(self, file_name):
        if not exists(file_name):
            raise Exception("file doesn't exist")
        points = []
        f = open(file_name, "r")
        for line in f:
            split = line.split(" ")
            i = int(split[0])
            x = int(split[1])
            y = int(split[2])
            z = int(split[3])
            points.append((i, x, y, z))
        f.close()
        return points
        
    def __init__(self, file_name, looping = True):
        self._rail = self.load_rail(file_name)
        self._position = 0
        self._looping = looping
        
    def path(self, x, y, z):
        while Player.Position.X != x or Player.Position.Y != y:
            position = Player.Position
            Player.PathFindTo(x,y,z)
            while True:
                Misc.Pause(1000)
                if Player.Position == position:
                    break
                position = Player.Position
                    

    
    def advance(self):
        i, x, y, z = self._rail[self._position]
        current = Player.Position
        self.path(x, y, z)
        print("Player at %s %s node %s"%(Player.Position.X, Player.Position.Y, i))
        
        self._position += 1
        if self._position == len(self._rail):
            if self._looping:
                self._position = 0
            else:
                return False
        return True
    
    def reset(self):
        self._position = 0
        