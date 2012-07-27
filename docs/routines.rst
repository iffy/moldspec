Routines
========


Mold
----

This routine finds out what state a system should be in, then does what's needed to make it conform to that state.

Here's some pseudo code describing how the state of a machine is set:

.. code-block:: python

    facts = FactChecker()
    prescription = Prescriber(facts)
    while 1:
        observation = Observer(prescription)
        steps = Choreographer(facts, prescription, observation)
        if not steps:
            break
        Performer(steps)


An implementation might replace some or most of those function calls with calls to remote systems.  Neither error handling nor logging are shown in the pseudo code.
