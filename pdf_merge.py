import PyPDF2
import sys



inputs= sys.argv[1:]   #accept inputs from CL

def pdf_merge(pdf_list):
    for pdf_file in pdf_list:
        merger=PyPDF2.PdfFileMerger()     #loops into pdf_file and merges it
        print(pdf_file)
        merger.write('super.pdf')       #writes a new pdf
pdf_merge(inputs)

