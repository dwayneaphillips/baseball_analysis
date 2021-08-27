from dependency_injector.wiring import inject

from bba.application.services.player.abstract.abstract_player_query_service import AbstractPlayerQueryService
from bba.core import mlb_player_bio_service as mlb_service
from bba.infrastructure.database.repositories.player_repository import PlayerRepository


class PlayerQueryService(AbstractPlayerQueryService):

    @inject
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def get_all_players(self):
        result = self.player_repository.get_all()
        return result

    def get_player_by_id(self, pid):
        result = self.player_repository.get_by_id(pid)
        return result

    def get_player_detail(self,pid):
        result = mlb_service.get_player_detail(pid)
        return result