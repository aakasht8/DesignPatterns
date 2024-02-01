"""
Implementing the Singleton design pattern in Python
This pattern is used when we want to instantiate a class only once during the whole program execution
Ex: Leaderboard, DBConnection, LogsConnection
"""


class Game:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.scores = []
        return cls._instance

    def __init__(self, name):
        self.name = name

    def add_score(self, name, score):
        self.scores.append({'name': name, 'score': score})

    def print_leaderboard(self):
        if self.scores:
            sorted_scores = list(sorted(self.scores, key=lambda x: x['score'], reverse=True))
            for val in sorted_scores:
                print(f"{val['name']} scored {val['score']}")
        else:
            print('No games played yet')


def main():
    g1 = Game('Aakash')
    g1.add_score('Aakash', 30)

    g2 = Game('Sarthak')
    g2.add_score('Sarthak', 40)

    g3 = Game('Amol')
    g3.add_score('Amol', 50)

    print(id(g1))
    print(id(g2))
    print(id(g3))

    print(g1.scores)
    print(g2.scores)
    print(g3.scores)

    g3.print_leaderboard()


if __name__ == '__main__':
    print('Implementing the Singleton design pattern in Python')
    main()
