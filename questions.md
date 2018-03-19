## 1. Minimax and Alphabeta

1.1 For the [first game tree on the HW3 page](mm0.png), use the minimax algorithm to compute a value for each non-leaf node. Squares represent max nodes and circles represent min nodes. Indicate which move the maximizing player should make.

*we'll descirbe how you can hand this in later*

1.2 Simulate the alpha-beta algorithm on the [second game tree on the HW3 page](mm1.png), crossing out the nodes that are pruned. For each non-leaf node that is not pruned, show the exact value (e.g., =3) or the last constraint (e.g., <= 2, >=8) that the alpha-beta algorithm determines.

*we'll descirbe how you can hand this in later*

## 2. Game characteristics

For each of the following statements, say whether it is true or false and provide a short (e.g. one paragraph) justification for your answer.

2.1 Given a two-player, turn-taking, zero-sum, fully observable game between two perfectly rational players, it does not help the first player's outcome to know what strategy the second player is using -- that is, what move the second player will make, given the first player's move.

False
In a fully observable game knowing the opponent's strategy helps. When a players knows all the possible states and the current state of the game,then if the opponents strategy is known a player can better traverse the game-state tree to make their best move, and obtain maximal payoff. When the opponent's strategy is unknown the player could end up making suboptimal moves.


2.2 Given a two-player, turn-taking, zero-sum, partially observable game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move.

False
In a partially observable game, the Monte Carlo method maximizes the payoff for a player. This method is not complete and does encounter deviations of the opponents from the strategies that were found, although numerous runs are made. If the strategy of the opponent was found correctly it would help us improve an agent's performance in partially observable zero-sum games.

2.3 A perfectly rational backgammon-playing agent with unlimited resources never loses.

False
Given unlimited resources, the backgammon agent has the ability to compute the entire game-state tree inclusive of all of the chance nodes for all dice rolls made the current player and the opponent. However, this does not guarantee victory for the agent. Due to the game depending on chance of the roll on the dice. The agent cannot guarantee maximial it's payoff since the dice roll is out of the agents hands.



## 3. Answer the following questions for our the game of Nim.

3.1 For a Nim game with initial configuration [5,4,3], what is the shortest possible game in terms of plys?

The shortest game would be a game of 3 moves consistiing of the first player taking all objects, from a pile, and the second player taking all, thus yielding a game with removal of 5, 4, and 3 or a different sequennce of taking all objects.

3.2 For a Nim game with initial configuration [5,4,3], what is the longest possible game in terms of plys?

The longest game would be if a player and their opponent take only one object from each heap therefore, the number of moves would increase significantly to 12 moves.

3.3 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the shortest possible game in terms of plys?

The shortest game is taking all objects from a pile at one time as a move, thus making the shortest game equal to Hi.

3.4 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the longest possible game in terms of plys?

The longest game is equal to the sum of every Hi value from an intial configuration, because a player will remove only one object at a time.

