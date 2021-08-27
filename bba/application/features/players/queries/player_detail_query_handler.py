from mediatr import Mediator
from dependency_injector.wiring import inject, Provide
from containers import Container
from bba.application.services.player.abstract.abstract_player_query_service import AbstractPlayerQueryService


class GetPlayerDetailQuery:
    def __init__(self, pid: int):
        self.pid = pid


@Mediator.handler
class GetPlayerDetailQueryHandler:
    @inject
    def __init__(self, player_query_service: AbstractPlayerQueryService = Provide[Container.player_service]):
        self.player_query_service = player_query_service

    def handle(self, request: GetPlayerDetailQuery):
        result = self.player_query_service.get_player_detail(int(request.pid))
        return result
