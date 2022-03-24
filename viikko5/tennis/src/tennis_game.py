import point_const as POINT_TBL
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.__equal_points_tbl = {POINT_TBL.ZERO: "Love-All",
        POINT_TBL.ONE: "Fifteen-All",
        POINT_TBL.TWO: "Thirty-All",
        POINT_TBL.THREE:"Forty-All"}

        self.__general_point_tbl = {
            POINT_TBL.ZERO: "Love",
            POINT_TBL.ONE: "Fifteen",
            POINT_TBL.TWO: "Thirty",
            POINT_TBL.THREE: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
           return self.equal_points(self.m_score1)
           
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(POINT_TBL.ONE, POINT_TBL.THREE):
                if i == POINT_TBL.ONE:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == POINT_TBL.ZERO:
                    score = score + self.__general_point_tbl.get(POINT_TBL.ZERO)
                elif temp_score == POINT_TBL.ONE:
                    score = score + self.__general_point_tbl.get(POINT_TBL.ONE)
                elif temp_score == POINT_TBL.TWO:
                    score = score + self.__general_point_tbl.get(POINT_TBL.TWO)
                elif temp_score == POINT_TBL.THREE:
                    score = score + self.__general_point_tbl.get(POINT_TBL.THREE)

        return score

    def equal_points(self, player1_score):
        if player1_score == POINT_TBL.ZERO:
            score = self.__equal_points_tbl.get(POINT_TBL.ZERO)
        elif player1_score == POINT_TBL.ONE:
            score = self.__equal_points_tbl.get(POINT_TBL.ONE)
        elif player1_score == POINT_TBL.TWO:
            score = self.__equal_points_tbl.get(POINT_TBL.TWO)
        elif player1_score == POINT_TBL.THREE:
            score = self.__equal_points_tbl.get(POINT_TBL.THREE)
        else:
            score = "Deuce"

        return score