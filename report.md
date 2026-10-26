Group report 

# Poisson-Kac Task 1

In this task, we simulate N random event times distributed uniformly within a time interval [0,T] to model velocity reversal events in a Poisson-Kac process. We calculate the time intvervals $\tau$ between successive reversal events and demonstrate that their probability density function p($\tau$) follows an exponential distribution given by $p(\tau) = \mu e^{-\mu\tau}$. Here the rate parameter is defined as  $\mu = N/T$.

## Layout of the algorithm, functions to be created

The code for this task relies on numpy to generate random numbers and to make array operations. It also uses matplotlib.pyplot to visualise. The two main functions of this task are:

      def generate_poisson_intervals(N,T):
            # It generates N random event times in the interval [0,T]
            # and sorts them. The function also calculates the time
            # differences tau between consecutive events.
            return tau

      def main_function():
            # This function ist used to coordinate the simulation, to
            # calculate mu, plot the histogram against the
            # theoretical distribution and to save the resulting
            # figure.


## How to run the code

To run the code, you need to install numpy and matplotlib in your active Python environment and execute:

      python3 task1.py

N and T are predefined. So you don't need to define them.

## Resulting files

task1_distribution.png: This is a generated figure which shows the comparison between the histogram of simulated time intervals $\tau$ and the theoretical exponantial distribution curve.

## Successful tests

It has been verified that all generated event times are within the interval between 0 and 1.
We can confirm that all calculated time intervals $\tau$ are positive numbers.
The area under the probability density histogram normalizes to 1 and aligns with the theoretical rate $\mu = N/T$. This was checked numerically and visually.

## Problems

Initial environment path conflicts, package resolution issues (numpy/matplotlib) within VS Code, and minor import errors (matplotlib vs matplotlib.pyplot). All issues were successfully resolved.

## Results (speed tests etc.)

The resulting plot clearly shows that the theoretical exponantial decay curve is closely followed by the simulated data points, validation the relation $\mu = N/T$.






# Poisson-Kac Task 2

Develop an algorithm which uses the inverse transform sampling method to generate random time intervals $\tau$ for a given rate $\mu$. The density of those time intervals corresponds to the exponential distribution $p(\tau) = \mu e^{-\mu\tau}$. Starting from the analytically calculated cumulative distribution function $P(\tau) = 1 - e^{-\mu\tau}$ and uniformly distributed random numbers $P \in [0,1]$, $N$ values are generated using the formula $\tau = -\ln(1-P)/\mu$ and visually verified.

## Layout of the algorithm, functions to be created

The code for this task relies on numpy to generate random numbers and to make array operations. It also uses matplotlib.pyplot to visualise. The two main functions of this task are:

      def generate_inverse_exponential(N,mu):
            # It generates N uniformly distributed random numbers
            # in the interval [0,1] and applies the inverse transform 
            # formula tau = -ln(1 - P) / mu.
            return tau

      def main_function():
            # This function ist used to coordinate the simulation, to
            # calculate mu, plot the histogram against the theoretical
            # distribution and to save the resulting figure.

## How to run the code

To run the code, you need to install numpy and matplotlib in your active Python environment and execute:

      python3 task2.py

N and T are predefined. So you don't need to define them.

## Resulting files

task2_distribution.png: This is a generated figure which shows the comparison between the histogram of inversely sampled $\tau$ values and the theoretical exponantial probability density curve.

## Successful tests

Verified that all generated random probabilities P lie within the interval between 0 and T.
Confirmed that all calculated $\tau$ values match the expected theoretical decay rate $\mu$.
Checked visually that the histogram matches the analytical curve $p(\tau) = \mu e^{-\mu\tau}$.

## Problems

No problems encountered; the inverse transform sampling method directly produced accurate distributions that match Task 1.

## Results (speed tests etc.)

The resulting plot clearly confirms that generating time intervals via the inverse cumulative distribution function can reproduce Poisson-Kac interval statistics successfully.







# Poisson-Kac Task 3

In this task, we simulate a 1D Poisson-Kac process trajectory $x(t)$ of an atom starting at $t=0$ at position $x(0)=0$ with initial velocity $v=s$. Velocity reversal events occur at random time intervals $\tau_i = -\ln(1-P)/\mu$, where $P \sim \text{Uniform}(0, 1)$ and $\mu$ is the event rate. Between reversal events, the atom moves at constant speed $s$ with alternating directions ($v \to -v$). We compare the event-driven discrete trajectory at times $t = 0, \tau_1, \tau_1+\tau_2, \dots$ with an equidistantly sampled trajectory evaluated at fixed time steps $t_j = j \Delta t$ (with $\Delta t \ll \mu^{-1}$) to validate the algorithm.

## Layout of the algorithm, functions to be created

The code relies on numpy for random number generation and array manipulation, and matplotlib.pyplot for visual validation. The two main functions of this task are:

      def generate_event_trajectory(N, rate_mu, speed_s):
            # Generates N random time intervals tau using inverse transform sampling,
            # tracks velocity direction reversals (v -> -v), and calculates the 
            # exact particle position x(t) at each event time.
            return t_events, x_events

      def interpolate_equidistant_trajectory(t_events, x_events, speed_s, dt):
            # Constructs the continuous trajectory x(t) at fixed, regular time
            # intervals t_j = j * dt by performing piece-wise linear interpolation
            # between reversal events.
            return t_grid, x_grid

      def main_function():
            # Sets parameters (N=40, mu=10, s=1, dt=0.25/mu), coordinates the
            # trajectory generation, overlays both representations on a single plot,
            # and saves the resulting figure.

## How to run the code

To run the code, you need to install numpy and matplotlib in your active Python environment and execute:

      python3 task3.py

Parameters ($N = 40$, $\mu = 10$, $s = 1$, and $\Delta t = 0.25/\mu$) are predefined inside the code.

## Resulting files

task3_trajectory.png: This is a generated figure which shows the visual overlay of the discrete reversal events (open circles) and the equidistantly sampled trajectory (dotted line with points).

## Successful tests

It has been verified that all calculated intervals $\tau_i$ strictly follow the prescribed distribution $\tau = -\ln(1-P)/\mu$ and remain positive.
We can confirm that velocity alternates correctly ($+s, -s, +s, \dots$) after every event.
The continuous piecewise linear trajectory constructed at regular intervals $t_j = j \Delta t$ passes directly through all event positions $(t_{\text{event}}, x_{\text{event}})$, confirming the validity of the interpolation algorithm both numerically and visually.

## Problems

Handling boundary conditions between discrete event steps during continuous time interpolation required precise interval lookup logic (np.searchsorted). Potential floating-point inaccuracies when matching fixed grid times $t_j$ with event times were successfully resolved.

## Results (speed tests etc.)

The generated plot demonstrates exact agreement between the continuous piecewise linear path evaluated at regular time steps $\Delta t$ and the discrete reversal event locations, verifying the correctness of the spatial velocity-reversal algorithm.