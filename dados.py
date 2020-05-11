from covid import Covid
from PIL import Image, ImageDraw, ImageFont
import json

#source
covid = Covid(source="john_hopkins")

#GlobalCases
confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()


#BrazilCases (getting)
confirmedbr = json.loads(json.dumps(covid.get_status_by_country_name("Brazil")))
getdata = confirmedbr["confirmed"]

recoveredbr = json.loads(json.dumps(covid.get_status_by_country_name("Brazil")))
getdata2 = recoveredbr["recovered"]

deathsbr = json.loads(json.dumps(covid.get_status_by_country_name("Brazil")))
getdata3 = deathsbr["deaths"]

## Pillow (criando imagem) -- Dados Mundiais
image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
font_type = ImageFont.truetype('arial.ttf', 23)
draw = ImageDraw.Draw(image)
draw.text(xy=(170,20), text=str('Casos no Mundo'), fill=(255,69,0), font=font_type)
draw.text(xy=(180,110), text=str(confirmed), fill=(255,69,0), font=font_type)
draw.text(xy=(180,200), text=str(recovered), fill=(255,69,0), font=font_type)
draw.text(xy=(180,280), text=str(deaths), fill=(255,69,0), font=font_type)
image.show()
image.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/worlddata.png")

## Pillow (criando imagem) -- Dados do Brasil
image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
font_type = ImageFont.truetype('arial.ttf', 23)
draw = ImageDraw.Draw(image)
draw.text(xy=(170,20), text=str('Casos no Brasil'), fill=(255,69,0), font=font_type)
draw.text(xy=(180,110), text=str(getdata), fill=(255,69,0), font=font_type)
draw.text(xy=(180,200), text=str(getdata2), fill=(255,69,0), font=font_type)
draw.text(xy=(180,280), text=str(getdata3), fill=(255,69,0), font=font_type)
image.show()
image.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/brazildata.png")

