---
title: Train Coupling Operations
---

# Train Coupling Operations

## Train coupling operations

<DocFigure src="/images/goto-couple-order.png" alt="goto couple order" width="80" />


### Coupling restrictions

Without coupling restrictions, the train will by default search *the whole map* for all trains waiting for coupling.
On the button bar, there are two commonly used restrictions:
- *Slot:* restrict coupling to trains holding the specified slot (token)
- *Station:* restrict coupling to trains waiting for coupling at a specified station
In `More options`, the other available restriction options are:
- *Slot group:* restrict coupling to trains holding a slot within the specified slot group
- *Vehicle group:* restrict coupling to trains within the specified vehicle group
- *Couple empty / Couple full:* restrict coupling to empty or fully loaded trains
- *Cargo type:* restrict coupling to trains that can load the specified cargo
- *Units couple:* restrict coupling to trains with a certain number of units
- *Speed:* restrict coupling to trains with a speed within the specified range (skip if my train has a lower/higher top speed)

### Coupling options

### Waiting schedule
By default, the coupled train will use the orders of the train that was heading to couple, but you can also press the `Waiting schedule` button, so that after coupling the train continues to follow and advance the schedule of the waiting train.


<DocFigure src="/images/use-wait-train-schedule.png" alt="use wait train schedule" width="80" />


### Early check point

By default, a train with the Go to couple order only checks for trains available for coupling when it executes the Go to couple order. However, in many cases we want the train to wait somewhere for the waiting train to get into position and then go straight to couple, for example in the scenario shown:


<DocFigure src="/images/couple-early-check.png" alt="couple early check" width="100" />


We want the train to wait at the `wait waypoint`, then go to the `reverse waypoint`, turn around and go to couple, instead of waiting at the `reverse waypoint` (which has only one waiting position) for the waiting train to get into position. For this you can use the early check point approach shown in the figure.
