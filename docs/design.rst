Design
======

Mold is at least two things:

    1. A description of standards for configuration management systems.
    2. An example implementation of those standards.

XXX

Setting state
=============

Here's some pseudo code describing how the state of a machine is set:

.. code-block:: python

    facts = getFacts()
    prescription = getPrescription(facts)
    while 1:
        state = getState(prescription)
        steps = getSteps(facts, prescription, state)
        if not steps:
            break
        execute(steps[0])


An implementation might replace some or most of those function calls with calls to remote systems.  Neither error handling nor logging are shown in the pseudo code.
