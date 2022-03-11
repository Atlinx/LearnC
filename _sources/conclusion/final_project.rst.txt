Final Project - Text Adventure Game 🎮
========================================

Now that you know the basics, it's finally time piece everything together! For our final project, we are going to make a text adventure game. 

This is a video game where you a shown text about story and can type a response to make different choices. It's basically a branching narrative that's driven by the users decisions.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Ask the player for their name and store it in a variable. Assume that the player's name can be at most 63 characters long.


.. admonition:: Ex.
    :class: example

    .. code-block:: text

        > Please enter your name:
        > Bob
        > Welcome Bob to the world of Augustine!

..

    .. collapse:: Hint 1 ❓

        You can create a string variable ``n`` characters long using ``char my_variable[n];``. See :doc:`/variables/string_variables` for more info.

    .. collapse:: Hint 2 ❓

        You can get user input using ``scanf(format_string, &variable_1, &variable_2)``. See :doc:`/variables/scanf` for more info.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                // Step 1
                char name[64] = "";

                printf("Please enter your name:\n");
                scanf("%s", name);
                printf("Welcome %s to the world of Augustine!", name);
            }

|check| Ask the user to make a choice by typing in a single-word. After receiving input, using an if statement to make a branching path that prints something different depending on the user's choice.

.. admonition:: Ex.
    :class: example

    .. code-block:: text

        > Welcome Bob to the world of Augustine!
        > You're an outlander who has just arrived to a small habor city on the east of Augustine. 
          As you get off the boat, you get a whiff of the air --- you can almost taste the salty 
          sea mixed with the sweetness of local delicacies. You scan the boardwalk and 
          see a bar, a hotel, and a shop.
        > - Type 'shop' to enter the shop.
        > - Type 'hotel' to enter the hotel.
        > - Type 'bar' to enter the bar.
        > shop
        > You enter a shop to buy some goods. The prices are so low, what a steal! 
          Unfortunately you were careless and spent all your money. You're now broke...


    .. code-block:: text

        > Welcome Bob to the world of Augustine!
        > You're an outlander who has just arrived to a small habor city on the east of Augustine. 
          As you get off the boat, you get a whiff of the air --- you can almost taste the salty 
          sea mixed with the sweetness of local delicacies. You scan the boardwalk and 
          see a bar, a hotel, and a shop.
        > - Type 'shop' to enter the shop.
        > - Type 'hotel' to enter the hotel.
        > - Type 'bar' to enter the bar.
        > bar
        > You enter the bar and you find some old friends sitting at a table in the corner.

..

    .. collapse:: Hint 1 ❓

        You can compare two strings using the ``strcmp()`` function. Make sure you have ``#include <string.h>`` at the top of your program when you use it! See :doc:`/conditionals/strcmp` for more info.


    .. collapse:: Hint 2 ❓

        You may want to use escape sequences to add in newlines or tabs to make your text more readable. See :doc:`/hello_world/escape_sequences` for more information.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>
            #include <string.h>

            int main() {
                // Step 1
                char name[64] = "";

                printf("Please enter your name:\n");
                scanf("%s", name);
                printf("Welcome %s to the world of Augustine!\n\n", name);
                
                // Step 2
                printf("You're an outlander who has just arrived to a small habor city on the east of Augustine. As you get off the boat, you get a whiff of the air --- you can almost taste the salty sea mixed with the sweetness of local delicacies. You scan the boardwalk and see a bar, a hotel, and a shop.\n");
                printf("\t - Type 'shop' to enter the shop.\n");
                printf("\t - Type 'hotel' to enter the hotel.\n");
                printf("\t - Type 'bar' to enter the bar.\n");
                
                char choice[64] = "";
                scanf("%s", choice);
                
                if (strcmp(choice, "shop") == 0) {
                    printf("You enter a shop to buy some goods. The prices are so low, what a steal! Unfortunately you were careless and spent all your money. You're now broke...\n");
                } else if (strcmp(choice, "hotel") == 0) {
                    printf("You rent a room in the hotel and you sleep in for the entire day. How relaxing...\n");
                } else if (strcmp(choice, "bar") == 0) {
                    printf("You enter the bar and you find some old friends sitting at a tab\n");
                }
            }

|check| At the end of one of your paths, write your next branching path.

.. admonition:: Ex.
    :class: example

    .. code-block:: text
    
        > You enter the bar and you find some old friends sitting at a table in the corner.
        > "Hey Bob, I haven't seen you in ages!" cried Blake.
        > Why not have a round of drinks with us?
        > - Type 'yes' to have a round
        > - Type 'no' to abstain
        > yes
        > You drink with your friends for the rest of the day and wake up at the hotel the 
          next day with a headache. You don't remember what happened the night beefore...
..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>
            #include <string.h>

            int main() {
                // Step 1
                char name[64] = "";

                printf("Please enter your name:\n");
                scanf("%s", name);
                printf("Welcome %s to the world of Augustine!\n\n", name);
                
                // Step 2
                printf("You're an outlander who has just arrived to a small habor city on the east of Augustine. As you get off the boat, you get a whiff of the air --- you can almost taste the salty sea mixed with the sweetness of local delicacies. You scan the boardwalk and see a bar, a hotel, and a shop.\n");
                printf("\t - Type 'shop' to enter the shop.\n");
                printf("\t - Type 'hotel' to enter the hotel.\n");
                printf("\t - Type 'bar' to enter the bar.\n");
                
                char choice[64] = "";
                scanf("%s", choice);
                
                if (strcmp(choice, "shop") == 0) {
                    printf("You enter a shop to buy some goods. The prices are so low, what a steal! Unfortunately you were careless and spent all your money. You're now broke...\n");
                } else if (strcmp(choice, "hotel") == 0) {
                    printf("You rent a room in the hotel and you sleep in for the entire day. How relaxing...\n");
                } else if (strcmp(choice, "bar") == 0) {
                    printf("You enter the bar and you find some old friends sitting at a table in the corner.\n");
                    
                    // Step 3
                    printf("\"Hey %s, I haven't seen you in ages!\" cried Blake.\n", &name);
                    printf("Why not have a round of drinks with us?\n");
                    printf("\t - Type 'yes' to have a round\n");
                    printf("\t - Type 'no' to abstain\n");
                    
                    scanf("%s", choice);
                    
                    if (strcmp(choice, "yes") == 0) {
                        printf("You drink with your friends for the rest of the day and wake up at the hotel the next day with a headache. You don't remember what happened the night beefore...");
                    } else if (strcmp(choice, "no") == 0) {
                        printf("You decide to buy a round for your friends and have a glass of juice for yourself. After spending some time talking, you bid farwell and leave the bar...\n");
                    }
                }
            }


|check| Print "THE END" at the end of all your paths.

.. admonition:: Ex.
    :class: example

    .. code-block:: text
    
        > You enter a shop to buy some goods. The prices are so low, what a steal! 
          Unfortunately you were careless and spent all your money. You're now broke...
        > THE END

    .. code-block:: text
    
        > You drink with your friends for the rest of the day and wake up at the hotel the 
          next day with a headache. You don't remember what happened the night beefore...
        > THE END

..

    .. collapse:: Solution ✅

        .. code-block:: c
        
            #include <stdio.h>
            #include <string.h>

            int main() {
                // Step 1
                char name[64] = "";

                printf("Please enter your name:\n");
                scanf("%s", name);
                printf("Welcome %s to the world of Augustine!\n\n", name);
                
                // Step 2
                printf("You're an outlander who has just arrived to a small habor city on the east of Augustine. As you get off the boat, you get a whiff of the air --- you can almost taste the salty sea mixed with the sweetness of local delicacies. You scan the boardwalk and see a bar, a hotel, and a shop.\n");
                printf("\t - Type 'shop' to enter the shop.\n");
                printf("\t - Type 'hotel' to enter the hotel.\n");
                printf("\t - Type 'bar' to enter the bar.\n");
                
                char choice[64] = "";
                scanf("%s", choice);
                
                if (strcmp(choice, "shop") == 0) {
                    printf("You enter a shop to buy some goods. The prices are so low, what a steal! Unfortunately you were careless and spent all your money. You're now broke...\n");
                    
                    // Step 4
                    printf("\nTHE END\n");
                } else if (strcmp(choice, "hotel") == 0) {
                    printf("You rent a room in the hotel and you sleep in for the entire day. How relaxing...\n");

                    // Step 4
                    printf("\nTHE END\n");
                } else if (strcmp(choice, "bar") == 0) {
                    printf("You enter the bar and you find some old friends sitting at a table in the corner.\n");
                    
                    // Step 3
                    printf("\"Hey %s, I haven't seen you in ages!\" cried Blake.\n", &name);
                    printf("Why not have a round of drinks with us?\n");
                    printf("\t - Type 'yes' to have a round\n");
                    printf("\t - Type 'no' to abstain\n");
                    
                    scanf("%s", choice);
                    
                    if (strcmp(choice, "yes") == 0) {
                        printf("You drink with your friends for the rest of the day and wake up at the hotel the next day with a headache. You don't remember what happened the night beefore...");

                        // Step 4
                        printf("\nTHE END\n");
                    } else if (strcmp(choice, "no") == 0) {
                        printf("You decide to buy a round for your friends and have a glass of juice for yourself. After spending some time talking, you bid farwell and leave the bar...\n");

                        // Step 4
                        printf("\nTHE END\n");
                    }
                }
            }

|check| Celebrate because you've just completed a text adventure game in C! 🥳