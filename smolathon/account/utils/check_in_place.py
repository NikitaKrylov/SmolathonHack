import qrcode
import qrcode.image.svg

from smolathon.settings import MEDIA_ROOT


def create_qr_code(url: str, filename: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    path = MEDIA_ROOT + "temp/" + filename
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    return path


