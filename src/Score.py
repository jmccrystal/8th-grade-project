
class Score:
    score = 0
    @classmethod
    def increment_score(cls):
        cls.score += 1

    @classmethod
    def reset_score(cls):
        cls.score = 0

    @classmethod
    def get_score(cls):
        return cls.score