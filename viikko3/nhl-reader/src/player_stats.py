from player import Player
class PlayerStats:
    def __init__(self, playerReader):
        self.__player_reader = playerReader
        self.__sorted_player_obj = []
    def top_scorers_by_nationality(self, nationality):
        self.__sort_by_most_points()
        #sort by nationality
        sortedList = filter(lambda p: p.nationality == nationality, self.__sorted_player_obj)
        return sortedList
        

    def __sort_by_most_points(self):
        players_obj_list = self.__player_reader.get_players()
        unsorted_player_tuples = [
            (player.name, player.team, player.assists, player.goals, player.nationality) for player in players_obj_list]
        sorted_player_tuples = sorted(unsorted_player_tuples, key=lambda p: p[2] + p[3], reverse=True)
        for player_tuple in sorted_player_tuples:
            player = Player(player_tuple[0], player_tuple[1], player_tuple[2], player_tuple[3], player_tuple[4])
            self.__sorted_player_obj.append(player)