import time
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def padding(string, max_n):
    if len(string) > max_n:
        return string[:max_n]
    if len(string) < max_n:
        return string.rjust(max_n)

def trans(filename):
    from PIL import Image

    img = Image.open(filename).resize((157, 112), Image.ANTIALIAS)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("new_sign.png", "PNG")

def generate_card(fontNIK, fontHeader, fontIdentity, templateName):
    template = Image.open(templateName)
    pic = Image.open('1.jpg').resize((444, 568), Image.ANTIALIAS)
    enhancer = ImageEnhance.Contrast(pic)
    factor = 0.5 #increase contrast
    pic = enhancer.enhance(factor)
    template.paste(pic, (1373, 228, 1817, 796))

    draw = ImageDraw.Draw(template)

    draw.text((320, 64-20), padding('Provinsi Sulawesi Selatan'.upper(), 35), font=fontHeader, fill='black', align='center')#max20
    draw.text((200, 135-20), padding('Kabupaten Kep. Siau Tagulandang Biaro'.upper(), 40), font=fontHeader, fill='black', align='center') #max 23 cahr

    draw.text((417, 236-30), '12132123123132' , font=fontNIK, fill='black')
    draw.text((463, 344-10), 'Random Name', font=fontIdentity, fill='black')
    draw.text((463, 404-12), 'Random TTL', font=fontIdentity, fill='black')
    draw.text((463, 459-12), 'Random JK', font=fontIdentity, fill='black')

    draw.text((463, 520-15), 'Random Alamat', font=fontIdentity, fill='black')
    draw.text((463, 572-16), 'Random RT/RW', font=fontIdentity, fill='black')
    draw.text((463, 626-13), 'Random Kel/Des', font=fontIdentity, fill='black')
    draw.text((463, 675-5), 'Random Kec', font=fontIdentity, fill='black')
    draw.text((463, 732-5), 'Random Religion', font=fontIdentity, fill='black')
    draw.text((463, 782-1), 'Random Marital Status', font=fontIdentity, fill='black')
    draw.text((463, 847-7), 'Random Job', font=fontIdentity, fill='black')
    draw.text((463, 897-1), 'Random Nationality', font=fontIdentity, fill='black')
    draw.text((463, 965-15), 'Random Expired', font=fontIdentity, fill='black')

    draw.text((1220+5, 460-15), 'X', font=fontIdentity, fill='black')

    draw.text((1412, 815), padding('AAAAAAAA SJDALSDJASLDASADSASD', 23), font=fontIdentity, fill='black')
    draw.text((1486, 873), '00-00-0000', font=fontIdentity, fill='black')


    im = Image.open('sign.jpg').convert("RGBA")
    enhancer = ImageEnhance.Contrast(im)
    factor = 3 #increase contrast
    im_output = enhancer.enhance(factor)
    im_output.save('new_sign.png')
    trans('new_sign.png')
    sign = Image.open("new_sign.png")
    area = (1543-10, 930+10, 1700-10, 1042+10)
    cropped_img = template.crop(area)
    template.paste(cropped_img,(1543-10, 930+10, 1700-10, 1042+10), cropped_img.convert("RGBA"))
    template.paste(sign,(1543-10, 930+10, 1700-10, 1042+10), sign)


    return template

def main():
    fontNIK = ImageFont.truetype("OCR-A Regular.ttf", size=70)
    fontIdentity = ImageFont.truetype("ArialUnicodeMS.ttf", size=46)
    fontHeader = ImageFont.truetype("ArialCEBold.ttf", size=65)

    templateName = "Template eKTP.jpg"

    card = generate_card(fontNIK, fontHeader, fontIdentity, templateName)
    card.save('Result.jpg')



if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.5f} seconds.")
