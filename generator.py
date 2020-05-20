import json
import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from datetime import date

def generator ():
    # source -- Brazil
    response = requests.get("https://disease.sh/v2/countries/brazil")
    stats = json.loads(response.content)
    # source -- World
    response2 = requests.get("https://disease.sh/v2/all")
    stats2 = json.loads(response2.content)
    # source -- Last30DaysBrazil
    response3 = requests.get("https://disease.sh/v2/historical/brazil?lastdays=10")
    stats3 = json.loads(response3.content)


    # BrazilCases (getting)
    cases = stats['cases']
    recovered = stats['recovered']
    deaths = stats['deaths']

    # WorldCases (getting)
    casesW = stats2['cases']
    recoveredW = stats2['recovered']
    deathsW = stats2['deaths']

    # Getting Date
    today = date.today()
    d1 = today.strftime("%d.%m.%Y")

    #Gráfico 1
    plt.figure(num=None, figsize=(5, 5), dpi=100, facecolor='w', edgecolor='k')


    mes_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    casos_y = [50, 500, 1000, 3000, 5000, 8000, 20000, 60000, 60050, 65000, 70000, 80000]

    plt.plot(mes_x, casos_y)

    casos_total_y = [5, 55, 155, 455, 955, 1755, 3755, 9755, 15760, 22260, 29260, 37260]

    plt.plot(mes_x, casos_total_y)

    plt.xlabel('Mês')
    plt.ylabel('Total de casos')
    plt.title('Media de casos de COVID-19')

    plt.legend(['Casos no Brasil', 'Casos no Mundo'])
    plt.savefig("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/grafico.jpg")

    #plt.show()

    ## Pillow (criando imagem) -- Dados do Brasil
    image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
    font_type = ImageFont.truetype('arial.ttf', 23)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, 20), text=str(f'Casos no Brasil - {d1}'), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200,110), text=str(f"{cases}"), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200,200), text=str(recovered), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200,280), text=str(f"{deaths}"), fill=(255, 69, 0), font=font_type)
    #image.show()

    #Salvando a Imagem e convertendo
    rgb_im = image.convert('RGB')
    rgb_im.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/brazildata.jpg")

    ## Pillow (criando imagem) -- Dados do Mundo
    image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
    font_type = ImageFont.truetype('arial.ttf', 23)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, 20), text=str(f'Casos no Mundo - {d1}'), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200, 110), text=str(f"{casesW}"), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200, 200), text=str(recoveredW), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200, 280), text=str(f"{deathsW}"), fill=(255, 69, 0), font=font_type)
    #image.show()


    # Salvando a Imagem e convertendo
    rgb_im = image.convert('RGB')
    rgb_im.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/worlddata.jpg")


