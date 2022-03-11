Else Statement ❔
=================

What if you wanted to also check if the condition wasn't satisfied in an if statement? You may assume we would have to write out two if statements, like:

.. code-block:: c

    int condition = 0;

    if (condition) {
        
    }

    if (!condition) {
        
    }

However you can actual use the else statement instead:

.. code-block:: c

    int condition = 0;

    if (condition) {
        
    } else {
        
    }

You can also chain together ``else if`` to check for multiple conditions in one if statement chain.

.. code-block:: c

    int condition = 0;
    int other_condition = 1;
    int another_condition = 0;

    if (condition) {
        
    } else if (other_condition) {
        
    } else if (another_condition) {
        
    }

Note that you can only add the else at the very end of an if statement chain.

.. code-block:: c

    int condition = 0;
    int other_condition = 1;

    if (condition) {
        
    } else if (other_condition) {
        
    } else {

    }

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Write a program that asks a person for their favorite number. 

- If the number is greater than 0, print "Your number is positive!". 
- If the number is less than 0, print "Your number is negative!". 
- If the number is equal to zero, print "Your number is neither positive nor negative, so it must be zero then!".

    .. collapse:: Solution ✅

        .. code-block:: c
        
            #include <stdio.h>

            int main() {
                int favorite_number = 0;
                printf("What is your favorite number?\n");
                scanf("%d", &favorite_number);
                if (favorite_number > 0) {
                    printf("Your number is positive!\n");
                } else if (favorite_number < 0) {
                    printf("Your number is negative!\n");
                } else {
                    printf("Your number is neither positive nor negative, so it must be zero then!\n");
                }
                return 0;
            }
