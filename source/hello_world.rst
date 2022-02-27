Hello World 👋
===============

The website should automatically have generated some C code when you'd opened it. If you are using your own editor, you can copy and paste th following text into your source file.

.. code-block:: c

	#include <stdio>

	int main() {
	    printf("Hello world!");
	    return 0;
	}

Run your code and you should see the text "Hello world!" printed to your output window!

But how this code actually works.

``main()``
----------

``main()`` is a function. We will talk more about ``functions`` and what ``return`` is in the :ref:`functions:Functions ⚙️` page. 

All you have to know for now is that this is the starting point of the program. Everything between the brackets of main will be ran when the program starts.

The "stuff" in between the brackets are **statements**.

Statements
^^^^^^^^^^

A statement is a single piece of instruction in our code. In C, statements always end with a semicolon, which is the ``;`` symbol. You should put each statement on it's own line to keep your code readable --- otherwise it may get too cramped and cluttered!

.. admonition:: Good
	:class: good

	.. code-block:: c

		#include <stdio>

		int main() {
		    printf("My name is Bob, ");
		    printf("my name is Joe, "); 
		    printf("and my name is Tom!"); 
		    return 0;
		}


.. admonition:: Bad
	:class: bad
	
	.. code-block:: c

		#include <stdio>

		int main() {
		    printf("My name is Bob, "); printf("my name is Joe, "); printf("and my name is Tom!"); return 0;
		}

``printf()``
------------

``printf()`` is a function, whose name is short for "print format". This function displays or **prints** text to the output window. 

printf can print text using the statement ``printf("text");`` where ``text`` with the text you want to print.

.. seealso::

	We will talk more about functions later in a the :ref:`functions:Functions ⚙️` chapter.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print "My name is __blank__", name to the output, replacing "__blank__" with your name. 

.. code-block:: bash
		
	My name is Bob!

..

	.. collapse:: Solution ✅

		.. code-block:: c

			#include <stdio>

			int main() {
			    printf("My name is Bob!");
			    return 0;
			}

|check| Print your name to the output like before except use a print statement for each word

.. code-block:: bash
	
	My name is Bob!

..

	.. collapse:: Solution ✅

		.. code-block:: c

			#include <stdio>

			int main() {
			    printf("My ");
			    printf("name ");
			    printf("is ");
			    printf("bob ");
			    return 0;
			}
