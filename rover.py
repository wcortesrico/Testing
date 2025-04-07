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
        self.pos[0] += 1
        return self.pos

    def left(self):
        if self.pos[0] > 0:
            self.pos[0] -= 1
        else:
            self.pos[0] = 10
        return self.pos
