Project 2 - Greeter 💬
================================

For our second project, lets make a program that greets the user. 

It should ask the user for their first name and then print a response!

.. admonition:: Ex.
    :class: example
    
    .. code-block:: bash
       
       > What is your first name?
       > Joe
       > Hello Joe, nice to meet you!

For this project, let's assume the maximum length of someone's first name is 63 characters.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print the question.

..

    .. collapse:: Hint ❓

        You can print something by writing ``printf("the stuff I want to print");``. If this seems unfamiliar to you, then check out the :doc:`\hello_word\printf` section.

        Don't forget the ``\n`` at the end of the ``printf`` statement in order to let the ``scanf`` to detect user input on the next line! 

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                printf("What is your name?\n");
                
                return 0;
            }


|check| Get user input for their first name.

..

    .. collapse:: Hint ❓

        You can get a string input into a variable from a user by writing ``scanf("%s", &string_variable_name);``. If this seems unfamiliar to you, then check out the :doc:`\variables\scanf` section.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                char first_name[64] = "";
                printf("What is your first name?\n");
                scanf("%s", first_name);
                
                return 0;
            }

|check| Print a greeting, including the user's first name.

..

    .. collapse:: Hint ❓

        You can print a string variable by writing ``printf("%s", string_variable_name);``. If this seems unfamiliar to you, then check out the :doc:`\variables\more_printf` section.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                char first_name[64] = "";
                printf("What is your first name?\n");
                scanf("%s", first_name);
                printf("Hi %s, nice to meet you!", first_name);
                
                return 0;
            }