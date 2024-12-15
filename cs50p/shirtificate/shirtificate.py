import sys

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 36)
        self._pdf.cell(0, 30, 'CS50 Shirtificate', align='C')
        self._pdf.image('./shirtificate.png', 10, 50, w=self._pdf.epw)
        self._pdf.set_font('helvetica', 'B', 28)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.ln(120)
        self._pdf.cell(0, 0, f'{name} took CS50', align='C')

    def shirt_out(self):
        self._pdf.output('shirtificate.pdf')


def main():
    name = input('Name: ')
    shirtificate = PDF(name)
    shirtificate.shirt_out()
    sys.exit(0)


if __name__ == '__main__':
    main()
