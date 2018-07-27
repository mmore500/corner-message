from impl.Baton import Baton
from impl.Corner import Corner
from impl.Message import Message

class Tile:

    def __init__(self):
        self.corners = {}
        self.neighbors = {'v' : {}, 'h' : {}}
        self.messages = []
        self.batons = {'v': {}, 'h' : {}}

        self.neighbors['v'][0] = self
        self.neighbors['h'][0] = self

    def link(self, other, orient, direct):
        self.neighbors[orient][direct] = other

    def takeCorner(self, corner):
        self.corners[corner.uid] = corner

    def moveCorner(self, uid, orient, direct):

        for char in self.batons:
            if uid in self.batons[char]:
                self.batons[char][uid].direct = direct
        self.neighbors[orient][direct].takeCorner(self.corners.pop(uid))

    def takeMessage(self, message):

        if message.uid in self.batons['v'] or message.uid in self.batons['h']:
            if message.cornered:
                print("message received: " + str(message.content))
                return

        if message.uid in self.corners:
            # move corner if need be
            res = self.corners[message.uid].checkMessage(message, self)
            # if message was just to move corner, don't need to store
            if res: return
            else: message.cornered = True

            # redirect message
            message.switchOrient()
            message.direct = self.corners[message.uid].direct[message.orient]

        self.messages.append(message)


    def trySendMessage(self):
        if self.messages:
            m = self.messages.pop()
            self.neighbors[m.orient][m.direct].takeMessage(m)
            return True
        else:
            return False


    def takeBaton(self, baton):
        self.batons[baton.orient][baton.uid] = baton

        if baton.uid in self.corners:
            baton.direct = 0
            self.corners[baton.uid].direct[baton.orient] = 0


    def makeMessage(self, uid, baton_orient, content):
            self.takeMessage(
                Message(uid,
                baton_orient,
                self.batons[baton_orient][uid].direct,
                content)
            )


    def moveBaton(self, uid, baton_orient, orient, direct):

        code = 'u' if orient == 'v' and direct == 1 else 'd' if orient == 'v' and direct == -1 else 'l' if orient == 'h' and direct == -1 else 'r' if orient == 'h' and direct == 1 else None

        if code is None: raise ValueError()

        # send move corner command
        self.makeMessage(uid, baton_orient, code)

        if uid in self.corners:
            self.corners[uid].direct[baton_orient] = direct
            self.batons[baton_orient][uid].direct = -direct

        self.neighbors[orient][direct].takeBaton(
                self.batons[baton_orient].pop(uid)
            )

    def makeSet(self, uid):
        self.batons['v'][uid] = Baton(uid, 'v')
        self.batons['h'][uid] = Baton(uid, 'h')
        self.corners[uid] = Corner(uid)


    def __repr__(self):
        res = ''
        if self.messages: res += 'm'
        if self.corners: res += 'c'
        if self.batons['h']: res += 'h'
        if self.batons['v']: res += 'v'
        return res.ljust(4)
