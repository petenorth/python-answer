import jmespath, json

def extract(key, object): 

    jsondata = json.loads(object)

    return jmespath.search(key.replace('/', '.'), jsondata)

if __name__ == "__main__":
    import sys
    print(extract(sys.argv[2], sys.argv[1]))
