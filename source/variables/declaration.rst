Declaration ➡️
==============

To create or **declare** a variable in C, you do

    .. code-block:: c

        type var_name;

    .. 

    where,

    ``type`` is the type of the variable.

    ``var_name`` is the name of the variable.

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

    .. collapse:: Solution ✅

        There may be mutliple valid solutions. Here's one solution:

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int cool_name;
                char some_name;
                float ben_and_jerry;
            }