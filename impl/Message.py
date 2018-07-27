class Message:

    # uid is integer unique identifier
    # content is the message to be delivered
    # orient is 'v' for vertical or 'h' for horizontal
    # direct is +1 or -1 (up/right or left/down), 0 for stationary
    def __init__(self, uid, orient, direct, content):
        self.uid = uid
        self.orient = orient
        self.direct = direct
        self.content = content
        self.cornered = False


    def switchOrient(self):
        if self.orient == 'h': self.orient = 'v'
        elif self.orient == 'v': self.orient = 'h'
        else: raise AssertionError()
