import sys
import random
from enum import Enum

def rps(name='Edna'):

    game_count = 0
    player_wins = 0
    comp_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal comp_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        # playerchoice = ("Enter... \n 1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
        playerchoice = input(f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: ")
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n {name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        

        computerchoice = random.choice("123")    
        computer = int(computerchoice)

        
        print(f"\n{name}You chose  {str(RPS(player)).replace('RPS.', '')}."  )
        print(f"comp chose  {str(RPS(computer)).replace('RPS.', '')}.")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal comp_wins

            if player == 1 and computer ==3:
                player_wins += 1
                return f"{name}🎉 you win"
                
            elif player == 2 and computer ==1:
                player_wins += 1
                return f"{name}🎉 you win"    

            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}🎉 you win"
            elif player == computer:
                return"😊 tie game"   

            else:
                comp_wins += 1
                return f"💻 comp win\nSorry, {name}..😥"
            

        game_result = decide_winner(player, computer) 
        print(game_result)   



        nonlocal game_count
        game_count += 1
        print(f"\n Game count:  {game_count}")    
        print(f"\n {name}'s wins: {player_wins}")    
        print(f"\n Player wins: {comp_wins}")    

        print(f"\n Play again, {name}")

        while True:

            playagain = input("\nY for Yes or \nQ to Quit \n") 
        
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else: 
            print("\n🎉🎉🎉")     
            print("Thank you for playing\n")
            if __name__ == "__main__":
                
                sys.exit(f"Bye {name} 👋") 
            else: 
                return    

    return play_rps
      

if __name__ == "__main__":
    import argparse

    parser =  argparse.ArgumentParser(
        description= "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the persion playing the game."
    )
    

    args = parser.parse_args()

    rock_paper_scissors = rps()  
    rock_paper_scissors()        