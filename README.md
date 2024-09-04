# Kalman-Information-Filter-Implementation

This is where we have the implementation of the kalman filter, a simple algorithm used for linear systems to filter noisy measurements and give accurate estimates. This implementation is a small dimensional example, which estimates and filters measurements for a 2 dimensional vector. Due to the structure of this algorithm, with equations represented in matrix form, this algorithm is straightforward to implement for higher dimensions. 

Kalman filters are very powerful and effective tools that engineers and scientists are able to apply for systems where both observations and measurements of a process are not completely deterministic. My first exposure to this tool came about during a research group I was a part of where we were attempting to study the possibility of developing and using a laser interferometer that would be sent into orbit to observe exoplanets without any worry of atmospheric interference. A system like this must be extremely stable, and as such, control methods must be in place to counterbalance internal and external factors that mess with the stability of the laser.

Kalman filters come in all different flavors for different purposes, (extended kalman filters (EKFs) and unscented kalman filters (UKFs) use first and second order derivatives to approximately estimate non-linear systems)


