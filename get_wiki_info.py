import requests
import json
import feedparser
import nltk
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')

def getWikiPages(subject):
    searchUrl = "https://en.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srlimit=1&srsearch="+subject
    response = requests.get(searchUrl).json()
    jsonString = json.dumps(response, indent=2)

    jsonDict= json.loads(jsonString)
    
    return jsonDict["query"]["search"][0]["title"]

def getWikiData(page):
    searchUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=1&exintro=1&titles="+page
    response = requests.get(searchUrl).json()
    jsonString = json.dumps(response, indent=2)

    jsonDict= json.loads(jsonString)

    for element in jsonDict["query"]["pages"]:
        
        return str.rstrip(jsonDict["query"]["pages"][element]["extract"])

def getSubjects(data):

    subjects=[]

    tagged_sent = pos_tag(data.split())

    for i, (word,tag) in enumerate(tagged_sent):
                
        if tag == 'NNP':
            if i == 0:
                subjects.append(word)
            else:
                if tagged_sent[i-1][1] == 'NNP':
                    subjects[len(subjects)-1] = subjects[len(subjects)-1]+" "+word
                else:
                    subjects.append(word)

    return subjects



