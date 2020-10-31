import numpy as np
import scipy.stats

def sampleMean( data ) :
  #Your code to calcualte the sampe mean should go here
  
def criticalRange( mu, sigma, N ) : 
  # Your code to calculate the critical region should go here
  lower = 
  upper = 
  return lower, upper
  
def hypothesisTest( data, mu, sigma ) : 
  l, u = criticalRange( mu, sigma, len(data) )
  # You need to use the l and u values that are returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  
  
data = np.loadtxt("mydata.dat")
print("Null hypothesis: the data points in mydata.dat are all samples from a ")
print("normal random variable with expectation 4 and variance 9")
print("Alternative hypothesis: the data points in mydata.dat are not all samples from a ")
print("normal random variable with expectation 4 and variance 9")
print( hypothesisTest( data, 4, 3 ) )
  
