

class Score:
    score = 0
    high_score = 0
    @classmethod
    def increment_score(cls):
        cls.score += 1

    @classmethod
    def reset_score(cls):
        cls.score = 0

    @classmethod
    def get_score(cls):
        return cls.score

    @classmethod
    def set_high_score(cls):
        cls.high_score = cls.score

    @classmethod
    def get_high_score(cls):
        return cls.high_score