
import pandas as pd


def getUniversities(countryName):
    import universities
    df = pd.DataFrame(columns = [countryName])
    uni = universities.API() 
    universities = uni.search(country = countryName)
    df[countryName] = [x.name for x in universities]
    df.to_csv(countryName+'.csv')
    return df

df = getUniversities('Korea, Republic of')
df

import universities
uni = universities.API() 
x = uni.lucky(name = "Korea")
x.name
x.country