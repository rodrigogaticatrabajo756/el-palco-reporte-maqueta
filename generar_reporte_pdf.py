from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


PDF_PATH = "reporte-el-palco.pdf"


class ColorBlock(Flowable):
    def __init__(self, width, height, color, text, label=None):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.label = label

    def draw(self):
        canvas = self.canv
        canvas.setFillColor(self.color)
        canvas.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        if self.label:
            canvas.setFillColor(colors.HexColor("#0b4f8a"))
            canvas.rect(12, self.height - 30, 76, 18, stroke=0, fill=1)
            canvas.setFillColor(colors.white)
            canvas.setFont("Helvetica-Bold", 7)
            canvas.drawString(18, self.height - 24, self.label.upper())
        canvas.setFillColor(colors.white)
        canvas.setFont("Times-Bold", 17)
        text_obj = canvas.beginText(14, 25)
        text_obj.setLeading(18)
        for line in self.text.split("\n"):
            text_obj.textLine(line)
        canvas.drawText(text_obj)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 12 * mm, "El Palco - reporte de mejoras")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Pagina {doc.page}")
    canvas.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    base = getSampleStyleSheet()
    styles = {
        "eyebrow": ParagraphStyle(
            "eyebrow",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=colors.HexColor("#0b4f8a"),
            uppercase=True,
            spaceAfter=8,
        ),
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=34,
            leading=36,
            textColor=colors.HexColor("#101820"),
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontSize=12,
            leading=17,
            textColor=colors.HexColor("#555555"),
            spaceAfter=16,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#101820"),
            spaceBefore=14,
            spaceAfter=8,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#101820"),
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=15,
            textColor=colors.HexColor("#222222"),
            spaceAfter=7,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#666666"),
        ),
        "center": ParagraphStyle(
            "center",
            parent=base["BodyText"],
            alignment=TA_CENTER,
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#555555"),
        ),
    }

    story = []
    story.append(Paragraph("REPORTE SIMPLE DE DIAGNOSTICO Y MEJORA", styles["eyebrow"]))
    story.append(Paragraph("El Palco", styles["title"]))
    story.append(
        Paragraph(
            "Propuesta para potenciar la presentacion digital del sitio, respetando su esencia actual y aprovechando la base solida que ya tiene en WordPress.",
            styles["subtitle"],
        )
    )
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Diagnostico general", styles["h2"]))
    story.append(
        Paragraph(
            "El sitio esta construido sobre WordPress, una plataforma correcta para medios digitales porque permite publicar notas, ordenar secciones, administrar autores y trabajar SEO sin depender siempre de desarrollo a medida.",
            styles["body"],
        )
    )
    summary_data = [
        [
            Paragraph("<b>Plataforma</b><br/>WordPress con tema NewsMunch.", styles["body"]),
            Paragraph("<b>Diseno</b><br/>Portal de noticias con partes editadas mediante Elementor.", styles["body"]),
        ],
        [
            Paragraph("<b>SEO</b><br/>Utiliza Yoast SEO, una buena base para posicionamiento.", styles["body"]),
            Paragraph("<b>Rendimiento</b><br/>Cuenta con LiteSpeed Cache para mejorar velocidad.", styles["body"]),
        ],
    ]
    summary = Table(summary_data, colWidths=[82 * mm, 82 * mm])
    summary.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f7f7f7")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(summary)
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "La base tecnica es adecuada y el sitio ya esta bien encaminado. El objetivo no deberia ser cambiarlo por completo, sino ajustar detalles de identidad, jerarquia editorial, marca, textos automaticos y terminacion profesional.",
            styles["body"],
        )
    )

    story.append(Paragraph("2. Puntos a mejorar", styles["h2"]))
    improvements = [
        ("Titulo de la home", 'Cambiar "Home - El Palco" por un titulo editorial como "El Palco | Politica bonaerense, legislatura y territorio".'),
        ("Footer", "Quitar creditos del tema, completar columnas vacias, sumar redes reales y usar un correo institucional del dominio."),
        ("Idioma", 'Reemplazar textos como "By" y "views" por "Por" y "lecturas".'),
        ("Identidad", "Reforzar la estetica propia con negro y distintos tonos de azul, manteniendo el espiritu actual del sitio."),
        ("Confianza", 'Sumar paginas de "Quienes somos", "Equipo", "Contacto", "Politica editorial" y "Publicidad".'),
    ]
    for title, text in improvements:
        story.append(KeepTogether([Paragraph(title, styles["h3"]), Paragraph(text, styles["body"])]))

    story.append(Paragraph("3. Propuesta profesional", styles["h2"]))
    proposal_items = [
        "Reordenar la portada actual para que la noticia principal y las secundarias se lean con mas claridad.",
        "Usar una paleta sobria basada en negro editorial, blanco, grises y diferentes tonos de azul.",
        "Mejorar las paginas de autor con foto, biografia breve, redes y archivo de notas.",
        "Ordenar categorias para que funcionen como secciones periodisticas claras.",
        "Optimizar imagenes, reducir plugins innecesarios y mantener activa la cache.",
        "Crear metadatos correctos para compartir notas en redes sociales.",
    ]
    for item in proposal_items:
        story.append(Paragraph(f"- {item}", styles["body"]))

    story.append(Paragraph("4. Alcance del trabajo", styles["h2"]))
    story.append(
        Paragraph(
            "El trabajo propuesto se enfoca en mejoras esteticas, editoriales y de presentacion sobre la estructura actual del sitio. No se plantea una reconstruccion completa ni el desarrollo de nuevas funcionalidades complejas.",
            styles["body"],
        )
    )

    scope_data = [
        [
            Paragraph("<b>Incluye</b>", styles["body"]),
            Paragraph("<b>No incluye</b>", styles["body"]),
        ],
        [
            Paragraph(
                "- Revision estetica general del sitio.<br/>"
                "- Ajustes de colores, espaciados, tipografias y jerarquia visual.<br/>"
                "- Orden visual de la portada manteniendo la estructura actual.<br/>"
                "- Revision responsive en celular, tablet y escritorio.<br/>"
                "- Footer mas profesional y mejor organizado.<br/>"
                "- Correccion de textos visibles del theme, como By o views.<br/>"
                "- Ajustes basicos de SEO: titulo, descripcion y presentacion general.<br/>"
                "- Revision de paginas institucionales simples.<br/>"
                "- Acompanamiento durante el proceso y una instancia de revision final.",
                styles["body"],
            ),
            Paragraph(
                "- Desarrollo de funcionalidades nuevas.<br/>"
                "- Sistemas de usuarios, membresias, pagos o suscripciones.<br/>"
                "- Redaccion completa de notas periodisticas.<br/>"
                "- Diseno de logo nuevo o identidad de marca desde cero.<br/>"
                "- Campanas de publicidad paga.<br/>"
                "- Mantenimiento mensual posterior.<br/>"
                "- Carga masiva de contenido.<br/>"
                "- Cambios estructurales profundos del theme.<br/>"
                "- Hosting, dominio o costos de plugins pagos.",
                styles["body"],
            ),
        ],
    ]
    scope = Table(scope_data, colWidths=[82 * mm, 82 * mm])
    scope.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#101820")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f7f7f7")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(scope)
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Si durante el proceso surge una necesidad fuera de este alcance, se conversa previamente y se cotiza aparte. Nada se implementa ni se cobra sin aprobacion.",
            styles["body"],
        )
    )

    story.append(Paragraph("5. Plan de implementacion", styles["h2"]))
    roadmap = Table(
        [
            ["Etapa", "Accion", "Resultado esperado"],
            ["Dias 1 a 3", "Ajustar SEO, footer, redes, correo, paginas institucionales y textos automaticos.", "Mayor confianza y presentacion mas seria sin alterar la estructura principal."],
            ["Dias 4 a 7", "Ordenar la portada en WordPress/Elementor, respetando la esencia actual.", "Home mas clara, moderna y periodistica, pero reconocible para el cliente."],
            ["Dias 8 a 10", "Mejorar autores, categorias, imagenes y estructura de notas.", "Mejor experiencia de lectura y navegacion."],
            ["Dias 11 a 14", "Medir velocidad, revisar plugins y ajustar detalles responsive.", "Sitio mas rapido y profesional en celular."],
        ],
        colWidths=[24 * mm, 91 * mm, 49 * mm],
    )
    roadmap.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#101820")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(roadmap)

    story.append(PageBreak())
    story.append(Paragraph("6. Como podria quedar la portada", styles["h2"]))
    story.append(
        Paragraph(
            "La maqueta visual adjunta muestra una posible evolucion: mas editorial, mas limpia y con tonos azules, pero sin alejarse demasiado de la estructura actual.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 8))

    top = Table(
        [[Paragraph("<font color='white'><b>El Palco</b></font>", styles["body"]), Paragraph("<font color='white'>Inicio | Legislatura | Politica | Territorio | Opinion</font>", styles["small"])]],
        colWidths=[60 * mm, 104 * mm],
        rowHeights=[16 * mm],
    )
    top.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#101820")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    story.append(top)
    story.append(Spacer(1, 6))

    hero = Table(
        [
            [
                ColorBlock(98 * mm, 72 * mm, colors.HexColor("#202b34"), "La agenda politica\nbonaerense, contada\ndesde el territorio", "Destacada"),
                [
                    ColorBlock(60 * mm, 33 * mm, colors.HexColor("#303b46"), "Claves de la semana\nen Diputados y Senado", "Legislatura"),
                    Spacer(1, 6),
                    ColorBlock(60 * mm, 33 * mm, colors.HexColor("#39424c"), "Municipios, poder local\ny rosca politica", "Territorio"),
                ],
            ]
        ],
        colWidths=[101 * mm, 63 * mm],
    )
    hero.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(hero)
    story.append(Spacer(1, 14))

    card_data = [
        [
            Paragraph("<b>Ultimas noticias</b><br/>Tres tarjetas limpias con categoria, titulo y bajada breve.", styles["body"]),
            Paragraph("<b>Bloque institucional</b><br/>Espacio claro para identidad, contacto y secciones principales.", styles["body"]),
            Paragraph("<b>Footer institucional</b><br/>Quienes somos, Equipo, Contacto, Politica editorial y Publicidad.", styles["body"]),
        ]
    ]
    cards = Table(card_data, colWidths=[54 * mm, 54 * mm, 54 * mm])
    cards.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f7f7f7")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    story.append(cards)
    story.append(Spacer(1, 14))
    story.append(
        Paragraph(
            "Conclusion: El Palco ya tiene una base funcional y solida. Para elevarlo, no hace falta empezar de cero: alcanza con profesionalizar la identidad, ordenar la portada, completar la informacion institucional, mejorar los detalles de idioma y optimizar la experiencia de lectura. Con apoyo tecnico, este proceso puede resolverse en un plazo maximo de dos semanas.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("Documento preparado como guia simple de presentacion. Fecha: mayo de 2026.", styles["center"]))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


if __name__ == "__main__":
    build_pdf()
