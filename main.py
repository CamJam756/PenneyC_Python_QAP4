# Comment like a pro.
# Author: Cameron Penney
# Date Written: March 20th, 2023

# Imports.
import datetime

# Open the defaults file, reads and formats the values.
next_policy_num = 1944
basic_prem = 869.00
discount_add_cars = .25
cost_extra_lia_cov = 130.00
cost_glass_cov = 86.00
cost_loaner_car = 58.00
hst_rate = .15
process_fee = 39.99

f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(next_policy_num)))
f.write("{}\n".format(str(basic_prem)))
f.write("{}\n".format(str(discount_add_cars)))
f.write("{}\n".format(str(cost_extra_lia_cov)))
f.write("{}\n".format(str(cost_glass_cov)))
f.write("{}\n".format(str(cost_loaner_car)))
f.write("{}\n".format(str(hst_rate)))
f.write("{}\n".format(str(process_fee)))
f.close()

# Calculations/Statements.
while True:

    CustFirstName = input("Enter the customers first name: ").title()
    CustLastName = input("Enter the customers last name: ").title()
    Address = input("Enter the customers address: ")
    City = input("Enter the customers city: ")
    Province = input("Enter the customers province: (XX) ")
    PostalCode = input("Enter the customers postal code: (XXXXXX)")
    CusPhoneNum = input("Enter the customers phone number: (XXX-XXX-XXXX) ")
    NumberCarsInsured = int(input("Enter the number of cars being insured: "))
    ExtraLia = input("Enter if you would like extra liability up to $1,000,000? (Y / N) ").upper()
    GlassCov = input("Enter if you would like glass coverage? (Y / N) ").upper()
    OptLoanCar = input("Enter if you would like a loner car? (Y / N) ").upper()
    PayOption = input("Enter the payment option you would like Full or Monthly? (F / M) ").upper()

    if NumberCarsInsured == 1:
        InsurePrem = basic_prem
    elif NumberCarsInsured > 1:
        InsurePrem = basic_prem + (NumberCarsInsured - 1) * (basic_prem * discount_add_cars)

    TotalExtra = 0
    if ExtraLia == "Y":
        TotalExtra += NumberCarsInsured * cost_extra_lia_cov

    if GlassCov == "Y":
        TotalExtra += NumberCarsInsured * cost_glass_cov

    if OptLoanCar == "Y":
        TotalExtra += NumberCarsInsured * cost_loaner_car

    TotalPremium = TotalExtra + InsurePrem
    Hst = TotalPremium * hst_rate
    TotalCost = TotalPremium + Hst

    MonPayment = (TotalCost + process_fee) / 8

# Outputs.
    print()
    print("     One Stop Insurance Company     ")
    print()
    print("------------------------------------")
    print("Customer's Name: " + CustFirstName, CustLastName)
    print(f"Customer's Phone Number:  {CusPhoneNum}")
    print(f"Customer's Address: {Address}")
    print("                    ", City + ",", Province)
    print("                    ", PostalCode)
    print("------------------------------------")
    print(f"Number of cars insured: {NumberCarsInsured}")
    print(f"Extra Liability: {ExtraLia}")
    print(f"Glass Coverage:  {GlassCov}")
    print(f"Loaner Car:      {OptLoanCar}")
    print(f"Payment Option:  {PayOption}")
    print("------------------------------------")
    InsurePremDSP = "${:,.2f}".format(InsurePrem)
    print(f"Insurance Premiums:  {InsurePremDSP} ")
    TotalExtraDSP = "${:,.2f}".format(TotalExtra)
    print(f"Total Extra Cost:    {TotalExtraDSP}")
    TotalPremiumDSP = "${:,.2f}".format(TotalPremium)
    print(f"Total Insurance Premium: {TotalPremiumDSP}")
    HstDSP = "${:,.2f}".format(Hst)
    print(f"Taxes(HST):          {HstDSP}")
    TotalCostDSP = "${:,.2f}".format(TotalCost)
    print(f"Total Cost:          {TotalCostDSP}")
    print("------------------------------------")
    MonPaymentDSP = "${:,.2f}".format(MonPayment)
    if PayOption == "M":
        print(f"Monthly Payment:     {MonPaymentDSP}")
        print("------------------------------------")

# Policy number input values.
    f = open("Policies.dat", "a")
    f.write("{}, ".format(next_policy_num))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Province))
    f.write("{}, ".format(PostalCode))
    f.write("{}, ".format(CusPhoneNum))
    f.write("{}, ".format(NumberCarsInsured))
    f.write("{}, ".format(ExtraLia))
    f.write("{}, ".format(GlassCov))
    f.write("{}, ".format(OptLoanCar))
    f.write("{}, ".format(PayOption))
    f.write("{}\n".format(TotalCost))

    print()
    print("Policy information processed and saved!")
    print()
    next_policy_num += 1

    Option = input("Would you like to process another claim? (Y / N) ").upper()
    print()
    if Option == "N":
        break

    f.close()

# Writes the current values back to the defaults file.
    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(next_policy_num))
    f.write("{}\n".format(basic_prem))
    f.write("{}\n".format(discount_add_cars))
    f.write("{}\n".format(cost_extra_lia_cov))
    f.write("{}\n".format(cost_glass_cov))
    f.write("{}\n".format(cost_loaner_car))
    f.write("{}\n".format(hst_rate))
    f.write("{}\n".format(process_fee))
    f.close()