from pymongo import MongoClient

from bba.domain.aggregates.player.batting_statistic import PlayerBattingStat
from bba.infrastructure.database.repositories.abstract.abstract_repository import AbstractRepository


class PlayerStatsRepository(AbstractRepository):
    def __init__(self,db_uri):
        self.client = MongoClient(db_uri)

    def get_all(self):
            pass

    def get_by_id(self, pid):
        db = self.client.baseballStatisticDb
        stats = db.player_batting_stats.find({"$and": [{"batter": pid},{"hc_x":{"$exists":True}}]})
        if stats is None:
            return {}
        result = map(lambda stat: PlayerBattingStat(stat['batter'], stat['player_name'],stat['hc_x'],stat['hc_y'],stat['game_date'],stat['type']).__dict__, stats)
        return list(result)







