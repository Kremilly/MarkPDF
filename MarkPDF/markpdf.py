import os

from xhtml2pdf import pisa
from md_builder import MDBuilder

class MarkPDF:
    
    @classmethod
    def read_content(cls, input):
        if os.path.exists(input):
            with open(input, encoding='utf-8') as content:
                return content.read()
    
    @classmethod
    def render(cls, input):
        content = cls.read_content(input)
        return MDBuilder.render(content)
    
    @classmethod
    def export(cls, input, output):
        md_content = cls.read_content(input)
        content = MDBuilder.render(md_content)
        
        with open(output, "wb") as result_file:
            pisa.CreatePDF(content, dest=result_file)
            
        return content