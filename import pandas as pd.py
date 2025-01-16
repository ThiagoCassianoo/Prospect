import pandas as pd 
import PyPDF2 
import re

# Função para extrair e organizar os dados do PDF
def extract_data_from_pdf(pdf_path):
    try:
        # Abrir o PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()  # Extrai texto de cada página
        
        # Salvar texto extraído em um arquivo temporário
        with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)
        
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return []

    # Expressão regular para capturar os dados
    pattern = r"(\d{9,12})\s+Indeferimento do pedido\s+Titular:\s+(.+?)\s+\[BR/[\w]+\]\s+Procurador:\s+(.+?)?\s+Detalhes do despacho:\s+(.+?)(?=\d{9,12}|$)"
    matches = re.findall(pattern, text, re.DOTALL)  # Encontra todas as correspondências
    
    # Organizar os dados em uma lista de dicionários
    data = []
    for match in matches:
        data.append({
            "Número do Processo": match[0].strip(),
            "Titular": match[1].strip(),
            "Procurador": match[2].strip() if match[2] else "",  # Deixar em branco se não houver procurador
            "Detalhes do despacho": match[3].strip(),
        })
    
    return data

# Caminho para o PDF
pdf_path = r"D:\Desktop\SC MARCAS\Arquivos\Indeferidos.2563.2932.pdf"  

# Extrair dados
data = extract_data_from_pdf(pdf_path)

# Verificar se dados foram extraídos
if data:
    # Criar DataFrame
    df = pd.DataFrame(data)

    # Exportar para CSV
    output_csv_path = "Indeferidos_Completos.csv"  # Nome do arquivo CSV de saída
    df.to_csv(output_csv_path, index=False, sep=';', encoding='utf-8')  # Exporta o DataFrame para CSV

    print(f"Arquivo exportado para: {output_csv_path}")  # Mensagem de confirmação
else:
    print("Nenhum dado foi extraído do PDF.")  # Mensagem de erro
