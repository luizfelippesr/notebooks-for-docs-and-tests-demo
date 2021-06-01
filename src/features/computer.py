import random
import time
import datetime
from . import thingy

class DeepThought:
    """
    Designed to allow better examining the
    "Ultimate Question of Life, the Universe, and Everything" [1]


    .. [1] D. Adams, "The Hitchhiker's Guide to the Galaxy"


    Parameters
    ----------
    questions : list
        Optional list of potential "Ultimate Questions..". If absent, common
        sense will be used.
    """
    def __init__(self, questions=None):
        if questions is None:
            questions = ['What do you get if you multiply six by nine?',
                         "How many roads must a man walk down?",
                         "What is 54 in base 13?"]
        self._questions = questions

    def get_the_answer(self):
        """
        Finds the answer for the "Ultimate Question of Life, the Universe,
        and Everything"!

        Returns
        -------
        question : str
            The Answer!
        """
        time.sleep(2)
        return 42


    def get_the_question(self):
        """
        Finds the  "Ultimate Question of Life, the Universe, and Everything"!

        Returns
        -------
        question : str
            The Question!
        """
        for i in range(2):
            print('This may take some time...')
            print('...')
            time.sleep(10)

        return thingy.something


    def get_a_question(self):
        """
        Finds a (possible) "Ultimate Question of Life, the Universe, and
        Everything"

        Note
        ----
        This may or may not be satisfying... but it is a bit better than
        waiting.

        Returns
        -------
        question : str
            A... question!
        """
        # Not very safe... but for a demo, who cares?
        random.seed(datetime.datetime.now())

        return random.choice(self._questions)
