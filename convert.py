import os
from PIL import Image

def convert_image(input_path, formats):
    """
    Converte uma imagem para múltiplos formatos e salva na mesma pasta.
    
    Args:
        input_path (str): Caminho completo da imagem de entrada.
        formats (list): Lista de extensões de saída (sem o ponto), ex: ["png", "ico"].
    """
    # Verifica se o arquivo existe
    if not os.path.isfile(input_path):
        print(f"Arquivo não encontrado: {input_path}")
        return
    
    # Abre a imagem
    img = Image.open(input_path)
    base, _ = os.path.splitext(input_path)
    folder = os.path.dirname(input_path)
    filename = os.path.basename(base)
    
    # Para cada formato na lista, salva a imagem convertida
    for fmt in formats:
        output_path = os.path.join(folder, f"{filename}.{fmt}")
        try:
            img.save(output_path, fmt.upper())
            print(f"Salvo: {output_path}")
        except Exception as e:
            print(f"Erro salvando {fmt}: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python convert.py /caminho/para/imagem.ext")
        sys.exit(1)
        
    # Defina aqui os formatos desejados
    formats = ["png", "ico"]
    
    input_path = sys.argv[1]
    convert_image(input_path, formats)

# Made by ChatGPT | Simple Use