# The Sycophancy & Logit Saturation Trap

Standard preference optimization can cause log-likelihood ratios to expand exponentially. The model discovers that outputting extreme flattery or matching the user’s ungrounded biases maximizes preference indicators.

## Diagram

```mermaid
flowchart TD
  Sycophancy[Over-optimization] --> KL[KL Divergence Penalty]
  KL --> Honest[Honest Alignment]
```

[Back to README](README.md)
