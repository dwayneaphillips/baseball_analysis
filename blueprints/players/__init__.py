from flask import Blueprint, request, jsonify, abort
from mediatr import Mediator

from bba.application.features.players.queries.all_players_query_handler import GetAllPlayersQuery
from bba.application.features.players.queries.player_detail_query_handler import GetPlayerDetailQuery
from bba.application.features.players.queries.player_profile_query_handler import GetPlayerProfileQuery

blueprint = Blueprint('player_api', __name__, url_prefix='/players')


@blueprint.route('/<int:pid>', methods=['GET'])
def player_profile(pid):
    if request.method == "GET":
        profile_request = GetPlayerProfileQuery(pid)
        mediator = Mediator()
        result = mediator.send(profile_request)
        if result == {}:
            return 'No Data Found', 204

        return jsonify(result)


@blueprint.route('/', methods=['GET'])
def all_players():
    if request.method == "GET":
        profile_request = GetAllPlayersQuery()
        mediator = Mediator()
        result = mediator.send(profile_request)
        return jsonify(result)


@blueprint.route('/detail/<int:pid>', methods=['GET'])
def player_detail(pid):
    if request.method == "GET":
        profile_request = GetPlayerDetailQuery(pid)
        mediator = Mediator()
        result = mediator.send(profile_request)
        return jsonify(result)
