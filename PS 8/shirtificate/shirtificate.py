from fpdf import FPDF


def main():
    try:
        name = input("Name: ")
    except:
        pass

    pdf = PDF(name)
    pdf.save()


class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw)
        self.set_font_size(25)
        self.set_text_color(255, 255, 255)
        self.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self):
        self.output("shirtificate.pdf")

if __name__ == "__main__":
    main()