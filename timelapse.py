import os
import datetime
import time

import picamera

from PIL import Image, ImageStat, ImageFont, ImageDraw


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.rotation = 180

    time.sleep(2)  # camera warm-up time

    for filename in camera.capture_continuous('images/img_{timestamp:%Y%m%d%H%M%S}.png'):
        image = Image.open(filename)
        stat = ImageStat.Stat(image)

        r, g, b, _ = stat.mean

        if r < 50 and g < 50 and b < 50:
            print('[!] Lights must be powered off, sleeping...')

            try:
                os.unlink(filename)
            except OSError:
                pass

            time.sleep(60 * 10)
        else:
            annotate_text = datetime.datetime.now().strftime('%H:%M:%S @ %d/%m/%Y')

            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf', 24)

            draw.text((10, 730), annotate_text, (255, 255, 0), font=font)

            image.save(filename)

            print('[!] Taken: {}'.format(filename))

            time.sleep(60 * 2)

        image.close()
