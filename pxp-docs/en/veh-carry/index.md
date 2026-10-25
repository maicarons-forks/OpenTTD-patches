---
title: Vehicle Transport
---

# Vehicle Transport

::: tip Note
the vehicle transport feature originates from the [Road Veh Transport patch](https://github.com/Babel-TTT/OpenTTD-patches/tree/feature/road-veh-transport/); px-patch is based on this patch, with optimizations and feature improvements.
:::


Turn on the `Vehicle transport` option in the settings to transport vehicles in the game.


<DocFigure src="/images/veh-carry-setting.png" alt="veh carry setting" width="80" />


## Simple vehicle transport orders

A vehicle can be transported simply by setting `Wait to be transported` and `Be unloaded here`.


<DocFigure src="/images/road-veh-carry-order.png" alt="road veh carry order" width="80" />


For a carrier vehicle, you first need to refit it to vehicle transport.


<DocFigure src="/images/carry-veh-refit.png" alt="carry veh refit" width="40" />


For vehicles refitted to vehicle transport, the orders added by default are all Load vehicles / Unload vehicles.


<DocFigure src="/images/carry-veh-order.png" alt="carry veh order" width="80" />


## Restrictions
### Weight restriction

A carrier vehicle cannot transport vehicles without limit; it is restricted by the total weight. When an aircraft transports road vehicles, the program simply calculates whether the road vehicle still fits into the aircraft; if not, the vehicle will not be transported. When trains or ships transport road vehicles, the program tries to put the road vehicles one by one into a wagon/hold until a suitable wagon/hold is found. When a ship transports trains, the program tries to put every wagon into a hold one by one; the transport is only possible when all locomotives have been placed into holds (they may be different holds).

### Unloading station restriction

For road vehicles, buses are not allowed to enter goods stations, trucks are not allowed to enter bus stations, and articulated vehicles are not allowed to enter bay-type stations (the same as the road vehicle station requirements in vanilla OpenTTD).

For trains, the rail type must match, and the platform length must be greater than the train length.

## In this section

- [Vehicle Transport Order Settings](/en/veh-carry/orders)
- [Cross-Company Vehicle Transport](/en/veh-carry/cross-company)
