Literals 🪨
============

**Literals** are values we defined in our source code that are fixed.

Integer Literal
---------------

To create an integer literal, we write the integer like how you would normally write it. The integer literal can have an optional negative sign.

.. admonition:: Ex.
	:class: example
	
	.. code-block:: c

		10
		-10
		0
		2340

Float Literal
---------------

To create a float literal, we just write the number like how you would normally write it. The float literal can have an optional negative sign and an optional decimal point.

.. admonition:: Ex.
	:class: example
	
	.. code-block:: c

		10.2340
		-10.204
		0
		2340.43438

Character Literal
-----------------

To create a character literal, we can use single-quotes surrounding a single character:

.. admonition:: Ex.
	:class: example
	
	.. code-block:: c

		'a'
		'#'
		'&'
		'9'

String Literal
---------------

To create a string literal, we can use double-quotes surrounding some text:

.. admonition:: Ex.
	:class: example
	
	.. code-block:: c

		"The quick brown fox"
		"My name is Bob!"
		"apples, peaches, grapes"
		"101 Dalmatians"

.. tip::
	You've already seen the string literal in action, because the string you put into ``printf()`` is a string literal.

	.. code-block:: c

		printf("This is a string literal being used in printf!");

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Create a string literal for your full name. 

	.. collapse:: Solution ✅

		.. code-block:: c

			"John Smith"

|check| Create a character literal for the first letter of "apple".

	.. collapse:: Solution ✅

		.. code-block:: c

			'a'

|check| Create a float literal for three and fifty-four hundredths.

	.. collapse:: Solution ✅

		.. code-block:: c

			3.54

|check| Create an integer literal for negative four-hundred and five.

	.. collapse:: Solution ✅

		.. code-block:: c

			-405