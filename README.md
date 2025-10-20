# Gas-Station-Simulation

A **discrete-event simulation** of a gas station built using SimPy
The simulation models multiple users arriving to a gas station that has:
- A limited number of **fuel pumps**.
- A **shop** that some users must visit before fueling.
- Random arrival times, fueling durations, and user states.

This simple model demonstrates how to use SimPy’s resources to simulate real-world queuing systems.

---

## Overview

Each **User** can be in one of two states:

- `True` → ready to fuel immediately.  
- `False` → must visit the shop before fueling.

The **GasFiller** manages:
- `n_pumps`: number of fuel pumps available.
- `n_shop`: number of customers the shop can serve at once.

Users arrive at random times within the first 10 simulated time units, queue for available resources, and complete their actions.  
After fueling, their total time in the system is recorded.

---

## Features

✅ Models concurrent users with queues.  
✅ Randomized arrivals and fueling durations.  
✅ Records each user’s total time in the system.  
✅ Prints simulation log and summary statistics.  
✅ Clean, modular structure easy to extend.

