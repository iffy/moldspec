# Running the tests #

Install Twisted then do:

    trial mold


# Components #

One goal of this project is to standardize configuration management.  There are a variety of tools that do things their own way, making the cost of switching or evaluating high.

To that end, all of the major components define an API and are replaceable -- if you don't like the way a component is working, you can write your own.


## Conformer ##

The job of the conformer is to make a machine match a JSON state description.


## Inspector ##

The job of the inspector is to read the current state of a machine.


## State maker ##

The job of the state maker is to generate a JSON state description based on data from the Inspector.