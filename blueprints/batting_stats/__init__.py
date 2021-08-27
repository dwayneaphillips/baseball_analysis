from flask import Blueprint, request, jsonify
from mediatr import Mediator

from bba.application.features.player_stats.queries.player_stats_query_handler import GetPlayerStatsQuery

blueprint = Blueprint('player_stats_api', __name__, url_prefix='/players/stats')


@blueprint.route('/batting/<int:pid>', methods=['GET'])
def player_profile(pid):
    if request.method == "GET":
        stats_request = GetPlayerStatsQuery(pid)
        mediator = Mediator()
        result = mediator.send(stats_request)
        if result == {}:
            return 'No Data Found', 204

        return jsonify(result)
