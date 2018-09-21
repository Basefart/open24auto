replacements = {"Heltidsstudier":"Halvtidsstudier", "100 %":"50 %", "100%":"50%", "heltid":"halvtid"}
def replacestring(strong):
    newstring = strong
    for k, v in replacements.items():
        newstring = newstring.replace(k, v)
    return newstring


originaldict = {'comment1': "Heltidsstudier på distans", "comment2": "heltid på distans", "comment3": "100 % distansstudier",
                    'comment4': "100% distansstudier"}
newdict = {}
for k, v in originaldict.items():
        newdict[k] = replacestring(v)
print(newdict)