from covid import Covid
from PIL import Image, ImageDraw, ImageFont

#source
covid = Covid(source="john_hopkins")

confirmed = covid.get_total_confirmed_cases()
#print(confirmed)

recovered = covid.get_total_recovered()
#print(recovered)

deaths = covid.get_total_deaths()
#print(deaths)


brazil_cases = covid.get_status_by_country_id(40)
#print(brazil_cases)

## Pillow (criando imagem)
image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
font_type = ImageFont.truetype('arial.ttf', 23)
draw = ImageDraw.Draw(image)
draw.text(xy=(180,170), text=str(confirmed), fill=(255,69,0), font=font_type)
draw.text(xy=(180,260), text=str(recovered), fill=(255,69,0), font=font_type)
draw.text(xy=(180,340), text=str(deaths), fill=(255,69,0), font=font_type)
image.show()
image.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/data.png")