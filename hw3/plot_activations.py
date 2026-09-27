"""Generate the activation-function figure for section 3.2 of the write-up."""

import matplotlib.pyplot as plt
import numpy as np

SAVE_PATH = "activations.png"
Z = np.linspace(-6, 6, 1201)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# (title, values, derivative title, derivative values)
PANELS = [
    ("Sigmoid", sigmoid(Z),
     r"Sigmoid derivative" "\n" r"$\sigma' = \sigma(1-\sigma)$, max 0.25",
     sigmoid(Z) * (1 - sigmoid(Z))),
    ("Tanh", np.tanh(Z),
     r"Tanh derivative" "\n" r"$\tanh' = 1 - \tanh^2$, max 1",
     1 - np.tanh(Z) ** 2),
    ("ReLU", np.maximum(0, Z),
     r"ReLU derivative" "\n" r"$ReLU' = 1_{z>0}$, undefined at 0",
     (Z > 0).astype(float)),
]


def main():
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for col, (name, values, deriv_name, deriv_values) in enumerate(PANELS):
        for row, (title, y) in enumerate([(name, values), (deriv_name, deriv_values)]):
            ax = axes[row][col]
            ax.plot(Z, y, color=f"C{row}")
            ax.set_title(title)
            ax.set_xlabel("z")
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axvline(0, color="black", linewidth=0.8)
            ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(SAVE_PATH)
    print(f"wrote {SAVE_PATH}")


if __name__ == "__main__":
    main()
