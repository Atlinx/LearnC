Project 5 - ASCII Art 🖌️
==========================

Did you know you can make art with just text?

For example, here on the left is an ascii art of Tux, the Linux operating system mascot. On the right is an actual image of Tux.

.. image:: _img/tux.png
    :alt: Tux, the linux mascot.
    :width: 400
    :align: right

.. code-block::

                     .88888888:.
                    88888888.88888.
                  .8888888888888888.
                  888888888888888888
                  88' _`88'_  `88888
                  88 88 88 88  88888
                  88_88_::_88_:88888
                  88:::,::,:::::8888
                  88`:::::::::'`8888
                 .88  `::::'    8:88.
                8888            `8:888.
              .8888'             `888888.
             .8888:..  .::.  ...:'8888888:.
            .8888.'     :'     `'::`88:88888
           .8888        '         `.888:8888.
          888:8         .           888:88888
        .888:88        .:           888:88888:
        8888888.       ::           88:888888
        `.::.888.      ::          .88888888
       .::::::.888.    ::         :::`8888'.:.
      ::::::::::.888   '         .::::::::::::
      ::::::::::::.8    '      .:8::::::::::::.
     .::::::::::::::.        .:888:::::::::::::
     :::::::::::::::88:.__..:88888:::::::::::'
      `'.:::::::::::88888888888.88:::::::::'
    miK     `':::_:' -- '' -'-' `':_::::'`


Let's try printing our own ascii art in C then!

---------

Tasks 🎯
---------

.. |check| raw:: html

    <input type="checkbox">

|check| Print the following ascii cat into the console.

.. code-block::

    .    |\      _,,,---,,_
    .    /,`.-'`'    -.  ;-;;,_
    .   |,4-  ) )-,_..;\ (  `'-'
    .  '---''(_/--'  `-'\_)

Credits to Felix Lee for this ASCII Cat.

..

    .. collapse:: Hint ❓

        You may have to esacpe some of the characters when printing the cat. Take a look at :doc:`/hello_world/escape_sequences` if you need a refresher.

..

    .. collapse:: Solution ✅

        .. code-block:: c

            #include <stdio.h>

            int main() {
                // Write C code here
                printf(".    |\\      _,,,---,,_\n");
                printf(".    /,`.-'`'    -.  ;-;;,_\n");
                printf(".   |,4-  ) )-,_..;\\ (  `'-'\n");
                printf(".  '---''(_/--'  `-'\\_)\n");
                
                return 0;
            }