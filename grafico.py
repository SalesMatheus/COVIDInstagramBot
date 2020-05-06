import matplotlib.pyplot as plt
import json, requests

response = requests.get("https://disease.sh/v2/countries/brazil")

stats = json.loads(response.content)

print(stats['cases'], stats['todayCases'])

mes_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

casos_y = [5, 50, 100, 300, 500, 800, 2000, 6000, 6005, 6500, 7000, 8000]

plt.plot(mes_x, casos_y)

casos_total_y = [5, 55, 155, 455, 955, 1755, 3755, 9755, 15760, 22260, 29260, 37260]

plt.plot(mes_x, casos_total_y)

plt.xlabel('Mês')
plt.ylabel('Total de casos')
plt.title('Media de casos de COVID-19')

plt.legend(['Casos no Brazil', 'Casos no mundo'])
#plt.savefig('covidGrafico.png')

plt.show()