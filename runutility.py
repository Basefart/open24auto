from Open24Utility import Open24Utility

coursenames, ccabb = Open24Utility.getcourselist()
ind = 0
for cn in coursenames:
    print(cn.text, ccabb[ind].text)
    ind = ind + 1