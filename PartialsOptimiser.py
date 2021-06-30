# If this were a lambda function, this would be the main file.

import PartialsCalculator as pc
from typing import List, Set, Dict, Tuple, Optional

def PartialOptimiser(AtR: List[float], Probability_AtR: List[float]) -> List[Tuple]:
    partials_perc_list = list(product(range(0, 101), repeat=len(AtR)))
    results_array = []

    for partial_tuple in partials_perc_list:
        # ----Optimise for speed
        # If there is not a closing partial, then profit is left on the table
        if (100 not in partial_tuple):
        continue
        # If there are more than one 100% partial, it's meaningless.
        if (partial_tuple.count(100) > 1):
            continue
       # If there are partials after a 100% partial, it's meaningless.
        if (100 in partial_tuple):
            i = partial_tuple.index(100)
            end = partial_tuple[i+1:]
            if (sum(list(end)) != 0):
                continue

        cumsum = pc.Caclulate_CumSum_Profit(partial_array_, at_R_, total_shares)
        total = pc.Total_Profit(Probability_AtR_, cumsum, total_shares)
        results_array.append((partial_tuple, total))
    
    sorted_results = sorted(results_array, key = lambda x: x[1], reverse = True)
    # return top 20 results
    return sorted_results[:20]