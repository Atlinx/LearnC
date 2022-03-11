Switch Statement 🎚️
====================

Sometimes when using if statements, you may end up doing something like this:

.. code-block:: c
   
    int target_value = 0;

    if (target_value == 1) {
        printf("1");
    } else if (target_value == 2) {
        printf("2");
    } else if (target_value == 3 || target_value == 4) {
        printf("3 or 4");
    } else if (target_value == 5) {
        printf("5");
    } else {
        printf("Didn't match anything!");
    }

However you can achieve the same thing using a switch statement.

.. code-block:: c

    int target_value = 0;

    switch(target_value) {
        case 1:
            printf("1");
            break;
        case 2:
            printf("2");
            break;
        case 3:
        case 4:
            printf("3 or 4");
            break:
        case 5:
            printf("5");
            break;
        default:
            printf("Didn't match anything!");
    }

Lets take a look at a general switch statement to understand how to write one:

.. code-block:: c

    switch(target_value) {
        case value_1:
            // Some code
            break;
        case value_2:
            // Some code
            break;
        ...
        default:
            // Some code
    }

``target_value``
    is the value we want to check.

``case value_1:``
    is a **case**. Cases in a switch statement are the different values that we check is equal to the ``target_value``.

    .. tip::

        Don't forget the colon after the value for the case!

``break``
    is a statement that, when used inside a case, will exit the switch. Break statements are actually optional and if omitted, your program will execute the next case's code if it exists. This behaviour is known as **fall-through**.

    .. admonition:: Ex.
        :class: example

        The code below will print "34".

        .. code-block:: c
        
            switch(3) {
                case 3:
                    printf("3");
                case 4:
                    printf("4");
            }

``default``
    is a special type of case that the program runs if ``target_value`` could not be matched. Think of this as an else statement for switches.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Make a program, using a switch statement, that converts a number from 1-7 to a day of the week.

For example, 1 would be converted into "Sunday", 2 would be converted into "Monday", and so forth. If you get a number that's not 1-7, then print "Number must be 1-7!".

.. code-block:: c

    #include <stdio.h>

    int main() {
        int day_of_week = 0;

        printf("Please enter a number from 1-7 to convert to a day of the week:\n");
        scanf("%d", &day_of_week);

        switch(day_of_week) {
            case 1:
                printf("Sunday");
                break;
            case 2:
                printf("Monday");
                break;
            case 3:
                printf("Tuesday");
                break;
            case 4:
                printf("Wednesday");
                break;
            case 5:
                printf("Thursday");
                break;
            case 6:
                printf("Friday");
                break;
            case 7:
                printf("Saturday");
                break;
            default:
                printf("Number must be 1-7!");
        }

        return 0;
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