class PlayerBattingStat:
    def __init__(self, pid,name,x_coord,y_coord,game_date,result_type):
        self.result_type = result_type
        self.game_date = game_date
        self.batting_coord = (x_coord,y_coord)
        self.name = name
        self.pid = pid
