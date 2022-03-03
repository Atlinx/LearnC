More Printf() 🖨️
======================

The ``printf`` function can do more than just print strings! It can also print strings with numbers, characters, or other strings placed inside of it.

To use printf, you do

    .. code-block:: c

        printf(format_string, value1, value2, ...);
    
    ..

    where

    ``format_string``
        is a string that contains **format specifiers**. Format specfiers are special strings that start with `%` and represent a type.

        A format string is basically a fill-in-the-blank string. The format specfifiers are the "blanks" that must be filled in.

        Here's the most common format specifiers 

        .. list-table::
            :widths: 25 50
            :header-rows: 1

            * - Format specifier
              - Type
            * - `%d`
              - Integer
            * - `%f`
              - Float
            * - `%c`
              - Character
            * - `%s`
              - String

    ``value1, value2, ...``
        are the values, separated by commas, that go with the format specfifiers. The 1st value goes with the 1st format specifier. The 2nd value goes with the 2nd format specifier, and so forth.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        // Prints "My name is Bob."
        printf("My name is %s.", "Bob");
        
        // Prints "I have $100."
        printf("I have $%d.", 100);

        // Prints "The first letter of 'apple' is 'a'."
        printf("The first letter of 'apple' is '%c'.", 'a');

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print "I have 100 apples and 50 bananas" using format specifiers for the numbers 100 and 50.

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("I have %d apples and %d bananas", 100, 50);
            }