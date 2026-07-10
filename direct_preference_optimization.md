# Direct Preference Optimization (DPO)

Bypasses separate reward network infrastructures entirely. It fine-tunes active model parameters directly using a reparameterized preference loss that measures log-likelihood ratio deltas between a chosen HHH response and a rejected response natively inside the language policy.

## Diagram

```mermaid
flowchart LR
  Pref[Preference Data] --> Loss[DPO Loss Formulation]
  Loss --> Policy[Updated Policy Weights]
```

[Back to README](README.md)
