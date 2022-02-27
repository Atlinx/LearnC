Variables 📦
=============

A variable is a name given to a space that the our program can use. Think of variables as a labelled box that can hold a value.

Declaring a Variable
--------------------
To create or **declare** a variable in C, you do

``var_type var_name;``
	where 
	
	``var_type`` is the type of the variable,
	
	``var_name`` is the name of the variable.

.. admonition:: Ex.
	:class: example

	.. code-block:: c

		int number;
		float decimal_number;

The name of the variable can only contain letters (``A-Z``), numbers (``0-9``), and underscores (``_``). The name must also begin with a letter.

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

Using a Variable's Value
------------------------

To use use a varaible's value, you just write the variable's name.

Printing a Variable
^^^^^^^^^^^^^^^^^^^

You can print a variable just 


Assigning Values to a Variable
******************************


Initializing a Variable
***********************
To *initialize* a variable, or create a variable that has a starting value, you do

``var_type var_name = ;``
	where 
	
	``var_type`` is the type of the variable,
	
	``var_name`` is the name of the variable.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Create a character variable can be used to represent 5820? 

	.. collapse:: Solution ✅

		Integer

|check| What type can be used to represent the letter C?

	.. collapse:: Solution ✅

		Character

|check| What type can be used to represent the phrase, "the quick brown fox jumps over the lazy dog"?

	.. collapse:: Solution ✅

		String