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

Debugging is hard
=================

----

.. image:: images/Commodore_Grace_M._Hopper,_USN_(covered).jpg
    :width: 600px

----

.. image:: images/H96566k.jpg

----

.. image:: images/Commodore_Grace_M._Hopper,_USN_(covered).jpg
    :width: 600px

----

Not all bugs are immediately obvious
====================================

----

.. code:: python 

    def main():

        # Obviously bad code follows
        for i in range(1, 30):
            i /= 4

        if i == 30:
            print("Completed")

    if __name__ == "__main__":
        main()

----

So what happened?
=================

----

.. code:: python 

    def main():

        # Obviously bad code follows
        for i in range(1, 30):
            i /= 4

        if i == 30:
            print("Completed")

    if __name__ == "__main__":
        main()

When we run this nothing is displayed.

----

The lowly print() statement
===========================

----


