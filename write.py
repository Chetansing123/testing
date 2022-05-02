import openpyxl

# load the workbook

workbook = openpyxl.load_workbook("")

# load the sheet
sheet = workbook.active

# write the content using for loop (n,n-1=3-1=2===1-2)
for r in range(1,3)
    for c in range(1,3)
        sheet.cell(row=r,column=c)value="welcome"

# save the workbook after once we added  the value
workbook.save("")
print("end of file writing")