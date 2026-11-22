"""
1) Add the activity details.
   a) Mention the activity name as "Farm Harvest Calculator".
   b) Introduce the program as a harvest and earnings calculator.

2) Store harvest values.
   a) Use the assignment operator `=` to store harvest from five fields.
   b) Store each field's harvest in separate variables.
"""
field1=100
field2=150
field3=200
field4=250
field5=300
total=field1+ field2+ field3+field4+field5
average=total/5
print("total per harvest",total)
print("average per harvest",average)
price=20
earnings=price*total
bags=total//25
leftover=total%25
total+=30
print("total after bounes")
total-=15
print("total earnings",earnings)
print("total bags",bags)
print("left over",leftover)
print("total after seed reserve",total)
lastyear=500
print("better last year",total >lastyear)
print("same like last year",total ==lastyear)
print("atleast better than last year",total >=lastyear)
"""
3) Use arithmetic operators.
   a) Use `+` to calculate the total harvest.
   b) Use `/` to calculate the average harvest per field.
   c) Use `*` to calculate total earnings.

4) Display total, average, and earnings.
   a) Print the total harvest in kilograms.
   b) Print the average harvest per field.
   c) Print the total earnings in rupees.

5) Use floor division and modulus.
   a) Use `//` to calculate the number of full 25 kg bags.
   b) Use `%` to calculate the leftover grain.
   c) Print the full bags and leftover amount.

6) Use comparison operators.
   a) Compare this year's harvest with last year's harvest.
   b) Use `>` to check if this year is better.
   c) Use `==` to check if both years are the same.
   d) Use `>=` to check if this year is at least as good.

7) Use assignment operators.
   a) Use `+=` to add bonus crop to the total.
   b) Use `-=` to subtract grain saved as seeds.
   c) Print the updated harvest after each change.

8) Calculate the final bag count.
   a) Use floor division again after adjustments.
   b) Print the final number of bags packed.
"""