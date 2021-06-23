import PartialsCalculator as pc
import unittest

class Test_CumSum(unittest.TestCase):
    def test_cumsum_one(self):
        """
        Function returns an array of cumsum values.
        Tests that simple values are correct
        """
        partials = [50, 100]
        at_R = [2, 3]
        total_shares = 1000
        result = pc.Caclulate_CumSum_Profit(partials, at_R, total_shares)
        self.assertEqual(result[0], 1000)
        self.assertEqual(result[1], 2500)

    def test_cumsum_two(self):
        """
        Function returns an array of cumsum values.
        Tests that complex values are correct
        """
        partials = [10, 30, 30, 100]
        at_R = [2, 2.5, 4, 5.5]
        total_shares = 1000
        result = pc.Caclulate_CumSum_Profit(partials, at_R, total_shares)
        self.assertEqual(result[0], 200)
        self.assertEqual(result[1], 875)
        self.assertEqual(result[2], 1631)
        self.assertEqual(result[3], 4056.5)

class Test_CalculateTotalProfit(unittest.TestCase):
    def test_totalprofit_one(self):
        """
        Function calculates total profit over 
        1000 trades given probability of reaching R.
        Tests simple value is correct
        """
        partials = [50, 100]
        at_R = [2, 3]
        total_shares = 1000
        probability_atR = [80, 30]
        cumsum = pc.Caclulate_CumSum_Profit(partials, at_R, total_shares)
        result = pc.Total_Profit(probability_atR, cumsum, total_shares)
        self.assertEqual(result, 1050000)

    def test_totalprofit_two(self):
        """
        Function calculates total profit over 
        1000 trades given probability of reaching R.
        Tests complex value is correct
        """
        partials = [10, 30, 30, 100]
        at_R = [2, 2.5, 4, 5.5]
        total_shares = 1000
        probability_atR = [70, 30, 15, 5]
        cumsum = pc.Caclulate_CumSum_Profit(partials, at_R, total_shares)
        result = pc.Total_Profit(probability_atR, cumsum, total_shares)
        self.assertEqual(result, 277175)



if __name__ == "__main__":
    unittest.main()
