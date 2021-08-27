from dependency_injector.wiring import inject

from bba.application.services.player.abstract.abstract_stats_query_service import AbstractPlayerStatsQueryService
from bba.infrastructure.database.repositories.player_stats_repository import PlayerStatsRepository


class PlayerStatsQueryService(AbstractPlayerStatsQueryService):
    @inject
    def __init__(self, player_stats_repository: PlayerStatsRepository):
        self.player_stats_repository = player_stats_repository

    def get_player_stats_by_id(self, pid):
        result = self.player_stats_repository.get_by_id(pid)
        return result



