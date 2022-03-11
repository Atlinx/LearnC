Project 6 - RPS ✂️
====================================

Lets make a game of rock paper scissors for two players.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Ask and store the first player's choice. Assume their choice is a single word no longer than 15 characters.

.. code-block:: bash

    > Player 1 enter "rock", "paper", or "scissors":
    > rock

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                char player_one_choice[16] = "";

                printf("Player 1 enter \"rock\", \"paper\", or \"scissors\":\n");
                scanf("%s", player_one_choice);
                
                return 0;
            }

|check| Ask and store the second player's choice. Assume their choice is a single word no longer than 15 characters.

.. code-block:: bash

    > Player 1 enter "rock", "paper", or "scissors":
    > rock
    > Player 2 enter "rock", "paper", or "scissors":
    > scissors

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                char player_one_choice[16] = "";

                printf("Player 1 enter \"rock\", \"paper\", or \"scissors\":\n");
                scanf("%s", player_one_choice);

                
                char player_two_choice[16] = "";

                printf("Player 2 enter \"rock\", \"paper\", or \"scissors\":\n");
                scanf("%s", player_two_choice);
                
                return 0;
            }

|check| Using if statements, print "Tie" if there is a tie, otherwise print who won.

.. code-block:: bash

    > Player 1 enter "rock", "paper", or "scissors":
    > rock
    > Player 2 enter "rock", "paper", or "scissors":
    > rock
    > Tie


.. code-block:: bash

    > Player 1 enter "rock", "paper", or "scissors":
    > rock
    > Player 2 enter "rock", "paper", or "scissors":
    > scissors
    > Player 1 wins!

.. code-block:: bash

    > Player 1 enter "rock", "paper", or "scissors":
    > rock
    > Player 2 enter "rock", "paper", or "scissors":
    > paper
    > Player 2 wins!

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>
            #include <string.h>

            int main() {
                char player_one_choice[16] = "";

                printf("Player 1 enter \"rock\", \"paper\", or \"scissors\":\n");
                scanf("%s", player_one_choice);

                
                char player_two_choice[16] = "";

                printf("Player 2 enter \"rock\", \"paper\", or \"scissors\":\n");
                scanf("%s", player_two_choice);

                if (strcmp(player_one_choice, player_two_choice) == 0) {
                    printf("Tie\n");
                } else if ((strcmp(player_one_choice, "rock") == 0 && strcmp(player_two_choice, "scissors") == 0) ||
                    (strcmp(player_one_choice, "scissors") == 0 && strcmp(player_two_choice, "paper") == 0) ||
                    (strcmp(player_one_choice, "paper") == 0 && strcmp(player_two_choice, "rock") == 0)
                ) {
                    printf("Player 1 wins!\n");
                } else {
                    printf("Player 2 wins!\n");
                }
                
                return 0;
            }