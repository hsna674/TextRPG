from functions import *
from settings import *
from save import *
import professions

class Game:
    def __init__(self) -> None:
        self.data = {}
        self.title_screen()

    def title_screen(self):
        clear_screen()
        print(text2art(text="TextRPG"))
        type_write(f"1. New Game\n2. Continue Game\n3. How to play\n4. Settings\n5. Quit\n\nHow would you like to proceed?")
        self.menu_option = input()
        self.menu_functions = [self.new_game, self.continue_game, self.how_to_play, self.settings, quit]
        self.menu_functions[int(self.menu_option) - 1]()

    def new_game(self):
        """Creates a new game instance"""
        self.save = SaveFiles.new_save(self.data)
        clear_screen()
        type_write(f"Choose a profession\n\n1. Knight\n2. Archer\n3. Mage\n4. Rogue\n5. Cleric\n6. Paladin\n7. Barbarian\n8. Druid\n9. Assassin\n10. Warlock\n\nWhat is your choice: ")
        self.profession = input()
        self.profession_functions = [professions.knight, professions.archer, professions.mage, professions.rogue, professions.cleric, professions.paladin, professions.barbarian, professions.druid, professions.assassin, professions.warlock]
        self.profession_functions[int(self.profession) - 1](self.save)

    def continue_game(self):
        """Loads game data into a new game instance"""
        pass

    def how_to_play(self):
        """Displays a how-to-play screen"""
        pass

    def settings():
        """Displays a settings screen"""
        pass

if __name__ == "__main__":
    game = Game()