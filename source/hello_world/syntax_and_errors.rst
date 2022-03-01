Syntax and Errors 📏
=====================

**Syntax** is the rules of a programming language. In C, if you break these rules and compile the program, the compiler will show an error.

As we saw in our "Hello World" example, statements must always end in a semicolon. But what happens if we forget to put a semicolon?

Consider the following code, which is missing a semicolon after ``printf("Hello world!")``.

.. code-block:: c

	#include <stdio.h>

	int main() {
		printf("Hello world")
		
		return 0;
	}

Copy and paste this code into your editor and run it.

You should get an error like

.. code-block:: bash

	/tmp/8h2q11m6TV.c: In function 'main':
	/tmp/8h2q11m6TV.c:4:23: error: expected ';' before 'return'
	    4 |  printf("Hello world")
	      |                       ^
	      |                       ;
	    5 | 
	    6 |  return 0;
	      |  ~~~~~~

Lets break down this error

``/tmp/8h2q11m6TV.c``
	This tells you which file the error occured in. 
	
	If you are using Programmiz's C online compiler, you may wonder why the file name ``8h2q11m6TV.c`` doesn't match the file name of ``main.c``. This is just a quirk with that online compiler, because your script's file name is actually managed the server in the background.

``:4:23:``
	This tells you which line and column the error occured.

	In this case, the error occured on line 4, column 23. So if you count to the 4th line and count 23 characters to the right, you will find the spot that's missing a semicolon.

.. code-block:: bash

	4 |  printf("Hello world")
	  |                       ^
	  |                       ;
	5 | 
	6 |  return 0;
	  |  ~~~~~~

Depending on your compiler, it may also show a small visual of what the code looks like around the region of error. 

For the Programmiz compiler, it shows the lines that are causing the error and puts squiggles under the parts related to the error. Additionally, it even provides an arrow indicating where the semicolon should be. 

So if you ever get an error, take the time to read about it and where it occured to fix it. If you still can't figure out what went wrong, then googling the error text is your next best option! Most of the time you will find other people asking the same question on `StackOverflow <https://stackoverflow.com/>`_ or on another online forum.

Case-sensitivity
-----------------

In general, C is case-sensitive, meaning "printf" is not the same as "PrintF", and "main" is not the same as "Main". Make sure you are careful how you type out your code!

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Fix the following code by running it and using the errors the compiler outputs:

.. code-block:: c

	#include <stdio.h>

	int main() {
		printf("Hi my name is ")
		printf("Bob!")
		
		return 0;
	}

..

	.. collapse:: Solution ✅

		.. code-block:: c

			#include <stdio.h>

			int main() {
				printf("Hi my name is");
				printf("Bob!");
				
				return 0;
			}

|check| Fix the following code by running it and using the errors the compiler outputs:

.. code-block:: c

	#include <stdio.h>

	int Main() {
		Printf("Today I'm going to the park.");
		
		RETURN 0;
	}

..

	.. collapse:: Solution ✅

		.. code-block:: c
		
			#include <stdio.h>

			int main() {
				printf("Today I'm going to the park.");
				
				return 0;
			}

