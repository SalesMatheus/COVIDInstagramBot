import matplotlib.pyplot as plt
import json, requests

response = requests.get("https://disease.sh/v2/countries/brazil")

stats = json.loads(response.content)

print(stats['cases'], stats['todayCases'])

plt.plot([1,2,3,4] , [4,7,8,12])

#plt.savefig('covidGrafico.png')

plt.show()