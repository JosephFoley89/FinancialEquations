from decimal import Decimal
import pandas as pd
import numpy as np

#This is a calculation to determine the dollar return value from an investment.
def DollarReturns(soldPrice, boughtPrice, cashFlow):
    gain = soldPrice - boughtPrice + cashFlow
    print(f"${Decimal(gain).quantize(Decimal('1.00'))}")
    return gain
    
#This is a calculation to determin the percentage return from an investment.
def PercentageReturns(soldPrice, boughtPrice, cashFlow):
    gain = ((soldPrice - boughtPrice) / boughtPrice + (cashFlow / boughtPrice)) * 100
    print(f"{Decimal(gain).quantize(Decimal('1.00'))}%")
    return gain

#This is a calculation that determines the net income of a firm
def NetIncome(dividends, prevRetainedEarnings, currentRetainedEarnings):
    netIncome = dividends + (currentRetainedEarnings - prevRetainedEarnings)
    print(f"${Decimal(netIncome).quantize(Decimal('1.00'))}")
    return netIncome

#This is a calculation that determines a firm's FCFF where EBIT is the earnings
#before interest and taxes, CAPEX is the capital expenditure on PP&E and NWC is
#an increase in the net working capital.
def FreeCashToTheFirm(EBIT, taxRate, depreciation, CAPEX, NWC):
    FCFF = EBIT * (1 - taxRate) + depreciation - CAPEX - NWC
    print(f"${Decimal(FCFF).quantize(Decimal('1.00'))}")
    return FCFF
    
#--------------------------------------------------------Ratio Equations---------------------------------------------------------#
#--------------------------------------------------Liquidity Ratio Equations-----------------------------------------------------#

#This equation is responsible for returning a firm's current ratio.
def CurrentRatio(currentAssets, currentLiabilities):
    ratio = currentAssets / currentLiabilities
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This equation is responsible for returning a firm's quick ratio.
def QuickRatio(currentAssets, inventory, currentLiabilities):
    ratio = (currentAssets - inventory) / currentLiabilities
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This equation is responsible for returning a firm's Accounts Receivable Turnover ratio.
def ArTurnover(creditSales, accountsReceivable):
    ratio = creditSales / accountsReceivable
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is responsible for returning a firm's average collection period.
#It's worth mentioning that this function is dependant upon the ArTurnover function.
def AverageCollectionPeriod(creditSales, accountsReceivable):
    ratio = 365 / ArTurnover(creditSales, accountsReceivable)
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This equation is responsible for returning a firm's inventory turnover ratio where
#COGS is the cost of goods sold.
def InventoryTurnover(COGS, inventory):
    ratio = COGS / inventory
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is used to determine the days inventory is on hand and is dependent
#upon the InventoryTurnover function.
def DaysOnHand(COGS, inventory):
    ratio = 365 / InventoryTurnover(COGS, inventory)
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#--------------------------------------------------Efficiency Ratio Equations-----------------------------------------------------#

#This equation is used to generate the total asset turnover ratio.
def TotalAssetTurnover(sales, totalAssets):
    ratio = sales / totalAssets
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is used to generate the Fixed Asset Turnover ratio.
def FixedAssetTurnover(sales, fixedAssets):
    ratio = sales / fixedAssets
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This equation is used to generate the OIROI (Operating Income Return on Investment)
def OIROI(operatingIncome, totalAssets):
    ratio = operatingIncome / totalAssets
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#--------------------------------------------------Financial Ratio Equations-----------------------------------------------------#

#This equation is used to generate the debt ratio of a firm.
def DebtRatio(totalLiabilities, totalAssets):
    ratio = totalLiabilities / totalAssets
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is used to generate the IBDTC (Interest-bearing debt to total capital) ratio.
def IBDTC(interestBearingDebt, totalCapital):
    ratio = interestBearingDebt / totalCapital
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is used to generate the TIE (Times Interest Earned) ratio.
def TIE(EBIT, interestExpense):
    ratio = EBIT / interestExpense
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#This equation is used to generate the FLR (Financial leverage ratio).
def FLR(totalAssets, equity):
    ratio = totalAssets / equity
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#--------------------------------------------------Profitability Ratio Equations-------------------------------------------------#
#----------------------------------------------Investment Profitability Ratio Equations------------------------------------------#

#This function is used to return a firm's return on asset (ROA) ratio. This is dependent upon the NetIncome function.
#Previous and current refer to retained earnings.
def ROA(dividends, previous, current, totalAssets):
    ratio = NetIncome(dividends, previous, current) / totalAssets
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This function is used to return a firm's return on equity (ROE) ratio. This is dependent upon the NetIncome fucntion.
#Previous and current refer to retained earnings.
def ROE(dividends, previous, current, ownersEquity):
    ratio = NetIncome(dividends, previous, current) / ownersEquity
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio
    
#---------------------------------------------Sales-Based Profitability Ratio Equations-----------------------------------------#

#This function is used to return a firm's Gross Margin ratio.
def GrossMargin(sales, COGS):
    ratio = (sales - COGS) / sales
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    
#This funtion is used to return a firm's Operating Margin ratio.
def OperatingMargin(EBIT, sales):
    ratio = EBIT / sales
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    
#This function is used to return a firm's net margin ratio and is dependent upon the 
#NetIncome function. Previous and current refer to retained earnings.
def NetMargin(dividends, previous, current, sales):
    ratio = NetIncome(dividends, previous, current) / sales
    print(f"{Decimal(ratio).quantize(Decimal('1.000'))}")
    return ratio

#This function is used to return the ROE via the DuPont Decomposition and, as a result, 
#is dependent upon the NetMargin, TotalAssetTurnover, and FLR functions.
def DuPontDecomposition(dividends, previous, current, sales, totalAssets, equity):
    ROE = NetMargin(dividends, previous, current, sales) * TotalAssetTurnover(sales, totalAssets) * FLR(totalAssets, equity) 
    print(f"{Decimal(ROE).quantize(Decimal('1.000'))}")
    return ROE

#------------------------------------------------------End of Ratio Equations----------------------------------------------------#

#This formula is used to determine the future value of present cash.
def FutureValue(presentValue, interestRate, years):
    futureValue = presentValue * (1 + interestRate) ** years
    print(f"${Decimal(futureValue).quantize(Decimal('1.00'))}")
    return futureValue

#This formula is used to determine the present value of future cash.
def PresentValue(presentValue, interestRate, years):
    presentValue = presentValue / (1 + interestRate) ** years
    print(f"${Decimal(presentValue).quantize(Decimal('1.00'))}")
    return presentValue
    
