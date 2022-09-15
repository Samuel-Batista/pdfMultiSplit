from PyPDF2 import PdfFileReader, PdfFileWriter
import os


mainpdf = PdfFileReader("tet.pdf")



subs = [
    [
        [13, 20],
        [300, 351],
    ],
    [
        [21, 86],
        [191, 205]
    ],
    [
        [89,109],
        [119, 135],
        [137, 147]
    ],
    [
        [149, 190],
    ],
    [
        [206, 276]
    ],
    [
        [276, 299]
    ],
    [
        [352, 422]
    ],

]


count = 0
for sub in subs:

    count += 1

    writer = PdfFileWriter()

    for pages in sub:
        start_page = pages[0]
        end_page = pages[1]

        range_= start_page - end_page

        for current_page in range(start_page, end_page+1):
            writer.addPage(mainpdf.getPage(current_page))

    writer.write(f"tet{count}.pdf")