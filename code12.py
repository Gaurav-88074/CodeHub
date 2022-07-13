from bs4 import BeautifulSoup
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
# link for extract html data
def getdata(url):
    r = requests.get(url, headers=headers)
    return r.text

# htmldata = getdata("https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/%22")
htmldata = getdata("https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/")

soup = BeautifulSoup(htmldata, 'html.parser')

divData = soup.find("div",class_ = "td-post-content")
print(divData.getText())

# allweb = []
# allTagList = set([
#     '<a>', '<abbr>', '<address>', '<area>', '<article>', '<aside>', '<audio>', '<b>', '<bdi>', '<bdo>', '<blockquote>', '<body>', '<br>', '<button>', '<canvas>', '<caption>', '<cite>', '<code>', '<col>', '<colgroup>', '<command>', '<datalist>', '<dd>', '<del>', '<details>', '<dfn>', '<div>', '<dl>', '<dt>', '<em>', '<embed>', '<fieldset>', '<figcaption>', '<figure>', '<footer>', '<form>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<header>', '<hr>', '<html>', '<i>', '<iframe>', '<img>', '<input>', '<ins>', '<kbd>', '<keygen>', '<label>', '<legend>', '<li>', '<main>', '<map>', '<mark>', '<menu>', '<meter>', '<nav>', '<object>', '<ol>', '<optgroup>', '<option>', '<output>', '<p>', '<param>', '<pre>', '<progress>', '<q>', '<rp>', '<rt>', '<ruby>', '<s>', '<samp>', '<section>', '<select>', '<small>', '<source>', '<span>', '<strong>', '<sub>', '<summary>', '<sup>', '<table>', '<tbody>', '<td>', '<textarea>', '<tfoot>', '<th>', '<thead>', '<time>', '<tr>', '<track>', '<u>', '<ul>', '<var>'])
# def getTagName(tagName):
#     actualTag= []
#     for i in tagName:
#         actualTag.append(i)
#         if i==">":
#             break
#         if i==" ":
#             actualTag.pop()
#             actualTag.append(">")
#             break
#     return ("".join(actualTag))
# def fetchData(divData):
#     for tag in divData:
#         tagName = list(str(tag)[0:20])
#         actualTag = getTagName(tagName)
#         if actualTag in allTagList:
#             allweb.append(tag.get_text())
#             # fetchData(tag)
        
# fetchData(divData)
# print(*allweb,sep ="\n==========================\n")

# paragraphData = []
# for tags in divData:

#     htmlTag = str(tags)[0:3]
#     # print(htmlTag)
#     if  htmlTag== "<p>":
#         # print(tags)
#         paragraphData.append(tags.get_text())
#     elif htmlTag =="<ul":
#         for liTag in tags.find_all("li"):
#             # print(liTag)
#             liTagData = tags.get_text()
#             if liTagData not in hashSet:
#                 hashSet.add(liTagData)
#                 paragraphData.append(liTagData)
# print(*paragraphData,sep="\n==========\n")
# soup.findParent
# for ulTag in divData .find_all('ul'):
#     for liTag in ulTag.find_all("li"):
#         print(liTag.getText())
#         print("-----------------")





# divDataString = ""
# for i in divData:
#     divDataString+=str(i)

# soupUl = BeautifulSoup(divDataString, 'html.parser')
# dataUl = soupUl.find("ul")
# print(dataUl)

