import unittest
from processor import Processor

class TestProcessorMethods(unittest.TestCase):
    def testLuhncheckTrue(self):
        myProcessor = Processor()
        self.assertEqual(myProcessor.luhncheck("4111111111111111"), True)

    def testLuhncheckFalse(self):
        myProcessor = Processor()
        self.assertEqual(myProcessor.luhncheck("1234567890123456"), False)

    def testAddNegative(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "-$50")
        self.assertEqual(myProcessor.myDB["James"].limit,"error")

    def testAddPositive(self):
        myProcessor = Processor()   
        myProcessor.addCard("James", "5454545454545454", "$50")
        self.assertEqual(myProcessor.myDB["James"].limit, 50)

    def testChargeNegative(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.chargeCard("James", "-$50")
        self.assertEqual(myProcessor.myDB["James"].balance, 0)

    def testChargePositive(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.chargeCard("James", "$50")
        self.assertEqual(myProcessor.myDB["James"].balance, 50)

    def testCreditPositive(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.creditCard("James", "$50")
        self.assertEqual(myProcessor.myDB["James"].balance, -50)

    def testCreditNegative(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.creditCard("James", "-$50")
        self.assertEqual(myProcessor.myDB["James"].balance, 0)

    def testOverCharge(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.chargeCard("James", "$100")
        self.assertEqual(myProcessor.myDB["James"].balance, 0)

    def testMultipleNamedUsers(self):
        myProcessor = Processor()
        myProcessor.addCard("James", "5454545454545454", "$50")
        myProcessor.chargeCard("James", "$10")
        myProcessor.addCard("James", "5454545454545454", "$50")
        self.assertEqual(myProcessor.myDB["James"].balance, 0)
        


if __name__ == '__main__':
    unittest.main()