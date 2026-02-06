import random
import os
import pandas as pd
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import time

class GeneratePlate():
    def __init__(self):
        pass

    async def padding(self, string, max_n):
        if len(string) > max_n:
            return string[:max_n]
        else:
            return string.rjust(max_n)
    
    async def genrateRandomData(self):
        data = []
        prefixes = ['A', 'B', 'D', 'E', 'G', 'H', 'K',
                    'L', 'M', 'N', 'P', 'R', 'AA', 'AB',
                    'AD', 'AE', 'AG', 'BA', 'BB', 'BD',
                    'BE', 'BG', 'BH', 'BK', 'BL', 'BM',
                    'BN', 'BP', 'BR', 'DA', 'DB', 'DD',
                    'DE', 'DG', 'DH', 'DK']
        
        alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA']
        numbers = ['1', '12', '123', '1234', '567', '89']


        for i in prefixes:
            for j in numbers:
                for k in alphabet:    
                    prefix = i
                    suffix = k
                    number = j
                    date = ('0'+str(random.randint(0, 13)))[-2:] + ':' +str(random.randrange(20, 30, 2))

                    data.append([prefix, suffix, number, date])

        for i in prefixes:
            for j in numbers:
                prefix = i
                suffix = '   '
                number = j
                date = ('0'+str(random.randint(0, 13)))[-2:] + ':' +str(random.randrange(20, 30, 2))
                data.append([prefix, suffix, number, date])

            
        dataset = pd.DataFrame(data, columns=['Prefix', 'Suffix', 'Number', 'Date'])
        dataset.to_csv('Dataset Number Plate.csv')

    async def GeneratePlateImage(self):
        await self.genrateRandomData()
        newPath = 'Plate Image'
        if not os.path.exists(newPath):
            os.makedirs(newPath)

        dataset = pd.read_csv('Dataset Number Plate.csv')[:150000]
        fontPlate = ImageFont.truetype('Template/PlatNomor.ttf', size=160)
        fontDate = ImageFont.truetype('Template/PlatNomor.ttf', size=80)
        for i in range(0, len(dataset)):
            template = Image.open('Template/Plat Nomor.jpg')
            enhancer = ImageEnhance.Contrast(template)
            factor = 1.3 #increase contrast
            template = enhancer.enhance(factor)
            
            draw = ImageDraw.Draw(template)
            
            draw.text((44, 42), dataset['Prefix'][i], font=fontPlate, fill='white')
            draw.text((205, 40), await self.padding(str(dataset['Number'][i]), 5), font=fontPlate, fill='white')
            draw.text((530, 42), dataset['Suffix'][i], font=fontPlate, fill='white')
            draw.text((524, 248), dataset['Date'][i], font=fontDate, fill='white')
            if dataset['Suffix'][i] == '   ':
                template.save('Plate Image/'+dataset['Prefix'][i]+str(dataset['Number'][i])+'.jpg')
            else:
                template.save('Plate Image/'+dataset['Prefix'][i]+str(dataset['Number'][i])+dataset['Suffix'][i]+'.jpg')

    async def main(self):
        await self.GeneratePlateImage()
        

if __name__ == '__main__':
    s = time.perf_counter()
    Generate = GeneratePlate()
    asyncio.run(Generate.main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.5f} seconds.")

