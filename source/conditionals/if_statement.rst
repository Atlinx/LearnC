If Statement 🌿
=================

An if statement is the most basic conditional. It appears in the format of

.. code-block:: c

	if (condition) {
		// Conditional code here
	}
	// Code after

where 

	``condition``
		is the a true/fales value. In C, true is represented by a non-zero number, often times 1, while false is represented by 0.
	
	``{}```
		The code between the brackets will be executed if the condition is true.

When the program reaches an if statement, it will check if 

.. code-block:: c

    #include <stdio>

    int main() {
        printf("Hello world!");
        return 0;
    }