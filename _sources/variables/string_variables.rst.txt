String Variables 🧵
====================

Working with string variables is different because strings are not an actual type in C.

String Declaration
------------------

Strings are actually declared differently to other variables.

To declare a string, you must do

    .. code-block:: c

        char string_var_name[length];

    .. 

    where,

    ``string_var_name`` 
        is the name of the string variable.

    ``length`` 
        is a number representing the maximum length of the string it can store. 
        
        Note that all strings in C have a special character at the end to represent the end of a string.
        This means the "true" length of the string is the length of a string + 1.

        Therefore if you wanted to store a string 3 characters long, you would have to specify the length as 4.
    
        .. admonition:: Ex.
            :class: example

            .. code-block:: c

                char my_string[4] = "hat";

.. admonition:: Ex.
    :class: example

    .. code-block:: c
    
        char my_string[50];

String Assignment and Initialization
------------------------------------

String assignment and initialization is the same as with regular variables. However you can only store strings whose character length is less than the length of the string variable.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        char my_string[6] = "apple";    // Intiailize with "apple"
        my_string = "hi";               // Store "hi"

However you cannot directly assign a string to another string.

.. admonition:: Bad
    :class: bad

    .. code-block:: c

        char my_string[4] = "hat";
        char my_other_string[4] = "rub";

        my_string = my_other_string;    // Doesn't work and causes an error.

We'll get into why in a later chapter.