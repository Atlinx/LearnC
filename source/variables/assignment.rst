Assignment ➡️
==============

Variables can be be given or **assigned** a value, by doing

    .. code-block:: c

        var_name = value;

    ..

    where,

    ``var_name`` is the name of the variable,

    ``value`` is the value you are assigning to the variable.

This overwrites the existing value of a variable.

The assigned value has to be of the same type as the variable.

.. admonition:: Good
    :class: good

    .. code-block:: c

        int some_int_var;
        float some_float_var;
        char some_char_var;
        char* some_string_var;

        some_int_var = 10;
        some_float_var = 0.5;
        some_char_var = 'a';
        some_string_var = "hello there!";

.. admonition:: Bad
    :class: bad

    .. code-block:: c
    
        int some_int_var;
        char some_char_var;

        // Integer variables can't store a float!
        some_int_var = 0.5;
        // Character variables can't store a string!
        some_char_var = "uh oh I don't belong here!";

Additionally, variables can only be assigned to after they've been declared.

.. admonition:: Good
    :class: good

    .. code-block:: c

        int some_var;
        some_var = 10;


.. admonition:: Bad
    :class: bad

    .. code-block:: c

        some_var = 10;
        int some_var;

..

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Reassign an even value to ``some_number`` to make the code below print out a valid statement. 

.. code-block:: c

    #include <stdio.h>

    int main() {
        int some_number;
        some_number = 11;

        // Add a new assignment here


        // No need to touch this! This prints out the variable.
        printf("%d is even!", some_number);
    }

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int some_number;
                some_number = 11;

                // Add a new assignment here
                some_number = 4;

                // No need to touch this! This prints out the variable.
                printf("%d is even!", some_number);
            }