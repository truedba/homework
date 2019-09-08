#!/usr/local/bin/python3


class Warrior:

    MAX_LEVEL = 100
    MAX_EXPERIENCE = 10000
    achievements = []
    RANK = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite',
            'Conqueror', 'Champion', 'Master', 'Greatest']

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = 'Pushover'

    def battle(self, opponent_level):
        if self.level < 1 or self.experience <100:
            output = "Invalid level"
        elif self.level == opponent_level:
            self.experience = min((self.experience + 10), self.MAX_EXPERIENCE)
            output = "A good fight"
        elif 2 >= self.level - opponent_level >= 1:
            self.experience = min((self.experience + 5), self.MAX_EXPERIENCE)
            output = "A good fight"
        elif self.level - opponent_level > 2:
            output = "Easy fight"
        elif 5 > opponent_level - self.level >= 1:
            self.experience = min((self.experience * 20 * (opponent_level - self.level) ** 2), self.MAX_EXPERIENCE)
            output = "An intense fight"
        elif opponent_level - self.level >= 5:
            output = "An intense fight" + "You've been defeated"
        self.level = self.experience // 100
        self.rank = self.RANK[self.level // 10]
        return output

    def training(self, training_name, achieved_experience, required_level):
        if self.level >= required_level:
            self.experience = min((self.experience + achieved_experience), self.MAX_EXPERIENCE)
            self.achievements.append(training_name)
            output = self.achievements
        else:
            output = "Not strong enough"
        self.level = self.experience // 100
        self.rank = self.RANK[self.level // 10]
        return  output

if __name__ == '__main__':

    bruce_lee = Warrior()
    print(bruce_lee.level)  # => 1
    print(bruce_lee.experience)  # => 100
    print(bruce_lee.rank)  # => "Pushover"
    print(bruce_lee.achievements)  # => []
    print(bruce_lee.training("Defeated Chuck Norris", 9000, 1))  # => "Defeated Chuck Norris"
    print(bruce_lee.experience ) # => 9100
    print(bruce_lee.level ) # => 91
    print(bruce_lee.rank ) # => "Master"
    print(bruce_lee.battle(90) ) # => "A good fight"
    print(bruce_lee.experience ) # => 9105
    print(bruce_lee.achievements ) # =
