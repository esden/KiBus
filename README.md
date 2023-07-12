# KiBus length matching script

This script implements way to monitor multiple nets, combined into a bus that
needs to be length matched.

The goal of this script is to combine the different features implemented
throughout the fairly vast selection of lengthmatching python scripts for
KiCad.

This script is also meant as a playground and prototyping environment to figure
out how a future UI within KiCad could look like to implement bus length
matching capability.

# Main features

The currently implemented features are:

* Monitor and display the length of multiple nets
* Display and sort by the difference of each trace to the max length trace
* Display and sort by the difference of each trace to the median length trace
* Visually indicate through background color how big the difference of each
  trace is to the target length
* Load the Bus specification from a file
* Ability to length match a wire that consists of multiple nets

Features on the wishlist
* Select target length
* Add bonding wire length adjustment.
* Add via length
* Store  project config file defining the bus nets and the length
  matching requirements. (this should eventually become part of the net class
  parameters within kicad) 
* Edit the bus definition file from the GUI
