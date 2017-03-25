import datetime
import io
import time

import picamera

from PIL import Image, ImageStat, ImageFont, ImageDraw


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.rotation = 180

    stream = io.BytesIO()

    time.sleep(2)  # camera warm-up time

    for _ in camera.capture_continuous(stream, format='png'):
        stream.truncate()
        stream.seek(0)

        image = Image.open(stream)
        stat = ImageStat.Stat(image)

        r, g, b, _ = stat.mean

        if r < 50 and g < 50 and b < 50:
            print('[!] Lights must be powered off, sleeping...')       
            
            time.sleep(60 * 5)
        else:
            now = datetime.datetime.now()
            filename = 'images/img_{timestamp:%Y%m%d%H%M%S}.png'.format(timestamp=now)

            annotate_text = now.strftime('%H:%M:%S @ %d/%m/%Y')

            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf', 24)

            draw.text((10, 720), annotate_text, (255, 255, 0), font=font)

            image.save(filename)

            print('[!] Taken: {}'.format(filename))

            time.sleep(60 / 2)

        image.close()