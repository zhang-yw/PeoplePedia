import json
from django.shortcuts import render_to_response
from collections import OrderedDict
import time
import os

def not_empty(s):
    return s and s.strip()


class Entry(object):
    def __init__(self, index, name, llist):
        self.index = index
        self.name = name
        self.llist = llist

class Essrntial(object):
    def __init__(self, front, middle, end):
        self.front = front
        self.middle = middle
        self.end = end

def getlist_jiao(words, path):
    if words == '':
        list_0 = []
        return list_0
    word_list = words.split(' ')
    word_list = list(filter(not_empty, word_list))
    with open(path) as file:
        dict = json.load(file)
    set_0 = set()
    for i in word_list:
        if i in dict:
            set_2 = set(dict[i])
            if len(set_0) == 0:
                set_0 = set_2
            else:
                set_0 = set_0 & set_2
    list_2 = list(set_0)
    return list_2

def first(request):
    start = time.clock()
    keywords = request.GET.get('keywords', '')
    name = request.GET.get('name', '')
    born = request.GET.get('born', '')
    died = request.GET.get('died', '')
    almamater = request.GET.get('almamater', '')
    page = request.GET.get('page', '')
    search_0 = request.GET.get('search', '')
    keywords_path = '/Users/yw-zhang/Desktop/Desk/crawl/text_list.json'
    name_path = '/Users/yw-zhang/Desktop/Desk/crawl/name_list.json'
    born_path = '/Users/yw-zhang/Desktop/Desk/crawl/born_list.json'
    died_path = '/Users/yw-zhang/Desktop/Desk/crawl/died_list.json'
    almamater_path = '/Users/yw-zhang/Desktop/Desk/crawl/alma_mater_list.json'
    if keywords != '':
        list_0 = getlist_jiao(keywords, keywords_path)
        print len(list_0)
        print '----------------'
        list_1 = getlist_bing(keywords, keywords_path)
        print len(list_1)
        print '-----------------'
        list_0.extend(list_1)
        list_all = list_0
        print list_all
    else:
        name_set = set(getlist_jiao(name, name_path))
        born_set = set(getlist_jiao(born, born_path))
        died_set = set(getlist_jiao(died, died_path))
        almamater_set = set(getlist_jiao(almamater, almamater_path))
        set_0 = set()
        if len(name_set) != 0:
            if len(set_0) == 0:
                set_0 = name_set
            else:
                set_0 = name_set & set_0
        if len(born_set) != 0:
            if len(set_0) == 0:
                set_0 = born_set
            else:
                set_0 = born_set & set_0
        if len(died_set) != 0:
            if len(set_0) == 0:
                set_0 = died_set
            else:
                set_0 = died_set & set_0
        if len(almamater_set) != 0:
            if len(set_0) == 0:
                set_0 = almamater_set
            else:
                set_0 = almamater_set & set_0
        list_all = list(set_0)
    items = 5
    if list_all is not None:
        pages = len(list_all) / items
        if len(list_all) % items != 0:
            pages = pages + 1
    else:
        pages = 0
    dict_1 = OrderedDict()
    list_pages = []
    if page == '':
        page = str(1)
    if page != '':
        page = int(page)
        list_final = list_all[items * (page - 1):items * page]
        with open('/Users/yw-zhang/Desktop/Desk/crawl/index_name.json') as file:
            dict_l = json.load(file)
        for i in list_final:
            dict_1[i] = dict_l[i]
        for i in range(pages):
            list_pages.append(i + 1)
    end = time.clock()
    if search_0 != '':
        time_0 = end - start
    else:
        time_0 = None
    list_modified = []
    for key, value in dict_1.items():
        index_0 = key
        name_0 = value
        path = '/Users/yw-zhang/Desktop/Desk/crawl/infobox_copy'
        file_name = index_0 + '.json'
        file_path = os.path.join(path, file_name)
        with open(file_path) as file:
            dict_0 = json.load(file)
        if keywords != '':
            keywords_list = keywords.split(' ')
            keywords_list = list(filter(not_empty, keywords_list))
            llist_0 = []
            for key_0, value_0 in dict_0.items():
                if key_0 != 'imgsrc':
                    for ii in keywords_list:
                        if value_0.find(ii) != -1:
                            if key_0 == 'id':
                                heads = 'name'
                            else:
                                heads = key_0
                            posi = value_0.find(ii)
                            front_1 = value_0[0:posi]
                            middle_0 = ii
                            posi_2 = posi + len(ii)
                            end_0 = value_0[posi_2:]
                            front_0 = heads + ': ' + front_1
                            essen = Essrntial(front_0, middle_0, end_0)
                            llist_0.append(essen)
            entry_0 = Entry(index_0, name_0, llist_0)
            list_modified.append(entry_0)
        else:
            llist_0 = []
            for key_0, value_0 in dict_0.items():
                if name != '':
                    if key_0 == 'id':
                        heads = 'Name: '
                        posi = value_0.find(name)
                        front_1 = value_0[0:posi]
                        middle_0 = name
                        posi_2 = posi + len(name)
                        end_0 = value_0[posi_2:]
                        front_0 = heads + front_1
                        essen = Essrntial(front_0, middle_0, end_0)
                        llist_0.append(essen)
                if born != '':
                    if key_0 == 'Born':
                        heads = 'Born: '
                        posi = value_0.find(born)
                        front_1 = value_0[0:posi]
                        middle_0 = born
                        posi_2 = posi + len(born)
                        end_0 = value_0[posi_2:]
                        front_0 = heads + front_1
                        essen = Essrntial(front_0, middle_0, end_0)
                        llist_0.append(essen)
                if died != '':
                    if key_0 == 'Died':
                        heads = 'Died: '
                        posi = value_0.find(died)
                        front_1 = value_0[0:posi]
                        middle_0 = died
                        posi_2 = posi + len(died)
                        end_0 = value_0[posi_2:]
                        front_0 = heads + front_1
                        essen = Essrntial(front_0, middle_0, end_0)
                        llist_0.append(essen)
                if almamater != '':
                    if key_0 == 'Alma mater':
                        heads = 'Alma mater: '
                        posi = value_0.find(almamater)
                        front_1 = value_0[0:posi]
                        middle_0 = almamater
                        posi_2 = posi + len(almamater)
                        end_0 = value_0[posi_2:]
                        front_0 = heads + front_1
                        essen = Essrntial(front_0, middle_0, end_0)
                        llist_0.append(essen)
            entry_0 = Entry(index_0, name_0, llist_0)
            list_modified.append(entry_0)
    if search_0 != '':
        return render_to_response('search.html',
                              {'time': time_0, 'keywords': keywords, 'name': name, "born": born, "died": died,
                               "almamater": almamater, "list_1": list_modified, "list_2": list_pages})
    else:
        return render_to_response('firstpage.html')