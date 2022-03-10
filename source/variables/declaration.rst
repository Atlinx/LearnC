Declaration ➡️
==============

To create or **declare** a variable in C, you do

    .. code-block:: c

        type var_name;

    .. 

    where,

    ``type`` is the type keyword of the variable.

    ``var_name`` is the name of the variable.

Here's a table below of the different data types in C again but with their keyword types. Note that strings are not shown here because they are declared in a different way. 

.. list-table::
    :header-rows: 1
    :widths: 10 20 50 30

    * - Name
      - Type Keyword 
      - Description
      - Examples
    * - Integer
      - ``int``
      - Represents an integer.
      - 0, -10, 2, 150, -349
    * - Float
      - ``float``
      - Represents a decimal number, with at most 7-8 decimal places.
      - 0, -10.43, 2.23420, 150.493, -349, -4230.340
    * - Character
      - ``char``
      - Represents a single symbol.
      - 'a', 'D', '1', '#', '^', '%', '&'

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        int number;
        float decimal_number;

The name of the variable can only contain letters (``A-Z``), numbers (``0-9``), and underscores (``_``). The name must also begin with a letter. It cannot have any spaces.

.. admonition:: Good
    :class: good
    
    .. code-block:: c

        int valid_name;
        char ValidName;
        float valid_name_0439;

.. admonition:: Bad
    :class: bad
    
    .. code-block:: text

        int 92invalid_name;
        char _invalid_name;
        float invalid#_name&;

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Fix the following variable names so the program compiles:

.. code-block:: c

    #include <stdio.h>

    int main() {
        int cool name;
        char _some_name;
        float ben&jerry;
    }

..

    .. collapse:: Solution ✅

        There may be mutliple valid solutions. Here's one solution:

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int cool_name;
                char some_name;
                float ben_and_jerry;
            }