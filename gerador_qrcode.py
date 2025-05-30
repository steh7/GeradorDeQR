import qrcode

def gerar_qrcode(texto, nome_arquivo):
    # Cria o QR code
    qr = qrcode.QRCode(
        version=1,  # tamanho do QR Code (1 é o menor)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # nível de correção de erro
        box_size=10,  # tamanho de cada quadrado do QR
        border=4  # borda
    )

    qr.add_data(texto)
    qr.make(fit=True)

    # Gera a imagem
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

    print(f"QR Code salvo como {nome_arquivo}")

if __name__ == "__main__":
    texto = input("Digite o texto ou URL para gerar o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: qrcode.png): ")
    gerar_qrcode(texto, nome_arquivo)
