class Rover:

    def __init__(self, pos, dir):
        """
        pos[0] is E,W-dir
        pos[1] is N,S-dir
        """
        self.pos = pos
        self.dir = dir


    def position(self):
        return self.pos

    def direction(self):
        return self.dir

    def forward(self):
        if self.pos[1] < 10:
            self.pos[1] += 1
        else:
            self.pos[1] = 0
        return self.pos

    def backward(self):
        if self.pos[1] > 0:
            self.pos[1] -= 1
        else:
            self.pos[1] = 10
        return self.pos
    
    def right(self):
        if self.dir == "N":
            self.dir = "E"
        elif self.dir == "E":
            self.dir = "S"
        elif self.dir == "S":
            self.dir = "W"
        elif self.dir == "W":
            self.dir = "N"
        return self.dir

    def left(self):
        self.pos[0] = 0
        return self.pos
