# The Santa Problem

This example demonstrates an example solution to the santa problem that
follows:

 In this problem there are:
 - 1 Santa
 - 9 Reindeer
 - 7 Elves

 - When Santa and 9 Reindeer are available then they should be taken
   (making them unavailable) and deliver presents. When they are
   finished, Santa becomes available again and the Reindeers each go on
   holiday, becoming available again when they come back from holiday.

 - When Santa and 3 Elves are available then they should be taken
   (making them unavailable) and meet in the study. When they are
   finished, Santa becomes available again and the Elves each go to
   work, becoming available again when they finish working.

We provide the following solutions:

## groups-and-status-checks.verona

A soultion with a cown of santa and cowns of groups of workers. Workers add themselves to groups when they are ready, behaviours repeatedly request access santa and to the groups to check if enough workers are present. If enough workers are present then the tasks are performed, otherwise a behaviour making the same check is created.

## groups-and-tasks.verona

## groups-and-pools.verona

## groups-and-barrriers.verona
