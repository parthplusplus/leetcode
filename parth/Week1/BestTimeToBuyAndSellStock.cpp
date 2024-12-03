class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int lowprice = prices[0];
        for(int i=1; i<prices.size(); i++)
        {
            if(prices[i] < lowprice)
            {
                lowprice = prices[i];
                continue;
            }
            profit = std::max(profit, prices[i] - lowprice);
        }
        return profit;
    }
};