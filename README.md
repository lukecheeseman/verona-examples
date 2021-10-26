# Investigating Cowns and Behaviours

This repository contains solutions to concurrency challenges and problems using cowns and behaviours. This repository investigates the following.

* **List**: An implementation of linked list found in the Verona stdlib.
* **Bank Account**: An atomic transfer between two bank accounts.
* **Dining Philosophers**: A solution to the dining philosphers, using cowns to represent forks that the philosophers must acquire.
* **Carpark**: A shared carpark cown, departure and arrival events are generated and the carpark must accurately track the number of cars in the carpark.
* **Concert Hall**: A booking system for a concert that must not double book seats.
* **Semaphore**: A design of a semaphore, allowing only a number of processes to down the semaphore and proceed with execution, before blocking further calls until the semaphore is up'ed.
* **Barrier**: Designs for achieving barrier synchronisation. All participants must reach a barrier before they can continue execution.
* **Santa**: Solutions to the Santa problem using different designs.
* **Shared Counter**: A shared counter that must not lose any increments.
* **Channels**: Means to build commmunication channels between behaviours using cowns and promises.
* **Join Calculus**: Encoding of the join calculus using cowns and behaviours.
* **Behaviour Ordering**: Discussion on the constraining order of behaviours and the semantics of nested behaviours.
* **Busy Wait versus Promises**: Discussion of alternatives to promises.
* **Hash Map**: Discussion on how one may implement a hashmap using cowns and behaviours and its API.
* **Disjunctions of Cowns**: Discussion on the design and semantics of behaviours requiring a disjunctions of cowns.
