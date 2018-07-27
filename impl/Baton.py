class Baton:

    def __init__(self, uid, orient):

        self.direct = 0
        self.uid = uid

        if orient in ['v','h']:
            self.orient = orient
        else:
            raise ValueError()
