---
title: Train Decoupling Operations
---

# Train Decoupling Operations

## Choosing the orders after decoupling
Through the drop-down menus for both parts after decoupling, you can choose different orders for the two parts of the train.


<DocFigure src="/images/decouple-order-editor.png" alt="decouple order editor" width="60" />


| *Type* | *Behavior* | *Order actually generated* | *Remarks* |
| --- | --- | --- | --- |
| Keep orders without loading | Keep the original orders and skip loading/unloading | The original orders | The original orders will be shared |
| Load and keep orders | Keep the original orders, and load/unload at the decoupling station | The original orders | Same as above |
| Wait for couple without loading | Wait for couple at the decoupling station | Keep the original order and append a `Wait for couple` order entry after the decoupling station |  |
| Load and wait for couple | Load/unload at the decoupling station, then wait for couple | Same as above |  |
| Use a schedule without loading | After decoupling, execute a player-defined custom order list, without loading/unloading | An `Execute schedule` order entry | See also [Custom Order Lists](/en/orderlist/) |
| Load and use a schedule | After decoupling, load/unload first, then execute the player-defined custom order list | A `Go to decoupling station` order entry<br>A `Execute schedule` order entry<br>A `Conditional jump: always skip to the second entry` | Same as above |
| Allow leaving in the same direction once the other part has left | After decoupling, this part is not forced to leave from the decoupling side; it may wait for the other part to leave the station and then leave from the same side | Independent of the orders; does not touch the orders | Only one of the two parts after decoupling may tick this; it cannot be ticked for both parts |

::: tip Note
for the impact of loading/unloading on passenger flow, see also: [Cargo Distribution when Decoupling](/en/decouple/decouple-passenger)
:::


## Choosing the number of vehicles to decouple
To choose the number of vehicles to decouple, you can directly click the marker button below the vehicles in the decoupling preview. For trains that couple first and decouple later, the decoupling preview may be inaccurate; in that case you can click the decouple count above the preview and type the number manually.

<DocFigure src="/images/decouple-num.png" alt="decouple num" width="80" />

::: warning Warning
if the number of vehicles to decouple is greater than the actual number of vehicles, the train will still decouple one vehicle.
:::

::: tip Note
when the number of vehicles to decouple is 0, the leading locomotive will be decoupled automatically
:::


## Conditional order jump
After decoupling, the decoupled trains are given the `First part` and `Second part` conditional labels, which can be used in conditional order jumps.


<DocFigure src="/images/decouple-conditional.png" alt="decouple conditional" width="80" />
