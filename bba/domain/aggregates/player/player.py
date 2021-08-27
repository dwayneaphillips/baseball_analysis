class Player:
    def __init__(self,pid,name):
        self.pid =  pid
        self.name = name

    @staticmethod
    def create_player(pid,name):
        return Player(pid,name)