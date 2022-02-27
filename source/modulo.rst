Modulo 🔢
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
	* - Modulo
	  - ``%``
	  - Gets the remainder from dividing the first number by the second number 
	  - ``50 % 10``

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