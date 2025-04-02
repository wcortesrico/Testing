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
        self.pos[1] += 1
        return self.pos

    def backward(self):
        self.pos[1] -= 1
        return self.pos
