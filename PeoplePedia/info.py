import json
import os
from django.shortcuts import render_to_response

def infobox(request):
    index = request.GET.get('n')
    path = '/Users/yw-zhang/Desktop/Desk/crawl/infobox_copy'
    file_name = index + '.json'
    file_path = os.path.join(path, file_name)
    with open(file_path) as file:
        dict = json.load(file)
    name = dict['id']
    imgsrc = None
    if 'imgsrc' in dict:
        imgsrc = dict['imgsrc']
    list = {}
    for key,value in dict.items():
        if key != 'id' and key != 'imgsrc':
            list[key] = value
    return render_to_response('info.html', {'name': name, 'imgsrc' : imgsrc, 'list': list})
