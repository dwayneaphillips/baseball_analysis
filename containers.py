from dependency_injector import containers, providers


from bba.application.services.player.player_query_service import PlayerQueryService
from bba.application.services.player.player_stats_query_service import PlayerStatsQueryService
from bba.infrastructure.database.repositories.player_repository import PlayerRepository
from bba.infrastructure.database.repositories.player_stats_repository import PlayerStatsRepository


class  Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    player_repository = providers.Factory(PlayerRepository,
                                          db_uri=config.db_uri)
    player_stats_repository = providers.Factory(PlayerStatsRepository,
                                                db_uri=config.db_uri)

    player_service = providers.Factory(PlayerQueryService, player_repository=player_repository)
    player_stats_service = providers.Factory(PlayerStatsQueryService, player_stats_repository=player_stats_repository)

