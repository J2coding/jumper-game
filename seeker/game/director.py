from game.terminal_service import TerminalService
from game.hider import Hider
from game.seeker import Seeker


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._hider = Hider()
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
        self._run_once = True

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        "        
        """
        while self._run_once:
            for line in self._hider._parachuteMan:# will print jumper line
                print(line)
                    

            # show game info
            hint = self._hider.get_hint()# prints the underscores
            self._terminal_service.write_text(hint)
            

            self._run_once = False

        ans = self._terminal_service.read_number( "\nGuess a letter of a word: ")

        self._seeker.move_location(ans)
    

    def _do_updates(self):
        """ 
        
        Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._hider.watch_seeker(self._seeker)

    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        print()
        # sho every line in jumper
        for line in self._hider._parachuteMan:
            print(line)

        # show game info
        hint = self._hider.get_hint()
        self._terminal_service.write_text(hint)

        # show lives left
        lives = self._hider.get_lives()
        self._terminal_service.write_text(lives)

        if self._hider.is_found():
            self._is_playing = False
