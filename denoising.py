import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sp


#Matplotlib is a library that enables functionalities that
#           helps us to visualize the signals

#Numpy is a library that deals with complex mathematical calculations
#       and constants that are required in forming and manipulating signals.

#Scipy is a Scientific library that enables funnctionalites that are required
#       for analyzing the signal and other Digital Signal processing methods.

n=int(input("Enter the no of elements in the signal: "))
inputSignal=[int(input("Enter element {}: ".format(i))) for i in range(n)]

# the signal is extended with some zeros on each side for a better interpretation.
extendedInput=np.hstack([np.zeros(5), inputSignal, np.zeros(5)])

#plotting the extended input signal on the graph.
plt.plot(extendedInput,label="Input Signal")

# Random White Noise is being added to the signal to test the filtering.
signalwithNoise = np.random.uniform(0, 2, 10 + len(inputSignal)) * (min(inputSignal) + max(inputSignal)) / 2 + extendedInput

#The  Signal with added Noise(The recieved signal) is being plotted.
plt.plot(signalwithNoise, label="Signal with Noise(Recieved Signal)")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Transmitted and Recieved Signals')
plt.axhline(0, color='black')
plt.legend()
plt.ylim(min(inputSignal) - 3, max(inputSignal) + 3)
plt.grid()
plt.show()



invertedSignal = inputSignal[::-1] # This is the inverse signal of the original signal

#lfilter is a filtering techinque similar to matched filters where the signal
#     with noise is beign correlated with the inverse of the inital signal.
signalafterFiltering = sp.lfilter(invertedSignal, 1, signalwithNoise)[::-1] / 10

# Signal with Noise(Recieved Signal) is plotted for reference.
plt.plot(extendedInput,label="Initial Signal without noise")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Extended Input Signal")
plt.plot(signalafterFiltering, label="Signal after Filtering")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal in Noise after Matched Filtering')
plt.axhline(0, color='black')
plt.legend()
plt.grid()
plt.show()