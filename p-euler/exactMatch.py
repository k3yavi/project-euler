# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys   
import re
ip = sys.stdin.readlines()
# Work on data

tags = ['CREATE', 'UPDATE', 'DELETE', 'SEARCH']

iData = {}
c = 0

def displayId(key, Id):
    
    reg = r"(\s|^|$|[^\w'])"

    if 'tag:' in key:
        key = key[4:]
        if '*' in key:
            key = key[:-1]
            for k, v in iData.items():
                if key.lower() not in v['tag'].lower():
                    if k in Id:
                        Id.remove(k)
        else:
            for k,v in iData.items():
                if len(re.findall(reg + key + reg, v['tag'], flags = re.IGNORECASE)) <= 0:
                    if k in Id:
                        Id.remove(k)
        
    elif 'created:' in key:
        key = key[8:]
        for k, v in iData.items():
                if int(key) > int(v['created'][0:10].replace('-','')):
                    if k in Id:
                        Id.remove(k)
    else:
        if '*' in key:
            key = key[:-1]
            for k, v in iData.items():
                if key.lower() not in v['content'].lower():
                    if k in Id:
                        Id.remove(k)
        else:
            for k,v in iData.items():
                if len(re.findall(reg + key + reg, v['content'], flags = re.IGNORECASE)) <= 0:
                    if k in Id:
                        Id.remove(k)
    return Id

def search(key):
    
    dId = ''
    sortDict = {}
    c =[]
    Id = list(iData.keys())
    key = key.split()
    for x in range(len(key)):
        Id = displayId(key[x], Id)
    for x in Id:
        date = iData[x]['created'].replace('T','-').replace(':','-').replace('Z','')
        sortDict[x] = date
        
    for k,v in sorted(sortDict.items(), key=lambda x: x[1]):
        dId += k + ','
        
    return dId


def read(c):
    
    readline = ip[c].replace('\n','')
    c+=1
    data = {}
    while readline != '</note>':
        readline = ip[c].replace('\n','')
        c+=1
        if '<guid>' in readline:
            readline = readline.replace('<guid>','').replace('</guid>','')
            guid = readline.strip()
        elif '<created>' in readline:
            readline = readline.replace('<created>','').replace('</created>','')
            data['created'] = readline.strip()
        elif '<tag>' in readline:
            readline = readline.replace('<tag>','').replace('</tag>','')
            if 'tag' in data.keys():
                data['tag'] = data['tag'] + ' ' + readline.strip()
            else:
                data['tag'] = readline.strip()
        elif '<content>' in readline:
            readline = ip[c].replace('\n','')
            c+=1
            content = readline
            readline = ip[c].replace('\n','')
            c+=1
            while '</content>' not in readline:
                content += readline
                readline = ip[c].replace('\n','')
                c+=1
            data['content'] = content
        if 'tag' not in data.keys():
            data['tag'] = ''
    return (guid, data)
            
try:
    while (c<200000):
        in_tag = ip[c].replace('\n','')
        c+=1
        if in_tag == tags[0] :
            guid, data = read(c)
            iData[guid] = data
        elif in_tag == tags[1]:
            guid, data = read(c)
            del iData[guid]
            iData[guid] = data
        elif in_tag == tags[2]:
            guid = ip[c].replace('\n','')
            c+=1
            del iData[guid]
        elif in_tag == tags[3]:
            key = ip[c].replace('\n','')
            c+=1
            print search(key)[:-1]
except IndexError as e:
    print