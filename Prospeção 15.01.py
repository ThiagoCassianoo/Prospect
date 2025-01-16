import os
from PyPDF2 import PdfReader, PdfWriter

# Função para extrair páginas de um PDF
def extract_pages(pdf_path, start_page, end_page, output_pdf_path):
    try:
        # Abrir o PDF original
        with open(pdf_path, 'rb') as infile:
            reader = PdfReader(infile)
            writer = PdfWriter()

            # Adicionar as páginas desejadas ao novo PDF
            for i in range(start_page - 1, end_page):  # Ajuste para 0-index
                if i < len(reader.pages):  # Verifica se a página existe
                    writer.add_page(reader.pages[i])

            # Salvar o novo PDF
            with open(output_pdf_path, 'wb') as outfile:
                writer.write(outfile)

        print(f"Páginas extraídas e salvas em: {output_pdf_path}")

    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Caminho para o PDF original
pdf_path = r"D:\Desktop\SC MARCAS\Arquivos\Marcas2819.pdf"  # Altere para o nome correto do seu PDF

# Definindo as páginas a serem extraídas
start_page = 1763
end_page = 1936

# Caminho para o PDF de saída
output_pdf_path = r"D:\Desktop\SC MARCAS\Arquivos\Marcas2819\Paginas_1763_a_1936.pdf"  # Caminho do PDF de saída

# Verifica se o diretório de saída existe, se não, cria
output_dir = os.path.dirname(output_pdf_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Executar a função para extrair as páginas
extract_pages(pdf_path, start_page, end_page, output_pdf_path)