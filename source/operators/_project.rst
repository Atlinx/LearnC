Project 3 - Calculator 🧮
==========================

Now that we know how to use operators, lets try making a program that performs division and tells you the remainder.

The calculator should as the user to enter two space-separated integers and then print out the quotient (the result) and the remainder.

.. admonition:: Ex.
    :class: example

    .. code-block:: bash

        > Enter two space-separated integers:
        > 9 4
        > 9 / 4 = 2 with a remainder of 1

    .. code-block:: bash

        > Enter two space-separated integers:
        > 13 / 5
        > 13 / 5 = 2 with a remainder of 3

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print the question:

..

    .. collapse:: Hint ❓

        You can print something by writing ``printf("the stuff I want to print");``. If this seems unfamiliar to you, then check out the :doc:`/hello_world/printf` section.

        Don't forget the ``\n`` at the end of the ``printf`` statement in order to let the ``scanf`` to detect user input on the next line! 

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("Enter two space-separated integers:\n");
                
                return 0;
            }

|check| Get the user's input for the two numbers.

..

    .. collapse:: Hint ❓

        You can get two inputs at the same time from a user by writing ``scanf("%d %d", &first_integer_var, &second_integer_var);``. If this seems unfamiliar to you, then check out the :doc:`/variables/scanf` section.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int dividend = 0;
                int divisor = 1;
                printf("Enter two space-separated integers:\n");
                scanf("%d %d", &dividend, &divisor);

                return 0;
            }

|check| Perform the division and remainder operations and print their results.

..

    .. collapse:: Hint ❓

        You can divide two integers by doing ``first_integer / second_integer``. To get the remainder, you can use the modulo operator and do ``first_integer % second_integer``. See :doc:`/operators/integer_division` and :doc:`/operators/modulo` for more information.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int dividend = 0;
                int divisor = 1;
                printf("Enter two space-separated integers:\n");
                scanf("%d %d", &dividend, &divisor);
                printf("%d / %d = %d with a remainder of %d", dividend, divisor, dividend / divisor, dividend % divisor);

                return 0;
            }