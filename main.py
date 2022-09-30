from PyPDF2 import PdfFileReader, PdfFileWriter
import os


mainpdf = PdfFileReader("tet.pdf")

# [
#     [89, 100],
#     [101, 109],
#     [130, 136],
#     [87, 88],
#     [119, 125],
#     [126, 129],
#     [320, 328]
# ],
# [
#     [149,161],
#     [141, 148],
#     [137, 138],
#     [180, 181]
# ],
# [
#     [206, 258]
# ],
# [
#     [259, 299],
#     [320, 322]
# ],
# [
#     [352, 361]
# ],
# [
#     [329, 351],
#     [395, 401]
# ]



subs = [
    [
        [206, 258]
    ]
]


count = 0
for sub in subs:

    count += 1

    writer = PdfFileWriter()

    for pages in sub:
        start_page = pages[0]
        end_page = pages[1]

        for current_page in range(start_page, end_page+1):
            writer.addPage(mainpdf.getPage(current_page))

    writer.write(f"{count}.pdf")