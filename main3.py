import matplotlib.pyplot as plt

import numpy as np
 

Q = np.array([[1.0,0.1],[0.1,1.0]]) #process noise variance

R = np.array([[16]]) #observation noise covariance

F = np.array([[1,0.1],[0,1]]) # state transition model

H = np.array([[0.5,0.5]]) #observation model

P = np.array([[0,0],[0,0]]) #a priori matrix model

T = 100

x = np.zeros((T,2)) #true state

z = np.zeros((T,1)) #observation based on true state x and control u

x_hat = np.zeros((T,2)) #updated true state
 

for i in range(T-1):

    x[i+1] = F.dot(x[i]) + np.random.multivariate_normal(np.zeros(2), Q) # true state vector is populated with state transitions with gaussian noise (a priori estimate) x_k|k-1

    z[i+1] = H.dot(x[i+1]) + np.random.multivariate_normal(np.zeros(1), R) # observation vector is populated with state vector applied to the observation model with gaussian observation noise

###

#YOUR KALMAN FILTER CODE GOES HERE AND POPULATES x_hat BASED ON z

###

def Kalman_Filter(z,Q,H,F,x,P):
    x_pred = F.dot(x) #we are making a prediction using our previous estimate
    P_pred = F.dot(P).dot(np.transpose(F))+ Q #we are making covariance prediction with state transition and processing noise (a priori estimate)
    S = H.dot(P_pred).dot(np.transpose(H))+R #innovation covariance (a priori estimate given observation model and process noise)
    K = H.dot(P_pred).dot(np.linalg.inv(S)) #kalman gain--
    x_hat = x_pred + K.dot(z - H.dot(x_pred)) #the updated estimate is calculated using the true state added with the product of the kalman gain and the difference bet
    P_hat = (np.identity(2) - K.dot(H)).dot(P_pred) #making the updated covariance to use in next iteration
    return (x_hat, P_hat)

def Information_Filter(z,Q,H,F,R,x,P):
    x_pred = F.dot(x) #we are making a prediction using our previous estimate
    P_pred = F.dot(P).dot(np.transpose(F))+ Q #we are making covariance prediction with state transition and processing noise (a priori estimate)
    S_pred = np.linalg.inv(P_pred) #defining information matrix
    y_pred = S_pred.dot(x_pred) #constructing the information vector
    y_hat = y_pred + np.transpose(H).dot(np.linalg.inv(R)).dot(z) #information vector updated using the observation
    S_hat = S_pred + np.transpose(H).dot(np.linalg.inv(R)).dot(H) #information matrix updated using lower bound for information of observation noise
    P_hat = np.linalg.inv(S_hat) #updated covariance matrix
    x_hat = P_hat.dot(y_hat) #new updated estimate for x_hat
    return (x_hat, P_hat)

for i in range(T-1):
    P = Information_Filter(z[i+1],Q,H,F,R, x_hat[i],P)[1] #updated covariance model
    x_hat[i+1] = Information_Filter(z[i+1],Q,H,F,R,x_hat[i],P)[0] #x_hat is populated with the new observation, state, and covariance for estimation

est = x_hat.dot(np.transpose(H))

#plt.plot(x[:,0], "r-", label="x_0")

#plt.plot(x_hat[:,0], "r--", label="estimated x_0")

#plt.plot(x[:,1], "b-", label="x_1")

#plt.plot(x_hat[:,1], "b--", label="estimated x_1")

plt.plot(z, "g--", label="measurement = 0.5(*x_0 + x_1) + noise")

plt.plot(est, "g-", label="Estimate")

plt.legend()

plt.show()

