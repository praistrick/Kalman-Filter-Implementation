# Kalman-Information-Filter-Implementation

Here I have the implementation of the kalman filter, a simple algorithm used for linear systems to filter noisy measurements and give accurate estimates. This implementation is a small dimensional example, coded in Python, which estimates and filters measurements for a 2 dimensional vector. Due to the structure of this algorithm, with equations represented in matrix form, this algorithm is straightforward to implement for higher dimensions and more complex dynamical systems. 

## Kalman Filters
The Kalman filter is a very powerful and effective tool that engineers and scientists are able to apply for systems where both observations and measurements of a process are not completely deterministic, requiring an estimation of the true state after the elimination of noise. From navigation, to weather forecasting, to signal processing, Kalman filters have a very wide range of uses in all different fields of science and engineering. My first exposure to this tool came about during a research group I was a part of, where we were attempting to study the possibility of developing and using a laser interferometer that would be sent into orbit to observe exoplanets without any worry of atmospheric interference. A system like this must be extremely stable, and as such, control methods must be in place to counterbalance internal and external factors that mess with the stability of the laser.

Kalman filters are optimal for estimating linear systems with Gaussian noise, but come in all different flavors for different purposes, (extended kalman filters (EKFs) and unscented kalman filters (UKFs) use first and second order derivatives to approximately estimate non-linear systems, particle filters use Bayesian Inference for non-linear systems, etc) but their structures all revolve around the same sequence of steps.

Kalman filters work on recursive estimation and thus need several defined factors, which may or may not be updated after each iteration. This includes a state space model, observation model, expected covariance matrices for each of those models, as well as measured values and true values. Depending on the application, an additional control model and control vector which acts on the model may be implemented to hold the estimated true value around some certain value. 

### State Prediction
After obtaining the initial true state values, first step is to make a prediction of the next state and covariance matrix conditioned on the current state space model and previous estimates of the true values for the state and covariance. 

### Kalman Gain Calculation
The next step is to use these (priori) estimates to update the system, given an observation. This is done by calculating the difference between the current measurement and the estimated state applied to an observation model. From there, the observation model is applied to the estimated covariance (called the updated covariance), and this, along with the initial prediction and the observation model are combined to calculate the Kalman gain. This a matrix which determines how "big" of a correction is needed (for example, if the estimated value for our state is far from our measurement with relatively small covariances between them, the Kalman gain will be large to correct for the large error between the state and measurement. 

### State Update
Finally, using the Kalman gain, we can calculate the corrected (posterior) estimates of the true state and state covariance. These values continuously feed back into the algorithm, being used as initial "true states" to then calculate the updated values for the next state until the end of the system's measurements. 

### Assumptions
For a system to be effective for estimation by an ordinary Kalman filter, a few assumptions need to be made, namely, observation and measurement noise is independent, approximately normal, with mean 0, and the dynamic observation/state space models are linear. 

In this implementation, I demonstrate the ordinary Kalman Filter I have just described as well as the Information Filter, which is a slight modification of the Kalman filter, that uses the statistical quantity of information to update and estimate state values (the Information/Fisher Matrix is calculated by the inverse of the state covariance matrix, assuming that the variance of the states are as low as possible by the Cramer-Rao Bound). While there are libraries out there that support these kinds of filters, by implementing it directly from its defining equations, the workings of the Kalman filter are demystified and are able to be more readily understood and thus effectively applied to real world problems.
