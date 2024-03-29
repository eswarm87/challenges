import requests
import json

metadata_url = 'http://metadata.google.internal/computeMetadata/v1/'


def expand_jsontree(url, arr):
    result = {}
    for item in arr:
        new_url = url + item + '?recursive=true'
        r = requests.get(new_url,  headers={"Content-Type":"text"})
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            result[item[:-1]] = expand_jsontree(new_url, list_of_values)
        elif is_valid_json(text):
            result[item] = json.loads(text)
        else:
            result[item] = text
    return result


def metadata():
    path = ["instance/"]
    result = expand_jsontree(metadata_url, path)
    return result


def metadata_json():
    md = metadata()
    metadata_json = json.dumps(md, indent=4, sort_keys=True)
    return metadata_json


def is_valid_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(metadata_json())