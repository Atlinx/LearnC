strcmp 🧵
==============

If you want to check if two strings are equal, you cannot use ``==``. This is because strings are stored as a list of characters, so you must use some function that can go through every character in both strings and check if they are equal.

Lucky for us, this has already been written in the C language. We can use the ``strcmp()`` function to compare two strings alphabetically, by writing:

.. important::

    Functions themselves can also evaluate into a value! If a function does this, then we say the funciton **returns** a value. The return value of a function must always be the same type --- For exmaple if a function returns a float, then it must always return a float.

.. code-block:: c
    
    strcmp(string_1, string_2);

where

    ``string_1`` is the first string
    ``string_2`` is the second string

    This function returns

    - 0 if the two strings are equal
    - -1 if the ``string_1`` comes first alphabetically
    - 1 if the ``string_2`` comes first alphabetically 

The ``strcmp()`` function is actually part of the ``string.h`` library, so in order to use it, you must have ``#enclude <string.h>`` at the top of your program.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Make a program that takes in two words and prints out the word comes first alphabetically. If both words are the same, then print out both words. Assume both words are at most 63 character long.

.. code-block:: c

    #include <stdio.h>

    int main() {
        char word_one[64] = "";
        char word_two[64] = "";

        printf("Enter two space-separated words:\n");
        scanf("%s %s", word_one, word_two);

        int result = strcmp(string_);
    }

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int condition = 1; // Setting this to any non-zero value would mean true.

                if (condition) {
                    printf("True");
                }

                if (!condition) {
                    printf("False");
                }

                return 0;
            }