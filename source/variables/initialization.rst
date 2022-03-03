Intialization ➡️
=================

What if you wanted to declare and assign a value to a variable in just a single statement?

Well you can **initialize** a variable to give it an "initial" value. The syntax is as follows

    .. code-block:: c

        type var_name = value;

    ..

    where,

    ``type`` is the type of the variable.

    ``var_name`` is the name of the variable.

    ``value`` is the value you are intializaing the variable to.

.. caution::

    By default, C does not initialize a variable. If you only declare a varaible and then try to use it, your program will run behave unexpectedly!

    It's good practice to intialize every variable you declare to a value to avoid this problem.

.. 

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Initialize ``some_number`` to an even number to make the code below print out a valid statement. 

    .. code-block:: c

        #include <stdio.h>

        int main() {
            // Edit this!
            int some_number;

            // No need to touch this! This prints out the variable.
            printf("%d is even!", some_number);
        }

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int some_number = 4;

                // No need to touch this! This prints out the variable.
                printf("%d is even!", some_number);
            }