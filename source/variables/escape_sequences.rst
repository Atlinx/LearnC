Escape Sequences 🪜
====================

Escape sequences are a special sequence of characters beginning with `\` that represent a single character. They are often used to write out untypeable characters, such as new lines, tabs, or double-quotation marks inside of a string.

Here's a list of common escape sequences:

.. list-table::
    :widths: 10 20 50

    * - Escape Sequence
      - Inserted Character
      - Description
    * - ``\n``
      - Inserts a newline.
      - This escape sequence is needed because you can't just hit enter to get a newline --- that would break C's syntax. 
    * - ``\t``
      - Inserts a tab.
      - This escape sequence is needed because often you can't just hit tab to get a tab character --- that would break C's syntax. 
    * - ``\%``
      - Inserts a ``%`` character. 
      - This escape sequence is needed when writing format strings, because format specifiers start with `%`. (ie. ``%d``, ``%s``)
    * - ``\'``
      - Inserts a ``'`` (single-quote).
      - This escape sequence is needed when writing the single-quote character, as characters are surrounded by single-quotes. (ie. 'a', 'b', '\\'')
    * - ``\"``
      - Inserts a ``"`` (double-quote).
      - This escape sequence is needed when using double-quotes inside of a string, because strings are surrounded by double-quotes. (ie. "This is an \\"apple\\".");
    * - ``\\``
      - Inserts a ``\`` (backslash).
      - This sequence is needed because the start of every escape sequence is a backslash.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        // Escape characters are needed here because double quotes are 
        // already used to denote the start and end of a string.
        printf("My name is \"Bob\"");

        // Add a tab between "I am" and " spaced out!"
        printf("I am \t spaced out!");

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Add a tab between "apple" and "banana" in print statement for the code below.

You should get the output:

.. code-block:: bash

    apple   banana

.. code-block:: c

    #include <stdio.h>

    int main() {
        printf("apple banana");
    }

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("apples\tbananas");
            }

|check| Add a newline between the two sentences that are printed in code below.

You should get the output:

.. code-block:: bash

    Hello there!
    The weather's looking fine today.

.. code-block:: c

    #include <stdio.h>

    int main() {
        printf("Hello there! The weather's looking fine today.");
    }

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("Hello there!\nThe weather's looking fine today.");
            }