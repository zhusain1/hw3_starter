from collections import namedtuple
import games
import utils

infinity = float('inf')

class Nim(games.Game):

    """ Nim is a two player game where the players are identified as 1
    and 2.  Player 1 is first to move. The state of the game is a
    namedtuple with at least two attributes: to_move (the player whose
    turn it is to move) and board (a Python data structure
    representing how many heaps there are and how many objects are in
    each)."""

    def __init__(self, heaps=[1,1], show_moves=True):
        self.show_moves = show_moves
        self.heaps = heaps
        # put your code here.  At a minimum, it should assign
        # self.initial to a games.GameState namedtuple with four elemants
        # named to_move, board, utility and moves.  See the aima
        # games.py code.
        self.initial = games.GameState(to_move=1, utility=0, board=self.heaps, moves=[])

    def actions(self, state):

        positionOfObjects = []
        objects = []
        for i in range(0, len(state.board)):
            objects.append(state.board[i])
            positionOfObjects.append(i)

        allPositionsAndObjects = []
        for j in range(0, len(state.board)):
            for k in range(1, objects[j] + 1):
                    positions_and_object = (positionOfObjects[j], k)
                    allPositionsAndObjects.append(positions_and_object)
        return allPositionsAndObjects

    def result(self, state,  move):
        """Given a move and a state, returns a representation of the
        new state that results after making the move."""
        # put your code here.  It should return an appropriate
        # GameState namedtuple for the state that results in making
        # the move in the state.
        position = move[0]
        object = move[1]
        if move not in self.actions(state):
            return state
        else:
            board = state.board.copy()
            board[position] = board[position] - object
            return games.GameState(to_move=(2 if state.to_move == 1 else 1),utility=0,board=board, moves=[])



    def terminal_test(self, state):
        """ Returns True iff state is a terminal state, i.e., one in
        which no moves are possible."""
        # put your code here
        for heap in state.board:
            if heap > 0:
                return False

        return True

    def utility(self, state, player):
        """ Given a state, returns a a number representing the state's
        utility w.r.t. player. This could be as simple as +infinity if
        it is a win for the player and -infinity if it is a win for
        the player's opponent and 0 if it is not a terminal state.  A
        better utility function would assign intermediate values for
        non-terminal states."""
        # put your code here

        if self.terminal_test(state):
            if player == state.to_move:
                return infinity
            else:
                return -infinity
        return 0

    def __repr__(self):
        """" returns a string that, if executed, would construnct the initial Nim object for self """
        # put your code here
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """Play an n-person, move-alternating game. This a version of
        the method from the aima-python games.py program that has been
        modified to optionaly print moves made by each player."""
        state = self.initial
        while True:
            for player_num, player in enumerate(players):
                player_num += 1
                move = player(self, state)
                state = self.result(state, move)
                if self.show_moves:
                    print("  Player{} moves {} => {}".format(player_num, move, state.board))
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))

