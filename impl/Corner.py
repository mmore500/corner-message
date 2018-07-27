class Corner:

    def __init__(self, uid):
        self.uid = uid
        self.direct = {'h' : 0, 'v' : 0}

    # in_direct is +1 for up/right, -1 for down/left, 0 for stationary
    def checkMessage(self, message, tile):

        # l r u d are move notifications
        if message.content == 'l':
            if message.orient == 'v': tile.moveCorner(self.uid, 'h', -1)
            return True
        elif message.content == 'r':
            if message.orient == 'v':  tile.moveCorner(self.uid, 'h', +1)
            return True
        elif message.content == 'u':
            if message.orient == 'h': tile.moveCorner(self.uid, 'v', +1)
            return True
        elif message.content == 'd':
            if message.orient == 'h': tile.moveCorner(self.uid, 'v', -1)
            return True

        return False
