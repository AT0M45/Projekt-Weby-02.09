from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
doc = SimpleDocTemplate('dokumentace.pdf', pagesize=A4, rightMargin=1.7*cm, leftMargin=1.7*cm, topMargin=5*cm, bottomMargin=1.7*cm)
styles = getSampleStyleSheet()
styles['BodyText'].fontName = 'Arial'
styles['Title'].fontName = 'Arial-Bold'
styles['Heading2'].fontName = 'Arial-Bold'
story = [Paragraph('Dokumentace - FitStart', styles['Title']), Spacer(1, 0.4*cm)]
story.append(Paragraph('Jednoduchý školní web o pohybových lekcích. Obsahuje responzivní navigaci, carousel se čtyřmi fotografiemi, karty lekcí, ukazatel postupu, tabulku rozvrhu, formulář pro přihlášku na více lekcí a kontaktní formulář.', styles['BodyText']))
story += [Spacer(1, 0.5*cm), Paragraph('Odkazy', styles['Heading2'])]
story.append(Paragraph('GitHub: https://github.com/AT0M45/Projekt-Weby-02.09', styles['BodyText']))
story.append(Paragraph('Hlavním zdrojem pro HTML, CSS a Bootstrap byla dokumentace W3Schools: https://www.w3schools.com/', styles['BodyText']))
story += [Spacer(1, 0.5*cm), Paragraph('Externí knihovny', styles['Heading2'])]
data = [['Název a verze', 'Odkaz', 'Licence', 'Autor'], ['Bootstrap 5.3.8', 'https://getbootstrap.com/', 'MIT', 'The Bootstrap Authors'], ['Font Awesome Free\n7.3.1', 'https://fontawesome.com/', 'CC BY 4.0,\nMIT a OFL 1.1', 'Fonticons, Inc.'], ['Tom Select 2.6.2', 'https://tom-select.js.org/', 'Apache-2.0', 'Brian Reavis a contributors']]
table = Table(data, colWidths=[3.2*cm, 4.4*cm, 3.2*cm, 4.1*cm], repeatRows=1)
table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#198754')), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('GRID', (0, 0), (-1, -1), 0.5, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('FONTNAME', (0, 0), (-1, 0), 'Arial-Bold'), ('FONTNAME', (0, 1), (-1, -1), 'Arial'), ('FONTSIZE', (0, 0), (-1, -1), 8), ('LEADING', (0, 0), (-1, -1), 10), ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
story.append(table)
story += [Spacer(1, 0.5*cm), Paragraph('Spuštění projektu', styles['Heading2'])]
story.append(Paragraph('Knihovny byly nainstalovány pomocí NPM. Lokální soubory knihoven jsou uložené ve složce assets, proto web funguje i po nahrání na hosting. Web se otevře souborem index.html.', styles['BodyText']))
doc.build(story)
