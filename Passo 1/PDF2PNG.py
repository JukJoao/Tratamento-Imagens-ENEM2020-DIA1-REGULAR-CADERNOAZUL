import os
from pdf2image import convert_from_path

input_folder = "Passo 1/2020_AZUL_D1_CD1.pdf"
output_folder = "imagensconvertidas"
os.makedirs(output_folder, exist_ok=True)

# Busca o PDF na pasta input
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

if pdf_files:
    pdf_path = os.path.join(input_folder, pdf_files[0])
    print(f"Convertendo {pdf_files[0]}...")
    
    paginas = convert_from_path(pdf_path, dpi=300)
    for i, pagina in enumerate(paginas):
        pagina.save(os.path.join(output_folder, f"pagina_{i:03d}.png"), "PNG")
    print("Conversão concluída.")
else:
    print("Nenhum arquivo PDF encontrado na pasta input.")