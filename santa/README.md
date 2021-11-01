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

A solution with a cown of santa and cowns of groups of workers. Workers add themselves to groups when they are ready, behaviours repeatedly request access santa and to the groups to check if enough workers are present. If enough workers are present then the tasks are performed, otherwise a behaviour making the same check is created.

## groups-and-tasks.verona

Workers are collected into groups. A task creates a promise and hands the it to a group of workers, a behaviour waits for the promise to be fulfilled with the desired number of workers. When the number of workers are available in the group, the tasks promise is fulfilled and a new promise created in its place.

## groups-and-pools.verona

Workers belong to pools and behaviours request a number of those workers. When a pool has enough workers, the pool fulfills a request and provides the required number. Once finished, the workers are automatically returned to their origin pool.

## groups-and-barrriers.verona

Workers and Santa are represented by processes. Signals, Groups and Barriers are used to communicate when processes are at specific points of execution. When enough workers reach a synchronisation point then a number of them are let through to do some colloborative task.
