# Define the Player class
class Player:
    def play(self):
        print("The player is playing cricket")

# Define the Batsman class that inherits from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting")

# Define the Bowler class that inherits from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Create objects of the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()