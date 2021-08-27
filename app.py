from flask import Flask, app
from mediatr import Mediator

from bba.application.features.player_stats.queries import player_stats_query_handler
from bba.application.features.players.queries import player_profile_query_handler, all_players_query_handler, \
    player_detail_query_handler
from bba.application.services.player import player_query_service, player_stats_query_service
from blueprints.error_handling import blueprint as error_handling
from containers import Container

from bba.application.features.players.queries.player_profile_query_handler import GetPlayerProfileQueryHandler
from blueprints.players import blueprint as player_endpoints
from blueprints.batting_stats import blueprint as player_stats_endpoints


def create_app() -> Flask:
    container = Container()
    # could have use an external file here
    container.config.from_dict({"db_uri": "mongodb+srv://app-user:WhMk8y0Ono9mVZkh@freecluster.gk6oy.mongodb.net"
                                          "/baseballStatisticDb?retryWrites=true&w=majority"})
    container.wire(modules=[player_profile_query_handler, player_query_service, all_players_query_handler,
                            player_detail_query_handler, player_stats_query_handler, player_stats_query_service])
    app = Flask(__name__)
    app.container = container
    app.register_blueprint(error_handling)
    app.register_blueprint(player_endpoints)
    app.register_blueprint(player_stats_endpoints)
    Mediator.register_handler(GetPlayerProfileQueryHandler)
    return app


if __name__ == '__main__':
    create_app().run()
