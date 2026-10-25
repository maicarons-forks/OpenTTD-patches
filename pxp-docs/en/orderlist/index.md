---
title: Custom Order Lists
---

# Custom Order Lists

In vanilla OpenTTD, an order list is always bound to vehicles: a vehicle can only have one order list, and multiple vehicles may share the same order list. In px-patch, players can create order lists without creating vehicles, and use custom order lists on vehicles.

## The order list manager window
From the map drop-down menu, you can open the order list manager window:


<DocFigure src="/images/orderlist-manager.png" alt="orderlist manager" width="80" />


In the order list manager window, you can create, delete, and rename order lists, as well as drag order lists into groups (drag onto `All schedules` to remove them from their group), or make an order list publicly visible.

::: warning Warning
once an order list has been made publicly visible and is in use by vehicles of other companies, it cannot be set back to private
:::


::: warning Warning
an order list cannot be deleted while it is in use by vehicles
:::

## In this section

- [Editing Order Lists](/en/orderlist/orderlist-edit)
- [Vehicles Using Custom Order Lists](/en/orderlist/orderlist-vehicle)
