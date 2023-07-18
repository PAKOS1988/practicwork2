import qrcode

def generate_qrcode(info):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f'film {info["user_film"]}; time {info["user_data"]}; cinema {info["user_hall"]}; position {"user_position"}')
    qr.make(fit=True)
    # img = qrcode.make(f'film {info["user_film"]}; time {info["user_data"]}; cinema {info["user_hall"]}; position {"user_position"}')
    img = qr.make_image(fill_color = 'black', back_color='white')

    img.save( 'img_qr_code.png', 'png')
    return img

