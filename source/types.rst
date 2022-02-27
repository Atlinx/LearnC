Types 🔤
=========

A **type** in C is a representation of a certain "type" of data. Here are the list of the 3 common types we will be dealing with:

.. list-table::
	:header-rows: 1
	:widths: 10 10 50 30
	
	* - Name
	  - Keyword 
	  - Description
	  - Examples
	* - Integer
	  - ``int``
	  - Represents an integer.
	  - 0, -10, 2, 150, -349
	* - Float
	  - ``float``
	  - Represents a decimal number, with at most 7-8 decimal places.
	  - 0, -10.43, 2.23420, 150.493, -349, -4230.340
	* - Character
	  - ``char``
	  - Represents a single symbol.
	  - 'a', 'D', '1', '#', '^', '%', '&'
	* - String
	  - ``char *``
	  - Represents a sequence of characters.
	  - "hello world!", "the quick brown fox"

More on Strings
----------------

In programming, a sequence of characters is called a **string**. Although many programming languages have a dedicated string type, C does not, which is why you see String using the ``char *`` keyword in the previous table. But for this guide, we will consider strings to be a "type"

.. note::
	The name "string" comes from using the word "string" to describe lists of objects, such "a string of beads". For the string type, it means "a string of characters".

.. seealso::

	We will go into what ``char *`` means and how strings are represented later in the :ref:`pointers:Pointers ☝️` chapter.


Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| What type can be used to represent 5820? 

	.. collapse:: Solution ✅

		Integer

|check| What type can be used to represent the letter C?

	.. collapse:: Solution ✅

		Character

|check| What type can be used to represent the phrase, "the quick brown fox jumps over the lazy dog"?

	.. collapse:: Solution ✅

		String