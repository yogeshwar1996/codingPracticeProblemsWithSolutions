# Statement
Bank has a simple policy for warning clients about possible fraudulent account activity.<br>
If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days

Given the transactions list of `n` days with amounts transferred and `d` (the trailing days). Find how many notifications were sent.

Example

d=3
n = 5
transactions = [10,20,30,40,50]

Result - 1 notification when user spent 40 because the 3 trailing days amount spent was 10,20,30 whose median is 20 and 
On the 4th day 40 was spent which is >= 2*median i.e 2*20