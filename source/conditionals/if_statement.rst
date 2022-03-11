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

When the program reaches an if statement, it will check if the condition is true.

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Change the value of condition so that the output of the program below is "True".

.. code-block:: c

    #include <stdio.h>

    int main() {
        int condition = 0;

        if (condition) {
            printf("True");
        }

        if (!condition) {
            printf("False");
        }

        return 0;
    }

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                int condition = 1; // Setting this to any non-zero value would mean true.

                if (condition) {
                    printf("True");
                }

                if (!condition) {
                    printf("False");
                }

                return 0;
            }