import json
import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def generator ():
    plt.figure(num=None, figsize=(5, 5), dpi=100, facecolor='w', edgecolor='k')

    response = requests.get("https://disease.sh/v2/countries/brazil")

    stats = json.loads(response.content)

    print(stats['cases'], stats['todayCases'])

    mes_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    casos_y = [50, 500, 1000, 3000, 5000, 8000, 20000, 60000, 60050, 65000, 70000, 80000]

    plt.plot(mes_x, casos_y)

    casos_total_y = [5, 55, 155, 455, 955, 1755, 3755, 9755, 15760, 22260, 29260, 37260]

    plt.plot(mes_x, casos_total_y)

    plt.xlabel('Mês')
    plt.ylabel('Total de casos')
    plt.title('Media de casos de COVID-19')

    plt.legend(['Casos no Brazil', 'Casos no mundo'])
    plt.savefig("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/grafico.jpg")

    #plt.show()

    # source -- Brazil
    response = requests.get("https://disease.sh/v2/countries/brazil")
    stats = json.loads(response.content)

    # source -- World
    response2 = requests.get("https://corona.lmao.ninja/v2/all")
    stats2 = json.loads(response2.content)

    # BrazilCases (getting)
    cases = stats['cases']
    todayCases = stats['todayCases']
    recovered = stats['recovered']
    deaths = stats['deaths']
    todayDeaths = stats['todayDeaths']
    # WorldCases (getting)
    casesW = stats2['cases']
    todayCasesW = stats2['todayCases']
    recoveredW = stats2['recovered']
    deathsW = stats2['deaths']
    todayDeathsW = stats2['todayDeaths']

    ## Pillow (criando imagem) -- Dados do Brasil
    image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
    font_type = ImageFont.truetype('arial.ttf', 23)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(140, 20), text=str('Casos no Brasil'), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(160, 110), text=str(f"{cases}      +{todayCases}"), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200, 200), text=str(recovered), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(160, 280), text=str(f"{deaths}      +{todayDeaths}"), fill=(255, 69, 0), font=font_type)
    #image.show()
    rgb_im = image.convert('RGB')
    rgb_im.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/brazildata.jpg")

    ## Pillow (criando imagem) -- Dados do Mundo
    image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
    font_type = ImageFont.truetype('arial.ttf', 23)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(140, 20), text=str('Casos no Mundo'), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(160, 110), text=str(f"{casesW}      +{todayCasesW}"), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(200, 200), text=str(recoveredW), fill=(255, 69, 0), font=font_type)
    draw.text(xy=(160, 280), text=str(f"{deathsW}      +{todayDeathsW}"), fill=(255, 69, 0), font=font_type)
    #image.show()
    rgb_im = image.convert('RGB')
    rgb_im.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/worlddata.jpg")
