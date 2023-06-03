from PyPDF2 import PdfFileReader, PdfFileMerger

merger = PdfFileMerger()
merger.append(PdfFileReader(open("file1.pdf", 'rb')))
merger.append(PdfFileReader(open("file2.pdf", 'rb')))
merger.write("file1_2_merge.pdf")