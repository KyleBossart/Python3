from email import header
import random
from urllib.request import HTTPDefaultErrorHandler
import xlsxwriter

def main():

    # Make
    # Model
    # Serial Number

    workbook = xlsxwriter.Workbook("inventory.xlsx")
    
    cellFormat = workbook.add_format()
    cellFormat.set_text_wrap()
    cellFormat.set_align("top")
    cellFormat.set_align("left=")

    headerFormat = workbook.add_format()
    headerFormat.set_bg_color("#0AB8F4")
    headerFormat.set_text_wrap()
    cellFormat.set_align("left")


    worksheet = workbook.add_worksheet("Assets")

    worksheet.set_column("A:C", 20)

    worksheet.write("A1", "Make", headerFormat)
    worksheet.write("B1", "Model", headerFormat)
    worksheet.write("C1", "Serial Number", headerFormat)

    rowIndex = 2

    for row in range(10):

        make = random.choice(["Dell", "Apple"])
        model = random.choice(["Laptop", "Desktop"])
        serial = row + 100

        worksheet.write("A" + str(rowIndex), make, cellFormat)
        worksheet.write("B" + str(rowIndex), model, cellFormat)
        worksheet.write("C" + str(rowIndex), serial, cellFormat)

        rowIndex += 1

        print(make, model, serial)

    workbook.close()
    


if __name__ == "__main__":
    main()
