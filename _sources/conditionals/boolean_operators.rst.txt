Boolean Operators ☑️
=====================

In programming the values true or false are called **boolean** values. In C, there is no dedicated data type for booleans. Instead, true is represented by any non-zero integer and false is represented by 0.

Therefore **boolean operators**, or **logic operators**, are operators that perform logical comparisons that evaluate to either 1 (true) or 0 (false).

C contains all the comparisons you would find in regular mathematics. Here's a list of all of the operators:

.. list-table::
    :header-rows: 1
    :widths: 10 10 50 30

    * - Name
      - Symbol
      - Description
      - Example
    * - Not
      - ``!``
      - Is placed infront of an expression. Inverts the boolean value of the experssion, converting any non-zero numbers to zero and converting zero to one.
      - ``!(0) is true, !(1) is false``
    * - Equals
      - ``==``
      - Checks if two values of the same type equal each other
      - ``'a' == 'a' is true, 50 == 23 is false``
    * - Not equals
      - ``!=``
      - Checks if two values of the same type are not equal to each other
      - ``'a' != 'a' is false, 50 != 23 is true``
    * - Greater than
      - ``>``
      - Checks if a number is greater than another number
      - ``50 > 2 is true, 2 > 2 is false``
    * - Greater or equal to
      - ``>=``
      - Checks if a number is greater than or equal to another number
      - ``50 >= 2 is true, 2 >= 2 is true``
    * - Less than
      - ``<``
      - Checks if a number is less than another number 
      - ``2 < 50 is true, 2 < 2 is false``
    * - Less than or equal to
      - ``<=``
      - Checks if a number is less than or equal to another number 
      - ``2 <= 50 is true, 2 <= 2 is true``
    * - Or
      - ``||``
      - Checks if either of two boolean values is true. 
      - ``1 || 1 is true, 0 || 1 is true, 0 || 0 is false ``
    * - And
      - ``&&``
      - Checks if both of two boolean values is true.
      - ``1 && 1 is true, 0 && 1 is false, 0 && 0 is false``

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        int boolean_result = 1 == 2;
        // boolean_result is 0 (false)

        boolean_result = 1 != 2;
        // boolean_result is 1 (true)

        boolean_result = 3 >= 3;
        // boolean_result is 1 (true)

        
        boolean_result = 0; // (false)
        boolean_result = !boolean_result;
        // boolean_result is 1 (true)

Boolean operators have lower precedence than math operators, meaning math operators will be evaluated first. But when in doubt, use parenthesis to explictly group your expressions!

.. admonition:: Fun fact

    Booleans are named after George Boole, who first defined an algebraic system of logic in the mid 19th century

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Write a program to print the result of the statement "50 plus 25 is greater than 40":

    .. collapse:: Solution ✅

        Should print out 

        .. code-block:: bash
        
            > 1

        .. code-block:: c
        
            #include <stdio.h>

            int main() {
                printf("%d", 50 + 25 > 40);
                return 0;
            }
