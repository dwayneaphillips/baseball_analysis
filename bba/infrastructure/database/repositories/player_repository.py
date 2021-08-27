from pymongo import MongoClient

from bba.domain.aggregates.player.player import Player
from bba.infrastructure.database.repositories.abstract.abstract_repository import AbstractRepository


class PlayerRepository(AbstractRepository):
    def __init__(self,db_uri):
        self.client = MongoClient(db_uri)

    def get_all(self):
        db = self.client.baseballStatisticDb
        players = db.players.find()
        result = map(lambda player: Player.create_player(player['mlb_id'], player['player_name']).__dict__, players)
        return list(result)

    def get_by_id(self, pid):
        db = self.client.baseballStatisticDb

        player = db.players.find_one({"mlb_id": pid})
        if player is None:
            return {}
        result = Player.create_player(player['mlb_id'], player['player_name']).__dict__
        print(result)
        return result
