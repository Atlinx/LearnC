Expressions 🔢
===============

Expressions are one ore more operators grouped together.

.. admonition:: Ex.
	:class: example

	.. code-block:: c

		5 + 20 / 5
		3 * 4 - 1

When C hits an expression, it will attempt to "solve", or **evaluate** the expression to simplify it down to just one value. This means you can use expressions whereevere you can use a single value!

.. admonition:: Ex.
	:class: example

	.. code-block:: c

		int some_integer = 350 + 2 / 29;
		int other_integer = some_integer;

		printf("%d is my number!", some_integer);
		printf("%d is an even number!", some_integer * 2);

Expressions can also use parenthesis to tell C which operators should be evaluated first.

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

|check| What does the experssion ``3 / 2 + 2`` evaluate to?

	.. collapse:: Solution ✅

		``3 / 2 + 2   = 1 + 2   = 3`` due to :ref:`operators/integer_division:Integer Division ➗`.

|check| What does the experssion ``(5 + 2) % 3 / 2``

	.. collapse:: Solution ✅

		``(5 + 2) % 3 / 2   = 7 % 3 / 2   = 1 / 2   = 0``