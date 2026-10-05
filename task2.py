import matplotlib.pyplot as plt
import numpy as np

rng=np.random.default_rng()

def generate_inverse_exponential(N, mu):
    P = rng.uniform(0, 1, N)
    tau = -np.log(1-P) / mu
    return tau

def main_function():
    N = 1000
    T = 100
    mu = N / T
    tau = generate_inverse_exponential(N, mu)

    plt.figure(figsize=(8, 5))
    plt.hist(tau, bins=30, density=True, alpha=0.6, color='orange', label='Inversely sampled tau')

    tau_theoretical = np.linspace(0,np.max(tau), 100)
    p_tau = mu * np.exp(-mu * tau_theoretical)
    plt.plot(tau_theoretical, p_tau, "r-", linewidth=2, label=r"Theortical: $p(\tau) = \mu e^{-\mu\tau}$")

    plt.xlabel(r'Time Interval $\tau$')
    plt.ylabel(r'Probability Density $p(\tau)$')
    plt.title('Probability Density via Inverse Transform Sampling (Task 2)')
    plt.legend()
    plt.grid(True)
    plt.savefig("task2_distribution.png")
    plt.show()

main_function()