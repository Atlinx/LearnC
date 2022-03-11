Printf() 🖨️
===============

``printf()`` is a function that can output or **print** text. A **function** is a piece of code that runs a set of code to do something.

.. note::
    Functions will be covered in-depth in a later chapter.

To use this function, you have to write ``printf()`` with a string inside of the parentheses.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        printf("print me!");
        printf("some string");
        printf("a really really really long string");

.. admonition:: Recall
    :class: recall

    A string is some text surrounded by double-quotes. See :doc:`/hello_world/strings` for more details.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print the following text to the output: 

.. code-block:: bash
        
    My name is Bob!

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("My name is Bob!");
                return 0;
            }

|check| Print the same text as before to the output except use a print statement for each word:

.. code-block:: bash
    
    My name is Bob!

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("My ");
                printf("name ");
                printf("is ");
                printf("Bob! ");
                return 0;
            }
