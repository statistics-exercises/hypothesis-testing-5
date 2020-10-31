import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_sampleMean(self) :
        self.assertTrue( np.abs( sum(data)/len(data) - sampleMean(data) ) <1e-7, "your sampleMean function does not calculate the sample mean correctly" )
    
    def test_criticalRange(self) : 
         l = scipy.stats.norm.ppf(0.025,loc=4,scale=3/np.sqrt(200) )
         u = scipy.stats.norm.ppf(0.975,loc=4,scale=3/np.sqrt(200) )
         lll, uuu = criticalRange( 4, 3, len(data) )
         self.assertTrue( np.abs(l-lll)<1e-4, "the lower bound for the critical region has been computed incorrectly")
         self.assertTrue( np.abs(u-uuu)<1e-4, "the upper bound for the critical region has been computed incorrectly" )

    def test_hypothesisTest(self) : 
        hhh = hypothesisTest( data, 4, 3 ) 
        self.assertTrue( hhh=="the null hypothesis is rejected in favour of the alternative", "the hypothesisTest function returns the wrong sentence"  )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not contain an if statement" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("there is insufficient evidence to reject the null hypothesis")>0, "the hypothesis test function does not contain the string there is insufficient evidence to reject the null hypothesis.  This string should be present and output when the sample mean falls outside the critical region." ) 
