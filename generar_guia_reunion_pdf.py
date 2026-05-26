from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


PDF_PATH = "guia-reunion-cliente.pdf"


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 12 * mm, "El Palco - guia de reunion")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Pagina {doc.page}")
    canvas.restoreState()


def p(text, style):
    return Paragraph(text, style)


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
            spaceAfter=8,
        ),
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=31,
            leading=34,
            textColor=colors.HexColor("#101820"),
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontSize=11,
            leading=16,
            textColor=colors.HexColor("#555555"),
            spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#101820"),
            spaceBefore=13,
            spaceAfter=7,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#0b4f8a"),
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            alignment=TA_LEFT,
            fontSize=9.7,
            leading=14,
            textColor=colors.HexColor("#222222"),
            spaceAfter=6,
        ),
        "quote": ParagraphStyle(
            "quote",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=15,
            leftIndent=8,
            rightIndent=8,
            textColor=colors.HexColor("#101820"),
            spaceAfter=8,
        ),
    }

    story = []
    story.append(p("GUIA DE APOYO PARA PRESENTAR EL REPORTE", styles["eyebrow"]))
    story.append(p("Reunion con El Palco", styles["title"]))
    story.append(
        p(
            "Material simple para explicar el diagnostico, hacer buenas preguntas y defender la propuesta sin que suene a critica del sitio actual.",
            styles["subtitle"],
        )
    )

    story.append(p("1. Objetivo de la reunion", styles["h2"]))
    story.append(
        p(
            "Presentar el trabajo como una mejora sobre una base que ya funciona. La idea no es decir que el sitio esta mal, sino mostrar que ya tiene una estructura solida y que con ajustes puntuales puede verse mas profesional, mas confiable y mas claro para los lectores.",
            styles["body"],
        )
    )

    story.append(p("2. Apertura sugerida", styles["h2"]))
    story.append(
        Table(
            [[p('"Estuve revisando la pagina y la base esta bien armada: usan WordPress, un tema pensado para noticias, herramientas de SEO y cache. Eso es positivo porque no hace falta empezar de cero. La propuesta es ordenar, profesionalizar y reforzar la identidad de El Palco con cambios concretos y realizables en poco tiempo."', styles["quote"])]],
            colWidths=[164 * mm],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f3f8fd")),
                    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c7d8ea")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                    ("TOPPADDING", (0, 0), (-1, -1), 9),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]
            ),
        )
    )

    story.append(p("3. Fundamentos tecnicos simples", styles["h2"]))
    tech_points = [
        "El sitio esta hecho en WordPress. Se ve por rutas publicas como /wp-content/, /wp-json/ y archivos propios de WordPress.",
        "Usa el tema NewsMunch. Se detecta por la ruta /wp-content/themes/newsmunch/ y por el archivo style.css del tema.",
        "Usa Elementor. Se ve por archivos del plugin y etiquetas publicas del constructor visual.",
        "Usa Yoast SEO. El codigo fuente indica que el sitio esta optimizado con Yoast SEO.",
        "Usa LiteSpeed Cache. El HTML muestra que la pagina esta cacheada con LiteSpeed Cache.",
        "Todo esto es una buena base para un medio digital porque permite publicar rapido, ordenar secciones y mejorar SEO sin rehacer el sitio.",
    ]
    for item in tech_points:
        story.append(p(f"- {item}", styles["body"]))

    story.append(p("4. Mensaje clave", styles["h2"]))
    story.append(
        p(
            '"La pagina no necesita un cambio drastico. Necesita una evolucion visual y editorial: mejorar jerarquia, detalles de marca, SEO, footer, textos automaticos y experiencia en celular."',
            styles["quote"],
        )
    )

    story.append(p("5. Preguntas para el cliente", styles["h2"]))
    questions = [
        ("Identidad y marca", [
            "Que quieren que el lector sienta cuando entra a El Palco?",
            "Tienen un azul institucional definido o trabajamos una gama de azules?",
            "Quieren mantener el logo actual tal cual o ajustar solo tamanos y ubicacion?",
            "Hay medios de referencia que les gusten visualmente?",
        ]),
        ("Contenido y secciones", [
            "Cuales son las secciones mas importantes?",
            "Que seccion deberia tener mas peso en la portada?",
            "Quieren que Periodismo no porteno sea una seccion distintiva principal?",
            "Que categorias actuales conviene mantener, unir o renombrar?",
        ]),
        ("Audiencia", [
            "A quien le hablan principalmente: funcionarios, legisladores, militancia, periodistas, lectores generales o municipios?",
            "La prioridad es informar rapido, analizar en profundidad o construir marca editorial?",
            "El lector entra mas desde redes sociales, Google o de forma directa?",
        ]),
        ("Equipo y credibilidad", [
            "Quieren mostrar autores con foto y biografia?",
            "Hay una descripcion institucional definitiva para Quienes somos?",
            "Quieren usar el Gmail actual o un correo del dominio, por ejemplo redaccion@elpalco.com.ar?",
            "Tienen redes sociales oficiales activas para enlazar?",
        ]),
        ("Portada y experiencia", [
            "Prefieren una home muy cargada de noticias o mas limpia y jerarquizada?",
            "Cuantas noticias destacadas deberia tener la primera pantalla?",
            "Quieren mantener carruseles o priorizar bloques fijos mas faciles de leer?",
            "Que informacion es imprescindible en celular?",
        ]),
        ("Plazos y forma de trabajo", [
            "Les parece bien trabajar en dos semanas con entregas por etapas?",
            "Quieren aprobar primero cambios visuales y despues cambios tecnicos?",
            "Quien aprueba textos institucionales, categorias y redes?",
            "Hay fechas importantes donde el sitio tenga que estar especialmente prolijo?",
        ]),
    ]
    for title, items in questions:
        story.append(p(title, styles["h3"]))
        for item in items:
            story.append(p(f"- {item}", styles["body"]))

    story.append(p("6. Cambios rapidos y defendibles", styles["h2"]))
    quick_changes = [
        "Cambiar el titulo SEO de la home.",
        "Completar footer y sacar textos genericos.",
        "Reemplazar textos en ingles como By y views.",
        "Ordenar la portada sin cambiar por completo el theme.",
        "Ajustar colores a negro y tonos de azul.",
        "Mejorar visualizacion en celular.",
        "Crear paginas institucionales basicas.",
        "Mejorar autores y categorias.",
    ]
    for item in quick_changes:
        story.append(p(f"- {item}", styles["body"]))

    story.append(p("7. Frases utiles", styles["h2"]))
    phrases = [
        ("Sobre el diagnostico", "La base existe y esta bien orientada para un medio. No estamos proponiendo tirar abajo el sitio, sino aprovechar lo que ya tiene."),
        ("Sobre el diseno", "La propuesta respeta la esencia actual, pero ordena la lectura. La idea es que parezca mas editorial y menos plantilla generica."),
        ("Sobre WordPress", "WordPress es una buena decision para este caso porque permite que el equipo publique sin depender de un programador para cada nota."),
        ("Sobre el plazo", "Como la base ya esta armada y los cambios son de mejora, el trabajo puede organizarse en un maximo de dos semanas."),
        ("Sobre el valor profesional", "Los detalles chicos suman mucho: footer completo, redes reales, autores, textos en espanol, SEO y una portada mas clara hacen que el medio se perciba mas serio."),
    ]
    for title, text in phrases:
        story.append(p(title, styles["h3"]))
        story.append(p(text, styles["body"]))

    story.append(p("8. Objeciones posibles", styles["h2"]))
    objections = [
        ("Pero la pagina ya esta funcionando", "Si, y eso es una ventaja. La propuesta no parte de un problema grave, sino de una oportunidad para que lo que ya funciona se vea mas profesional."),
        ("No queremos cambiar todo", "Justamente la idea es no cambiar todo. Se mantiene la estructura y se ajusta jerarquia, identidad y terminacion."),
        ("No queremos formularios ni suscripciones por ahora", "Perfecto. Por eso la maqueta no incluye formularios. Se puede usar ese espacio para identidad, contacto institucional o secciones principales."),
        ("Nos preocupa el tiempo", "El plan esta pensado para un maximo de dos semanas porque no hay que reconstruir el sitio. Se trabaja sobre la base actual."),
        ("No sabemos si hace falta tocar codigo", "Muchas cosas se pueden hacer desde WordPress. Solo algunos detalles finos de idioma, footer o estilos pueden requerir ajustes tecnicos puntuales."),
    ]
    for title, text in objections:
        story.append(p(title, styles["h3"]))
        story.append(p(text, styles["body"]))

    story.append(p("9. Cierre sugerido", styles["h2"]))
    story.append(
        p(
            '"Mi recomendacion es avanzar en dos etapas: primero ordenar lo institucional, SEO y detalles visibles; despues ajustar portada, mobile y secciones. Con eso El Palco mantiene su identidad, pero queda mas profesional y mas facil de presentar."',
            styles["quote"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(p("Idea central: la base esta bien; el trabajo propuesto la potencia.", styles["subtitle"]))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


if __name__ == "__main__":
    build_pdf()
