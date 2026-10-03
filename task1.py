import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()



def generate_poisson_intervals(N,T):
    t_events=np.sort(rng.uniform(0, T, N))
    tau = np.diff(t_events)
    return tau

def main_function():
    N = 1000
    T = 100

    tau = generate_poisson_intervals(N, T)

    mu = N/T
    print(f"Calculated term for mu: {mu}")

    plt.figure(figsize=(8,5))
    plt.hist(tau, bins=30, density=True, alpha=0.6, color='g', label='Simulated tau')

    tau_theoretical = np.linspace(0, np.max(tau), 100)
    p_tau = mu * np.exp(-mu * tau_theoretical)
    plt.plot(tau_theoretical, p_tau, "r-", linewidth=2, label=r"Theoretical: $p(\tau) = \mu e^{-\mu\tau}$",
    )

    plt.title("Probability Density of Time Intervals (Task 1)")
    plt.xlabel(r"Time interval $\tau$")
    plt.ylabel(r"Probability density $p(\tau)$")
    plt.legend()
    plt.grid(True)
    plt.savefig("task1_distribution.png")
    plt.show()


main_function()