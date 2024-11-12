import qrcode

texto_qr = "texto para ser convertido para qrcode"

qr = qrcode.QRCode(
    version=2, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=20,  
    border=2,  
)

qr.add_data(texto_qr)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("nome_do_arquivo.png")
