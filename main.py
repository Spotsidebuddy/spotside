from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name: str):
        super().__init__()
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 36)
        self.pdf.cell(0, 30, 'CS50 Shirtificate', align='C')
        self.pdf.image('./shirtificate.png', 10, 50, w=self.pdf.epw)
        self.pdf.set_font('helvetica', 'B', 28)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.ln(120)
        self.pdf.cell(0, 0, f'{name} took CS50', align='C')

    def shirt_out(self):
        self.pdf.output('shirtificate.pdf')


def main():
    name = input('Name: ')
    shirtificate = PDF(name)
    shirtificate.shirt_out()


if __name__ == '__main__':
    main()
