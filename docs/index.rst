.. aalog documentation master file, created by
   sphinx-quickstart on Thu Dec 21 22:33:55 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to aalog's documentation!
=================================

aaLog is an Adventurous Activities Logging package, which you can use to keep track 
of your outdoor activites, in a simple and flexible way.

Activity entities
=================

Activities are logged against entities, which are structured as follows

Region > Site > Section

Region is a broad area for collecting sites.  It typically is smaller than a state.
Examples:
* Caving: Upper South East, Bungonia or Mole Creek.
* Canyoning:  Blue Mountains
* Climbing: Morialta, Arapiles

Site is a more specific location within a region.
Examples:
* Caving: A specific cave, or network or entrances
* Canyoning: A cluster of canyons, typically attached to a common water catchment or trail head
* Climbing: A specific crag

Section is a specific part that belongs to a Site.
Examples:
* Caving: A part of a cave system
* Canyoning: A specific canyon
* Climbing: A route on a crag

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
