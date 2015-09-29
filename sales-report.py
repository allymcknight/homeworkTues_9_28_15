# """
# sales_report.py - Generates sales report showing the total number
#                   of melons each sales person sold.
# """
# #Creates empty lists to hold names of sales people and total number
# # of melons sold by person. 
# salespeople = []
# melons_sold = []

# #Opens text file and separates each line into 3 items in a list.
# #names the sales person for string in item, assigns 
# #the integer of melons sold per order to melons.
# f = open("sales-report.txt")
# for line in f:
#     line = line.rstrip()
#     entries = line.split("|")
#     salesperson = entries[0]
#     melons = int(entries[2])
# #Checks to see if name is already in list holding all sales people iterated over.
# #gets the index number of one list and grabs the corresponding
# #values from the melons_sold list. Adds melons to that position.
#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons

# #Adds the sales person name to the sales people list if not there originally.
# #Adds the melons sold to same index location.
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# #Calls the value in corresponding index and places them in print.
# for i in range(len(salespeople)):
#     print "%s sold %d melons" % (salespeople[i], melons_sold[i])

def sales_report(filename):
    total_sales_report = {}
    for line in filename:
        line = line.strip()
        name, total, melons = line.split("|")
        total_sales_report[name] = melons
        if name in total_sales_report[name]:
            melons = melons + total_sales_report[melons]
        total_sales_report[name] = melons
        print "%s sold %s melons"%(name, melons)


sales_report(open("sales-report.txt"))