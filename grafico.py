import json
import requests

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
    plt.savefig("D:/Dev/Projetos/Covid/COVIDInstagramBot/img/grafico.jpg")

    plt.show()