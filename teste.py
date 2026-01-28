from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import cm

# --- Paleta de Cores Personalizada (Mais moderna que o Excel padrão) ---
COR_CABECALHO_FUNDO = colors.HexColor("#2c3e50")  # Azul petróleo escuro
COR_CABECALHO_TEXTO = colors.white
COR_COLUNA_HORA_FUNDO = colors.HexColor("#dfe6e9") # Cinza azulado claro
COR_LINHA_PAR = colors.white
COR_LINHA_IMPAR = colors.HexColor("#f1f2f6")      # Cinza muito claro para alternar
COR_BORDAS = colors.HexColor("#b2bec3")           # Cinza médio para as grades

def gerar_cronograma_semanal(nome_arquivo):
    # 1. Configuração do documento (A4 Paisagem/Deitado)
    # Margens pequenas para aproveitar o máximo do papel
    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize=landscape(A4),
        rightMargin=0.8*cm,
        leftMargin=0.8*cm,
        topMargin=1*cm,
        bottomMargin=0.8*cm
    )
    
    elementos = []
    
    # 2. Título
    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        'TituloSemanal',
        parent=estilos['Title'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=COR_CABECALHO_FUNDO,
        spaceAfter=15,
        alignment=1 # Centralizado
    )
    titulo = Paragraph("Planejamento Semanal de Atividades (24h)", estilo_titulo)
    elementos.append(titulo)

    # 3. Preparação dos Dados da Tabela
    # Cabeçalhos
    dias_semana = ['HORA', 'DOMINGO', 'SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
    dados_tabela = [dias_semana]
    
    # Gerando 24 linhas de horário (ex: das 05:00 às 04:00 do dia seguinte)
    # Você pode mudar o 'start_hour' para a hora que você costuma acordar
    start_hour = 4
    for i in range(20):
        hora_atual = (start_hour + i) % 24
        # Formata a hora (ex: 05:00, 23:00)
        horario_str = f"{hora_atual:02d}:00"
        # Cria a linha: [Hora, vazio, vazio, ..., vazio]
        linha = [horario_str] + [""] * 7
        dados_tabela.append(linha)

    # 4. Dimensões da Tabela (Cálculo para caber na A4 Paisagem)
    # Largura total disponível aprox 28cm.
    largura_hora = 2.5 * cm
    largura_dia = 3.6 * cm # (28 - 2.5) / 7 dias = ~3.64
    col_widths = [largura_hora] + [largura_dia] * 7
    
    # Altura disponível aprox 18cm (descontando título e margens)
    # 18cm / 25 linhas (1 cabeçalho + 24 dados) = ~0.72cm por linha
    altura_linha = 0.72 * cm
    row_heights = [1*cm] + [altura_linha] * 20 # Cabeçalho um pouco maior

    tabela = Table(dados_tabela, colWidths=col_widths, rowHeights=row_heights)

    # 5. Estilização da Tabela (Onde a mágica visual acontece)
    estilo_tabela = TableStyle([
        # -- Configurações Gerais --
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), # Alinhamento vertical no meio
        ('GRID', (0, 0), (-1, -1), 0.5, COR_BORDAS), # Grades finas em tudo

        # -- Cabeçalho (Linha 0) --
        ('BACKGROUND', (0, 0), (-1, 0), COR_CABECALHO_FUNDO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COR_CABECALHO_TEXTO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),

        # -- Coluna de Horários (Coluna 0) --
        ('BACKGROUND', (0, 1), (0, -1), COR_COLUNA_HORA_FUNDO),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
    ])

    # -- Efeito Zebra nas células de atividades (Alternar cores das linhas) --
    # Começa da linha 1 até o final, nas colunas 1 até o final
    for i, linha in enumerate(dados_tabela[1:], start=1):
        if i % 2 == 0:
            cor_fundo = COR_LINHA_PAR
        else:
            cor_fundo = COR_LINHA_IMPAR
        # Aplica a cor background nas células dos dias (coluna 1 em diante)
        estilo_tabela.add('BACKGROUND', (1, i), (-1, i), cor_fundo)

    tabela.setStyle(estilo_tabela)
    elementos.append(tabela)

    # 6. Gerar PDF
    try:
        doc.build(elementos)
        print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado com 24 horários.")
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")

if __name__ == "__main__":
    # Lembre-se de ativar seu ambiente virtual antes de rodar:
    # source venv/bin/activate  (Linux/Mac)
    # venv\Scripts\activate     (Windows)
    gerar_cronograma_semanal("cronograma_semanal_24h.pdf")
    