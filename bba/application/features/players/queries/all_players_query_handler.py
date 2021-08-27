from mediatr import Mediator
from dependency_injector.wiring import inject, Provide
from containers import Container
from bba.application.services.player.abstract.abstract_player_query_service import AbstractPlayerQueryService


class GetAllPlayersQuery:
    def __init__(self):
        print("All Players Query")


@Mediator.handler
class GetPlayerProfileQueryHandler:
    @inject
    def __init__(self, player_query_service: AbstractPlayerQueryService = Provide[Container.player_service]):
        self.player_query_service = player_query_service

    def handle(self, request: GetAllPlayersQuery):
        result = self.player_query_service.get_all_players()
        return result
