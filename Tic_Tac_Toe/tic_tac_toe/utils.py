
## HELPER FUNCTIONS LIKE 'REPLAY()', 'CLEAR_OUTPUT()'M ETC.

from time import sleep
import os

#Clears screen
def clear_screen():
    sleep(0.5) # Pauses for half a second for better UX
    os.system('cls' if os.name == 'nt' else 'clear')

#Replays game
def replay():
    return input('Play again? (Yes/No): ').lower().startswith('y')
