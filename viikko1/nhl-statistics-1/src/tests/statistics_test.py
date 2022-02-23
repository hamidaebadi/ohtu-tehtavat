import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_correct_name_finds_player(self):
        player_name = "Kurri"
        result = self.statistics.search(player_name)
        self.assertNotEqual(result, None)

    def test_wrong_name_returns_none(self):
        wrong = "Who"
        result = self.statistics.search(wrong)
        self.assertEqual(result, None)

    def test_players_same_team_is_correct(self):
        team_name = "EDM"
        result = self.statistics.team(team_name)
        self.assertEqual(len(result), 3)

    def test_first_top_scorer_return_correct_data(self):
        result = self.statistics.top_scorers(0)
        self.assertEqual(len(result), 1)
