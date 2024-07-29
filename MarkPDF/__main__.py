from flags import Flags
from markpdf import MarkPDF

flags = Flags.parser("Usage: python markpdf -i <INPUT_MARKDOWN_FILE> -o <OUTPUT_PDF_FILE>", [
    {'short': 'i', 'long': 'input', 'help': 'Input markdown file', 'required': True},
    {'short': 'o', 'long': 'output', 'help': 'Output PDF file', 'required': True},
])

if __name__ == '__main__':
    MarkPDF.export(flags.input, flags.output)
