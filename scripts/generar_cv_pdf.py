import os
from fpdf import FPDF

class CV_PDF(FPDF):
    def header(self):
        pass
        
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, "Pagina 1 de 1", 0, 0, "C")

def generate_pdf_cv(avatar_path, output_pdf_path):
    # Initialize A4 PDF, margins: 12mm
    pdf = CV_PDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(12, 12, 12)
    pdf.add_page()
    
    # ------------------
    # COLOR PALETTE
    # ------------------
    primary_color = (26, 27, 39)    # Dark Navy
    accent_blue = (65, 105, 225)    # Royal Blue
    accent_purple = (123, 47, 247) # Deep Purple
    text_dark = (40, 40, 45)        # Soft Dark Text
    text_muted = (100, 100, 105)    # Muted Grey Text
    
    # ------------------
    # HEADER SECTION
    # ------------------
    if os.path.exists(avatar_path):
        pdf.image(avatar_path, x=12, y=12, w=28)
    
    # Name and Title (Shifted X to 44mm)
    pdf.set_xy(44, 12)
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(*primary_color)
    pdf.cell(0, 7, "David Santiago Gil Cifuentes", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_x(44)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(*accent_purple)
    pdf.cell(0, 5, "Desarrollador Junior  |  Estudiante ADSO - SENA (5 Trimestre)", new_x="LMARGIN", new_y="NEXT")
    
    # Contact Info row
    pdf.set_x(44)
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(*text_muted)
    contact_info = "Funza, Cundinamarca, Colombia  |  Tel: +57 313 356 8187  |  Email: gilsantiagodepa@gmail.com"
    pdf.cell(0, 5, contact_info, new_x="LMARGIN", new_y="NEXT")
    
    # Git & LinkedIn Info row
    pdf.set_x(44)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_text_color(*accent_blue)
    links_info = "GitHub: github.com/David-Santiago-Gil  |  LinkedIn: linkedin.com/in/david-santiago-gil-cifuentes-1410943b3"
    pdf.cell(0, 5, links_info, new_x="LMARGIN", new_y="NEXT")
    
    # Separator Line
    pdf.set_xy(12, 43)
    pdf.set_draw_color(*accent_blue)
    pdf.set_line_width(0.5)
    pdf.line(12, 43, 198, 43)
    
    # Helper to draw Section Titles
    def draw_section_title(y_pos, title):
        pdf.set_xy(12, y_pos)
        pdf.set_font("helvetica", "B", 10.5)
        pdf.set_text_color(*primary_color)
        pdf.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
        
        pdf.set_fill_color(*accent_purple)
        pdf.rect(12, y_pos + 5.5, 20, 1.0, "F")
        pdf.set_fill_color(230, 230, 235)
        pdf.rect(32, y_pos + 5.7, 166, 0.6, "F")
        return y_pos + 8

    # ------------------
    # PERFIL SECTION
    # ------------------
    next_y = draw_section_title(46, "PERFIL PROFESIONAL")
    pdf.set_xy(12, next_y)
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(*text_dark)
    perfil_text = (
        "Estudiante de quinto trimestre del Tecnologo ADSO en el SENA, con conocimientos basicos-intermedios en desarrollo "
        "frontend y experiencia en despliegue de aplicaciones completas. Construyo paginas web responsivas con HTML, CSS y "
        "JavaScript, y desarrollo componentes con Angular y React. Tengo experiencia practica montando aplicaciones full stack: "
        "frontend en Vercel, backend en Railway/Render con Node.js, y bases de datos en TiDB Cloud. Manejo Git/GitHub, trabajo "
        "con APIs REST (incluyendo integracion de APIs externas como TMDB), y cuento con certificacion en Inteligencia Artificial "
        "Fundamentals de IBM SkillsBuild. Busco mi primera oportunidad como desarrollador junior o trainee donde pueda seguir "
        "creciendo y aportar con lo que ya se."
    )
    pdf.multi_cell(0, 4.0, perfil_text)
    
    # ------------------
    # HABILIDADES TÉCNICAS SECTION
    # ------------------
    next_y = draw_section_title(pdf.get_y() + 3, "HABILIDADES TECNICAS")
    pdf.set_xy(12, next_y)
    
    skills = [
        ("Frontend:", "HTML5, CSS3, JavaScript (basico-intermedio), TypeScript (basico), Angular, React, Responsive Design."),
        ("Backend & APIs:", "Node.js, Express, Python, FastAPI, Workbench y MySQL (aprendidos y aplicados activamente)."),
        ("Despliegue & DevOps:", "Vercel, Railway, Render, TiDB Cloud (base de datos), Git / GitHub, VS Code, Scrum (basico)."),
        ("IA & Idiomas:", "Fundamentos de IA (Certificado IBM SkillsBuild)  |  Espanol (Nativo) e Ingles B1 (meta B2+).")
    ]
    
    for category, list_str in skills:
        pdf.set_x(12)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.set_text_color(*primary_color)
        pdf.cell(38, 4.2, category, 0, 0)
        
        pdf.set_font("helvetica", "", 8.2)
        pdf.set_text_color(*text_dark)
        pdf.cell(0, 4.2, list_str, 0, 1)

    # ------------------
    # PROYECTOS SECTION
    # ------------------
    next_y = draw_section_title(pdf.get_y() + 3, "PROYECTOS DESTACADOS (GitHub)")
    
    proyectos = [
        ("MovieNexus (Aplicacion Web de Entretenimiento)", "Angular | TypeScript | Vanilla CSS | TMDB API | Vercel", 
         "Catalogo interactivo de peliculas consumiendo la API de TMDB. Busquedas en tiempo real, trailers y favoritos persistentes (localStorage)."),
         
        ("Gestor de Tareas (Aplicacion Full Stack - CRUD)", "Angular | TypeScript | Node.js | Express | MySQL | Vitest | Render & Railway", 
         "Plataforma para administracion visual de tareas con operaciones CRUD completas y backend RESTful estructurado. Incluye testeo con Vitest."),
         
        ("FARM Stack CRUD (Desarrollo Full Stack de Alto Rendimiento)", "FastAPI (Python) | React | JavaScript | MySQL | TiDB Cloud | Uvicorn", 
         "Arquitectura moderna con backend asincono en Python de alta velocidad y frontend dinamico interactivo consumiendo APIs en la nube."),
         
        ("NeonRoyale Casino (Interfaz Web Interactiva UX/UI)", "Angular | TypeScript | HTML5 | CSS3 (Glow & Neon animations) | Vercel", 
         "Proyecto enfocado en el diseno premium y animaciones avanzadas en CSS3 para recrear una estetica neon retro-futurista responsiva.")
    ]
    
    current_y = next_y
    for title, tech, desc in proyectos:
        pdf.set_xy(12, current_y)
        pdf.set_font("helvetica", "B", 8.5)
        pdf.set_text_color(*primary_color)
        pdf.cell(100, 3.8, title, 0, 0)
        
        pdf.set_font("helvetica", "B", 7.5)
        pdf.set_text_color(*accent_blue)
        pdf.cell(0, 3.8, f"[{tech}]", 0, 1, "R")
        
        pdf.set_x(12)
        pdf.set_font("helvetica", "", 8)
        pdf.set_text_color(*text_dark)
        pdf.multi_cell(0, 3.6, f"  * {desc}")
        current_y = pdf.get_y() + 1.2

    # ------------------
    # EDUCACIÓN & CERTIFICACIONES SECTION
    # ------------------
    next_y = draw_section_title(current_y + 1.5, "EDUCACION Y CERTIFICACIONES")
    pdf.set_xy(12, next_y)
    
    # Certifications
    pdf.set_font("helvetica", "B", 8.2)
    pdf.set_text_color(*primary_color)
    pdf.cell(105, 4.2, "IBM SkillsBuild - Artificial Intelligence Fundamentals", 0, 0)
    pdf.set_font("helvetica", "", 7.8)
    pdf.set_text_color(*text_muted)
    pdf.cell(0, 4.2, "(Abril 2026 | Credencial Credly: 71c8be4e-7200-4f22-84ff-10136c39930)", 0, 1, "R")
    
    # SENA ADSO
    pdf.set_x(12)
    pdf.set_font("helvetica", "B", 8.2)
    pdf.set_text_color(*primary_color)
    pdf.cell(105, 4.2, "SENA - Tecnologo en Analisis y Desarrollo de Software (ADSO)", 0, 0)
    pdf.set_font("helvetica", "", 7.8)
    pdf.set_text_color(*text_muted)
    pdf.cell(0, 4.2, "(En curso | Trimestre 5 de 6)", 0, 1, "R")
    
    # Logistics
    pdf.set_x(12)
    pdf.set_font("helvetica", "B", 8.2)
    pdf.set_text_color(*primary_color)
    pdf.cell(105, 4.2, "SENA / Col. Dept. de Funza - Tecnico en Integracion Logistica (IDOL)", 0, 0)
    pdf.set_font("helvetica", "", 7.8)
    pdf.set_text_color(*text_muted)
    pdf.cell(0, 4.2, "(Completado | 2024)", 0, 1, "R")

    # ------------------
    # EXPERIENCIA LABORAL SECTION
    # ------------------
    next_y = draw_section_title(pdf.get_y() + 2, "EXPERIENCIA LABORAL")
    pdf.set_xy(12, next_y)
    
    pdf.set_font("helvetica", "B", 8.2)
    pdf.set_text_color(*primary_color)
    pdf.cell(100, 4.2, "Asesor de Ventas  |  Furor de la Moda (Funza, Cundinamarca)", 0, 0)
    pdf.set_font("helvetica", "", 7.8)
    pdf.set_text_color(*text_muted)
    pdf.cell(0, 4.2, "(Diciembre 2024 - Enero 2025)", 0, 1, "R")
    
    pdf.set_x(12)
    pdf.set_font("helvetica", "", 8)
    pdf.set_text_color(*text_dark)
    pdf.cell(0, 3.8, "  * Atencion al cliente, gestion de caja e inventario en un entorno comercial dinamico de alto flujo.", new_x="LMARGIN", new_y="NEXT")

    # ------------------
    # DISPONIBILIDAD E INTERESES SECTION
    # ------------------
    next_y = draw_section_title(pdf.get_y() + 2, "DISPONIBILIDAD E INTERESES")
    pdf.set_xy(12, next_y)
    pdf.set_font("helvetica", "", 8.0)
    pdf.set_text_color(*text_dark)
    disp_text = (
        "Disponibilidad inmediata para posiciones de Desarrollador Junior, Frontend Trainee, Practicas o soporte tecnico. "
        "Etapa lectiva: desde 28/07/2025 hasta 28/01/2027. Etapa productiva (para iniciar practicas): desde 29/01/2027 hasta 27/07/2027."
    )
    pdf.multi_cell(0, 3.8, disp_text)

    # Save PDF
    pdf.output(output_pdf_path)
    print(f"CV PDF successfully compiled at: {output_pdf_path}")

if __name__ == "__main__":
    avatar = r"c:\Users\davi2\OneDrive\Documentos\hoja de v\perfil Git hub\David-Santiago-Gil\assets\photo_framed.png"
    output_pdf = r"c:\Users\davi2\OneDrive\Documentos\hoja de v\perfil Git hub\David-Santiago-Gil\David_Santiago_Gil_CV.pdf"
    generate_pdf_cv(avatar, output_pdf)
