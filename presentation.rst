:title: Introduction to Debugging in Python
:author: Craig Maloney
:css: presentation.css

.. title:: Introduction to Debugging in Python

----

Introduction to Debugging in Python
===================================

* Author: Craig Maloney
* Email: craig@decafbad.net
* Presented: 2017-04-11

----

Programming is hard
===================

----

Programming leads to bugs
=========================

----

.. image:: images/Commodore_Grace_M._Hopper,_USN_(covered).jpg
    :width: 600px

----

.. image:: images/H96566k.jpg

----

Not all bugs are as obvious
===========================

----

Debugging is not just about fixing bugs...
==========================================

----

Debugging is about matching our expectations of what the code is doing with the reality of what the computer is executing
=========================================================================================================================

----

What does this code do?
=======================

----

.. code:: python 

    # Example 1
    def main():

        # Obviously bad code follows
        for i in range(1, 20):
            i /= 4

        if i == 20:
            print("Completed")

    if __name__ == "__main__":
        main()

----

So, what happened?
==================

----

.. code:: python 

    # Example 1
    def main():

        # Obviously bad code follows
        for i in range(1, 20):
            i /= 4

        if i == 20:
            print("Completed")

    if __name__ == "__main__":
        main()

When we run this nothing is displayed.

----

The lowly print() statement
===========================

----

.. code:: python

    # Example 2
    def main():

        # Obviously bad code follows
        for i in range(1, 20):
            i /= 4
            print(i)

        if i == 20:
            print("Completed")

    if __name__ == "__main__":
        main()

----

::

    craig@lister:~/projects/intro_debugging_python$ python3 example2.py 
    0.25
    0.5
    0.75
    1.0
    1.25
    1.5
    1.75
    2.0
    2.25
    2.5
    2.75
    3.0
    3.25
    3.5
    3.75
    4.0
    4.25
    4.5
    4.75

Now we can see what's happening with the ``i`` variable.

----

What we learned...
==================

* ``print(i)`` shows us the value inside of ``i``
* ``i`` is reset each iteration by the ``range(1, 20)`` generator.
* ``i`` will never be equal to ``20`` in this program, so we have dead code.

----

Let's try another example...
============================

----

.. code:: python

    # Example 3
    def main():
        list_of_numbers = []
        with open("list_of_numbers", 'rt') as f:
            for number in f:
                list_of_numbers.append(number)

        print("The sum is {total}".format(total=sum(list_of_numbers)))

    if __name__ == "__main__":
        main()

----

Running the code...
===================

----

::

    craig@lister:~/projects/intro_debugging_python$ python3 example3.py 
    Traceback (most recent call last):
    File "example3.py", line 10, in <module>
        main()
    File "example3.py", line 7, in main
        print("The sum is {total}".format(total=sum(list_of_numbers)))
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

----

So, what happened?
==================

----

Sure we could print the data, but...
====================================

----

::

    craig@lister:~/projects/intro_debugging_python$ wc -l list_of_numbers 
    2000001 list_of_numbers
    
----


