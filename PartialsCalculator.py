from functools import reduce
import numpy as np

# 70% of trades get to 2R
# 60% get to 3R
# 10% get to 4R

# This assumes SL to BE after first partial.
# We have 100 shares and $1 risk on the position. This means that the share/$ risk is $100, so 2R = $200 etc.
# We take 30% of our position at 2R. This is 60 dolls out of 200, leaving $140 on the table and 70 shares.. However, out of 1000 trades, only 70% get to 2R. That means 700 * 60 = 42,000 dolls realised, 300 * 100 = 30,000 dolls lost, net 12,000 profit 
# (in other words, 300 trades out of the 1000 don't make it to 2R and go back to -1R loss).
# Of those 700 that get to 2R, only 14.28% fail to get to 3R (700 - 600) / 700. The profit of a 60% partial at 3R is 126 dolls. If the trade gets this far, then you will have 186 dolls realised.
# This means that out of 700 profitable trades, 14.28% (100 trades) make only 60 dolls, and 85.72% (600 trades) make 126 dolls. 100 * 60 = 6000, 600 * 126 = 75,600, sum = 81,600. Again, you would lose 30,000 from those that didnt make 2R, and so net is 51,600 dolls. If we were to stop here, then that would be it.
# If we have more than two partials, we need to consider all of the partial probabilities together. So we have 700/1000 make it to 2R, 600/1000 make it to 3R, and 100/1000 make it to 4R. So 85.72% of trades that made it to 2R make it to 3R, and 16.67% of trades that made it 3R will make it to 4R. 
# So previously, we had 600 trades that got to 3R. 16.67% of these (100/600), 100 trades, will make it to 4R. 
# so now: 100 trades make 60 dolls, 500 trades make 186 dolls, and 100 trades make 298 dolls, 300 trades lose 100 dolls = 128,800 gross profit, 98,800 net profit 

# so it goes: 
# 6000
# 93000
# 29800
# gross = 128,800
# net = 98,800

# So what we need to do is firstly calculate the profit according to where you are taking the partials. 
# Then we need to calculate the profit according to probability, as described above. 
# Then we need to adjust the partials, and calculate the profit.
# Then we need to calculate the profit according to probability, again.
# This will generate a range of values for the net profit, each should be stored as a tuple, which has the first element as an array of partial percentages, the second as the NP

def Caclulate_CumSum_Profit(Partials, AtR):
    total_shares = 1000
    remaining_shares = total_shares
    total_profit = 0
    profit_array = []
    for idx, partial in enumerate(Partials):
        # Percentage of shares to close
        shares_to_close = remaining_shares * (partial / 100)
        # print(shares_to_close)
        remaining_shares = remaining_shares - shares_to_close
        profit = shares_to_close * AtR[idx]
        profit_array.append(profit)
        total_profit += profit
    return np.cumsum(profit_array)

# ---------Now we can calculate profit according to probability of outcome across 1000 trades

# Out of 1000 trades, 70% are 2R, 60% are 3R, 30% are 4R, and 5% are 6R. This means that of the 700 trades that reach 2R, 600 will go on to be 3R trades. That means that 
# only 100 trades will be purely 2R trades (2R, then back to BE). Of the 600, 300 will go on to be 4R, leaving 300 and 3R. Finally, 50 will be full R trades, so 250 will be left at 4R
def Total_Profit(ProbabilityAtR, CumSum):
    no_of_trades = 1000
    no_of_trades_AtEachR = []
    for probability in ProbabilityAtR:
        # Using the probability, calculate the number of trades that will go through each R.
        no_of_trades_AtEachR.append(no_of_trades * (probability / 100))

    # Calculate the number of trades that only hit each R, then turn around and go to BE.
    no_of_winners_AtR = []
    for idx, no_of_trades in enumerate(no_of_trades_AtEachR):
        # Out of 1000 trades, 70% are 2R, 60% are 3R, 30% are 4R, and 5% are 6R. This means that of the 700 trades that reach 2R, 600 will go on to be 3R trades. That means that 
        # only 100 trades will be purely 2R trades (2R, then back to BE). Of the 600, 300 will go on to be 4R, leaving 300 and 3R. Finally, 50 will be full R trades, so 250 will be left at 4R
        # The last element for number of trades doesn't need updating.
        # If the probabilities were 70, 60, 10, and we had 1000 trades, then the last will always be equal to probability * no_of_trades (= 100)
        if idx == len(no_of_trades_AtEachR) - 1:
            no_of_winners_AtR.append(no_of_trades_AtEachR[-1])
            # print(no_of_winners_AtR)
            break
        no_of_winners_AtR.append(no_of_trades - no_of_trades_AtEachR[idx + 1])

    # Now simply multiply the no_of_winners_AtR by the realised profit at each R. This will tell you how much money each trade that got to that R and turned around to BE
    # made. For example, if a trade that gets to 2R and drops 30%, then hits BE will make 0.6R, then 1000 of these will make 600R. 
    x = []
    for idx, t in enumerate(CumSum):
        # print(t)
        # print(no_of_winners_AtR[idx])
        # print("_")
        x.append(t * no_of_winners_AtR[idx])
    return reduce((lambda a, b: a + b), x)

# Divide by total shares to get realised R
def total_r(total_profit, risk):
    return total_profit / risk





