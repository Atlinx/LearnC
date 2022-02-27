Expressions and Operators 🔢
============================

Operators
---------

Operators in C are symbols that tell the computer to perform a specific operation on some inputs. The inputs of an operator are called the **operands**.

Operators are taken primarily from math and logic. Here's a list of the math operators in C.

.. list-table::
	:header-rows: 1
	:widths: 10 10 50 30

	* - Name
	  - Symbol
	  - Description
	  - Example
	* - Addition
	  - ``+``
	  - Adds two numbers together
	  - ``50 + 10``
	* - Subtraction
	  - ``-``
	  - Adds two numbers together
	  - ``50 - 10``
	* - Multiplication
	  - ``*``
	  - Multiplies two numbers together
	  - ``50 * 10``
	* - Division
	  - ``/``
	  - Divides the first number by the second number
	  - ``50 / 10``
	* - Modulo
	  - ``%``
	  - Gets the remainder from dividing the first number by the second number 
	  - ``50 % 10``

.. caution::
	Just like in regular math, you cannot divide by zero. If you do then your program may behave unexpectedly!

Modulo
^^^^^^

There is a special "remainder" operator called the **modulo** operator. It can be used to find the remainder after two integers.

.. admonition:: Ex.
	:class: example

	.. code-block:: c

		4 % 2 = 0		// 4 / 2 = 2 remainder 0
		3 % 2 = 1		// 3 / 2 = 1 remainder 1

		10 % 3 = 1		// 10 / 3 = 2 remainder 1
		11 % 3 = 2		// 11 / 3 = 2 remainder 2

Integer Division
^^^^^^^^^^^^^^^^

If you divide an integer by an integer, the result is just the quotient.

This means if you divide something like ``5 / 2``, you would not get a fraction like ``2.5`` and instead get ``2``.

Expressions
-----------

Expressions are one ore more operators grouped together. For example these are some expression:

.. admonition:: Ex.
	:class: example

	.. code-block:: c

		5 + 20 / 5
		3 * 4 - 1

When we "solve" an expression, it's called **evaluating** the expression. Expressions can also use parenthesis to tell C which operators should be evaluated first. 

.. admonition:: Ex.
	:class: example
	
	.. code-block:: c

		(5 + 10) * 2
		4 / ((2 - 20) * 10)

Order of Operations
^^^^^^^^^^^^^^^^^^^

C's math operators follow the order of operations from math. This means the order operators are evaluated is

1. `()` Expressions in Parentehsis
2. `*`, `/`, `%` Mulitplication, Division, and Modulo
3. `+`, `-`, Addition and Subtraction

.. admonition:: EX.
	:class: example

	.. code-block:: c
		
		5 - 3 * 3 % 2     = 5 - 9 % 2   = 5 - 1   = 4
		(5 - 3) * 3 % 2   = 2 * 3 % 2   = 6 % 2   = 0

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| What does the expression ``5 - 2 * 3 + 1`` evaluate to?

	.. collapse:: Solution ✅

		``5 - 2 * 3 + 1    = 5 - 6 + 1   = -1 + 1   = 0``

|check| What does the modulo operator do?

	.. collapse:: Solution ✅

		The modulo operator gets the remainder from dividng the first number by the second number

|check| What does the experssion ``3 / 2`` evaluate to?

	.. collapse:: Solution ✅

		``3 / 2 = 1`` due to :ref:`Integer Division`.

|check| What does the experssion ``(5 + 2) % 3 / 2``

	.. collapse:: Solution ✅

		``(5 + 2) % 3 / 2   = 7 % 3 / 2   = 1 / 2   = 0``