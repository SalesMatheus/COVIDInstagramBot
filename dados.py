from PIL import Image, ImageDraw, ImageFont
import json, requests

#source
response = requests.get("https://disease.sh/v2/countries/brazil")
stats = json.loads(response.content)


#BrazilCases (getting)
cases = stats['cases']
todayCases = stats['todayCases']
recovered = stats['recovered']
deaths = stats['deaths']

## Pillow (criando imagem) -- Dados do Brasil
image = Image.open('/Users/DinoPC/PyCharmProjects/COVIDBot/Images/template.png')
font_type = ImageFont.truetype('arial.ttf', 23)
draw = ImageDraw.Draw(image)
draw.text(xy=(140,20), text=str('Casos no Brasil'), fill=(255,69,0), font=font_type)
draw.text(xy=(160,110), text=str(f"{cases}      +{todayCases}"), fill=(255,69,0), font=font_type)
draw.text(xy=(200,200), text=str(recovered), fill=(255,69,0), font=font_type)
draw.text(xy=(200,280), text=str(deaths), fill=(255,69,0), font=font_type)
image.show()
rgb_im = image.convert('RGB')
rgb_im.save("/Users/DinoPC/PyCharmProjects/COVIDBot/BotUploads/brazildata.jpg")

