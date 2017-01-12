# spanishoptions
I have analysed the options traded (with a non-null volume) in the Spanish stock market. I obtained the DATA through MEFF archives .

I want to portray an accurate description of the different variables and target features for an option and test the best predictors for the success of an option, with three KPI in mind: execution, net profit and ROI.




My first batch of data will be for the call options traded during month of November 2014 with a maturity date previous to November 2016. Later in the month, I will publish the results for the same period with put options. I will also test my results with other months in future posts.  

***

This is the introductory post to my series on Spanish options.

INDEX:

Descriptive, Correlations and Black Swans

By Companies

By Sectors

A Graphical Walk

Forecasting

***

REFERENCE GUIDE:

Targets:

NET (diff between máximum stock price and strike price + premium).
ROI (NET divided by the premium price).
TRIGGER (categorical variable. 1=máximum price > strike price + premium.)
Known variables:

DELTA, and VOLATILITY are provided by MEFF.
DAYS (days between the selling of the option and the strike date).
PREMIUM (percentage of the premium in relation to the strike price).
MAX (peak price of the stock before the maduration date).
1ySTD, 6mSTD, 3mSTD(1-year, 6-month,3-month past standard deviations of the stock).
Unknowable variables:

GAIN (price variation between maturity date and trading day of the stock).
STD (standard deviation between maturity date and trading day of the stock).
Categorical variables:

HIGH DELTA, HIGH PREMIUM, HIGH VOL, DURATION: five-degree (1 to 5) categories by quantiles.

I will work with 3 final tables: disaggregated, by company and by sector.

 

Disclaimer:

This project is merely an experiment, as it takes the peak quote of a stock before their maturity date as a reference. It would certainly take a wizard to know when the price of a stock has reached its peak.   It is not the goal of this study to analyse the profitability of the stock options, but to question their best predictors.

 

As a second disclaimer, this shouldn’t be tested through statistics independence criteria as the future of an option is path dependant to their underlying stock. Obviously, the first criterium when buying an option is choosing the company buy this study will try to fine tune the election of the option.

Thirdly, commssions are not taken into account, as their impact is greatly related to the initial investment. 
