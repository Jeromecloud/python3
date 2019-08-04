class Game:
    score = 0 
    @staticmethod
    def show_help():
        print("让僵尸走进房间！")
    
    @classmethod
    def show_top_score(cls):
        print("The Top Scoe is %s " % Game.score)

    def __init__(self,player_name):
        self.player_name = player_name
    
    def start_game(self):
        print("%s start game" % self.player_name)
        Game.score = 999

Game.show_help()
Game.show_top_score()

game = Game("jerome")
game.start_game()
Game.show_top_score()