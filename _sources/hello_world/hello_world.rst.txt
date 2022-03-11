Hello World 👋
================

The Programmiz website should automatically have generated some C code when you open it. If you are using your own editor, you can copy and paste the following text into your source file.

.. code-block:: c

    #include <stdio.h>

    int main() {
        // Write C code here
        printf("Hello world!");

        return 0;
    }

Run your code and you should see the text "Hello world!" printed to your output window!

How it Works
------------

Let's go through what each portion of the code does.

``#include <stdio.h>``
    This is required for ``printf()`` to work.

``// Write C code here``
    This is a comment. Comments help explain parts of your code and do nothing when the program runs. Comments start with ``//``, and continue until of the end of the line.

``int main() {``
    This is the starting point of the program. Everything between the brackets of main runs, from top to bottom, when the program starts.

    The "stuff" between the brackets that is ran are called **statements**. Most statements end with a semicolon (``;``).

``printf("Hello world!");``
    This line of code displays or **prints** "Hello world!" to the output window. Notice how it ends with a ``;``, because this is a statement.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Try changing "Hello world!" to your name and see what it prints!

    .. collapse:: Solution ✅

        .. code-block:: bash
                
            Bob


        .. code-block:: c

            #include <stdio.h>

            int main() {
                // Write C code here
                printf("Bob");

                return 0;
            }