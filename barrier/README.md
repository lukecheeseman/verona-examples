# Barrier Synchronisation 

The purpose of this subdirectory is how cowns and behaviours can be used to create barrier synchronisation between partcipants.

This subdirectory contains the following designs:
- behaviour-ordering.verona: synchronisation through behaviour ordering constraints.
- data-flow.verona: synchronisation through promises and participants being passed between behaviours.
- exchange-promises.verona: synchronisations through participants awaiting promises fulfilled by other partcipants.
- sophisticated.verona: synchronisation through a barrier object, built using promises, to which participants subscribe.
