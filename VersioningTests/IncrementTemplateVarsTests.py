import unittest
from Versioning.IncrementTemplateVars import *

class Test_IncrementTemplateVars(unittest.TestCase):
    sampleVar = "{compile:0}"
    sampleVarOut = "{compile:1}"
    sampleVarProduct = "1"
    sampleVar2 = "{build:111}"
    sampleVarOut2 = "{build:112}"
    sampleVarProduct2 = "112"
    unmodifiedText = " SomeText "

    def test_incrementAllVars_HasOneVar_CheckIncrement(self):
        incr = IncrementTemplateVars()
        incr.setSource(self.sampleVar)
        incr.build()
        expect=self.sampleVarOut
        self.assertEqual(expect,incr.getTemplate())
        

    def test_incrementAllVars_HasOneVarAndRawText_CheckNotChangeRawText(self):
        incr = IncrementTemplateVars()
        incr.setSource(self.sampleVar + self.unmodifiedText)
        incr.build()
        expect=self.sampleVarOut + self.unmodifiedText
        self.assertEqual(expect,incr.getTemplate())


    def test_incrementAllVars_HasTwoVar_CheckIncrementBoth(self):
        incr = IncrementTemplateVars()
        incr.setSource(self.sampleVar + self.unmodifiedText+ self.sampleVar2)
        incr.build()
        expect=self.sampleVarOut + self.unmodifiedText + self.sampleVarOut2
        self.assertEqual(expect,incr.getTemplate())


    def test_incrementAllVars_HasTwoVar_CheckCorrectChangeProduct(self):
        incr = IncrementTemplateVars()
        incr.setSource(self.sampleVar + self.unmodifiedText+ self.sampleVar2)
        incr.build()
        expect=self.sampleVarProduct + self.unmodifiedText + self.sampleVarProduct2
        self.assertEqual(expect,incr.getProduct())

if __name__ == '__main__':
    unittest.main()
