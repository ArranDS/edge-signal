# Adaptive Edge Signal Triage for Constrained 5G Links
## Overview
This project looks into how bandwidth effiency and robustness in a field-deployable RF sensing system can be improved.
Instead of simply transmitting all captured RF data, this system performs prioritisation at the edge and will only send signals of interest over a constrained 5G link.

## Problem
The baseline system suffers from:
- high data volume from RF capture
- slow edge inference using a heavyweight model
- unnecessary transmission of all data
- poor performance under degraded connectivity
- lack of security considerations

## Solution
This project introduces an **edge-side triage system** that:
- uses lightweight filtering before the heavy inference
- assigns priority scores to each detected signal
- transmits only the high-value signals
- buffers medium-priority events locally
- drops low value traffic under congestion

## Prototype
The python simulation demonstrates:
- event generation and scoring
- adaptive prioritisation
- bandwidth-constrained transmission
- graceful degradation under poor connectivity

## How to Run
```bash
python edge_signal_triage_sim.py




