import requests as requests


def get_player_detail(pid):
    response = requests.get(
        "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='%s'" % pid)
    return response.json()


