from mediatr import Mediator
from dependency_injector.wiring import inject, Provide

from bba.application.services.player.abstract.abstract_stats_query_service import AbstractPlayerStatsQueryService
from containers import Container
from bba.application.services.player.abstract.abstract_player_query_service import AbstractPlayerQueryService


class GetPlayerStatsQuery:
    def __init__(self, pid: int):
        self.pid = pid


@Mediator.handler
class GetPlayerStatsQueryHandler:
    @inject
    def __init__(self, player_stats_query_service: AbstractPlayerStatsQueryService = Provide[Container.player_stats_service]):
        self.player_stats_query_service = player_stats_query_service

    def handle(self, request: GetPlayerStatsQuery):
        result = self.player_stats_query_service.get_player_stats_by_id(int(request.pid))
        return result
