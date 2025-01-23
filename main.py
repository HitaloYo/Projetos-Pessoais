import pyautogui
import pytesseract
from openpyxl import Workbook
from datetime import datetime

# Configurar o caminho do Tesseract OCR (ajuste conforme sua instalação)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Criar ou carregar a planilha
try:
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Pontuação Mahjong"
    sheet.append(["Data e Hora", "Pontuação"])  # Cabeçalho
    workbook.save("pontuacoes_mahjong.xlsx")
except Exception as e:
    print(f"Erro ao criar a planilha: {e}")

# Função para capturar e extrair pontuação
def capturar_pontuacao(area):
    # Capturar a área da tela
    screenshot = pyautogui.screenshot(region=area)
    # Reconhecer o texto na imagem
    pontuacao = pytesseract.image_to_string(screenshot, config='--psm 7')
    return pontuacao.strip()

# Coordenadas da área onde aparece a pontuação (ajuste manualmente)
# Formato: (x, y, largura, altura)
area_da_pontuacao = (100, 200, 150, 50)  # Exemplo de coordenadas, ajuste para o seu caso

try:
    # Capturar a pontuação atual
    pontuacao = capturar_pontuacao(area_da_pontuacao)
    print(f"Pontuação capturada: {pontuacao}")

    # Salvar na planilha
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    workbook = Workbook()
    sheet = workbook.active
    sheet.append([agora, pontuacao])
    workbook.save("pontuacoes_mahjong.xlsx")
    print("Pontuação salva na planilha!")
except Exception as e:
    print(f"Erro durante o processo: {e}")
