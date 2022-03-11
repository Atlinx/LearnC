Scanf() ⌨️
=================

What if we wanted to get input from the user?

You may have noticed you could type in the output window --- This is how we can send text to our program.

To request input from the user, we do 

    .. code-block:: c

        scanf(format_string, &variable1_name, &variable2_name, ...);
    
    ..

    where

    ``format_string``
        is a string that contains **format specifiers**. Format specfiers are special strings that start with `%` and represent a type.
    
    ``&variable1_name, &variable2_name, ...``
        are the variables, separated by commas, that go with the format specfifiers. The 1st variable receives the value gotten by the 1st format specifier. The 2nd variable receives the value gotten by the 2nd format specifier, and so forth.

        .. important::

            For string variables do not include the ``&`` symbol in front of it.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        int my_number_variable = 0;
        scanf("%d", &my_number_variable);
        printf("%d", my_number_variable);   // Input: 10
        
        // Input:
        // 10

        // Output: 
        // 10
        
        
        // Input:
        // hello

        // Output:
        // 0

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        int my_number_variable = 0;
        char my_string_variable[32] = "";
        scanf("%d %s", &my_number_variable, my_string_variable);
        printf("Gotten: %d %s", my_number_variable, my_string_variable);
        
        // Input: 
        // 10 apples
        
        // Output:
        // Gotten 10 apples

You can get a Q&A like behaviour by having a ``printf`` statement, before your ``scanf``, that asks a questions.

.. admonition:: Ex.
    :class: example

    .. code-block:: c

        int number = 0;
        printf("What is your favorite number?\n");
        scanf("%d", &number);
        printf("I got it! Your favorite number is %d.", number);

.. note::

    By default ``scanf`` actually asks for input
    right where the last ``printf`` left off. So in the example above, the newline character (``\\n``) after the question 
    lets the user type their response on the next line instead of on the same line as the question. 

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Ask the user how they are feeling today and print out their response. 

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                char feelings[64] = "";

                printf("How are you feeling today?\n");
                scanf("%s", feelings);
                printf("You are feeling %s.", feelings);

                return 0;
            }