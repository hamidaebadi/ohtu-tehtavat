import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.__url = url
        self.__players = []

    def get_players(self):
        response = requests.get(self.__url).json()
        for player_dic in response:
            player = Player(player_dic['name'], player_dic['team'], player_dic['assists'], player_dic['goals'], player_dic['nationality'])
            self.__players.append(player)
        return self.__players