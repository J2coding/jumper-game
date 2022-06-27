import random
from game.seeker import Seeker


class Hider:
    """The person hiding from the Seeker. 

    The responsibility of Hider is to keep track of its location and distance from the seeker. 

    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._word ='QWERTY'
        self._results =[]
        self._points =[]
        self._parachuteMan =[
            " ___",
            "/___\\",
            "\\   /",
            " \\ /",
            "  O",
            " /|\\",
            " /  \\"
            "       ",
            "^^^^^^^",
            " "        ]

        self._lives = 4
        for _ in self._word:
            self._results.append('_')
            self._index_of = 0

            self._location = random.randint(1, 1000)
            self._distance = [0, 0]  

    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.

        Returns:
            string: A hint for the seeker.
        """
        hint = " ".join(self._results)

        return hint

    def get_lives(self):
        lives = f'Lives left: {self._lives}'
        return lives

    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.

        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        returning = False

        if self._lives == 0:
            print("No lives left!")
            returning = True

        # replace results items,
        
        if '_' not in self._results:
            print("you won")
            returning = True
            print(self._results)
            input('play again!')

        return returning

    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        letter = seeker.get_location()
        index_of = 0
        if letter in self._word:
            # getting the index of where is ans located in word
            index_of = self._word.index(letter)
            # print(f'the index is {index_of}')
            # set collected input
            self._results[index_of] = letter
        else:
            # reduce lives
            self._lives = self._lives - 1
            # remove first index in jumper
            self._parachuteMan.pop(0)
            # replace head with x
            if len(self._parachuteMan) == 3:
                self._parachuteMan[0] = "  x"
