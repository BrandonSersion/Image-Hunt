from django.db import models

import requests
board = ("an")
last_time = 1512677076999

# Create your models here.
class Image(models.Model):
    image = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

    def __str__(self):
        return str(self.image)

class Post(models.Model):
    imagefk = models.ForeignKey(Image, on_delete=models.CASCADE)
    tim = models.IntegerField()
    ext = models.CharField(max_length=4)
    time = models.IntegerField()
    fsize = models.IntegerField()

    def __str__(self):
        return str(self.tim)

# class Thumbnail(models.Model):
#     images = models.OneToOneField(
#         Image,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     tn_w = models.IntegerField()
#     tn_w = models.IntegerField()
    

# API
class ApiThreadList:
    def __init__(self, board):
        self.board = board

    def getThreadList(self):
        request = "https://a.4cdn.org/{}/threads.json".format(self.board)
        thread_list = requests.get(request)
        self.parseThreadList(thread_list.json())
        #test json = [{'page': 1, 'threads': [{'no': 396534925, 'last_modified': 1510449633}, {'no': 396535501, 'last_modified': 1510449633}, {'no': 396522079, 'last_modified': 1510449632}, {'no': 396513653, 'last_modified': 1510449632}, {'no': 396520225, 'last_modified': 1510449632}, {'no': 396537259, 'last_modified': 1510449631}, {'no': 396507090, 'last_modified': 1510449629}, {'no': 396537559, 'last_modified': 1510449630}, {'no': 396523087, 'last_modified': 1510449628}, {'no': 396494558, 'last_modified': 1510449628}, {'no': 396524157, 'last_modified': 1510449627}, {'no': 396536954, 'last_modified': 1510449626}, {'no': 396538302, 'last_modified': 1510449626}, {'no': 396533231, 'last_modified': 1510449626}, {'no': 396521090, 'last_modified': 1510449624}]}, {'page': 2, 'threads': [{'no': 396530294, 'last_modified': 1510449632}, {'no': 396534434, 'last_modified': 1510449621}, {'no': 396535716, 'last_modified': 1510449620}, {'no': 396534351, 'last_modified': 1510449620}, {'no': 396516952, 'last_modified': 1510449619}, {'no': 396533179, 'last_modified': 1510449618}, {'no': 396538980, 'last_modified': 1510449617}, {'no': 396535470, 'last_modified': 1510449617}, {'no': 396492085, 'last_modified': 1510449613}, {'no': 396498158, 'last_modified': 1510449612}, {'no': 396534701, 'last_modified': 1510449610}, {'no': 396531243, 'last_modified': 1510449610}, {'no': 396531435, 'last_modified': 1510449608}, {'no': 396527073, 'last_modified': 1510449604}, {'no': 396533575, 'last_modified': 1510449605}]}, {'page': 3, 'threads': [{'no': 396515428, 'last_modified': 1510449605}, {'no': 396536839, 'last_modified': 1510449602}, {'no': 396536857, 'last_modified': 1510449598}, {'no': 396521541, 'last_modified': 1510449597}, {'no': 396530332, 'last_modified': 1510449595}, {'no': 396537869, 'last_modified': 1510449595}, {'no': 396534576, 'last_modified': 1510449594}, {'no': 396532919, 'last_modified': 1510449592}, {'no': 396525305, 'last_modified': 1510449592}, {'no': 396538683, 'last_modified': 1510449592}, {'no': 396533480, 'last_modified': 1510449590}, {'no': 396534237, 'last_modified': 1510449589}, {'no': 396533415, 'last_modified': 1510449587}, {'no': 396535913, 'last_modified': 1510449586}, {'no': 396535309, 'last_modified': 1510449579}]}, {'page': 4, 'threads': [{'no': 396503638, 'last_modified': 1510449577}, {'no': 396535586, 'last_modified': 1510449574}, {'no': 396537428, 'last_modified': 1510449573}, {'no': 396490561, 'last_modified': 1510449572}, {'no': 396536931, 'last_modified': 1510449572}, {'no': 396515817, 'last_modified': 1510449572}, {'no': 396538081, 'last_modified': 1510449570}, {'no': 396537742, 'last_modified': 1510449569}, {'no': 396538768, 'last_modified':1510449567}, {'no': 396530389, 'last_modified': 1510449567}, {'no': 396527020, 'last_modified': 1510449564}, {'no': 396537039, 'last_modified': 1510449564}, {'no': 396535931, 'last_modified': 1510449559}, {'no': 396528990, 'last_modified': 1510449555}, {'no': 396533329, 'last_modified': 1510449551}]}, {'page': 5, 'threads': [{'no': 396538974, 'last_modified': 1510449549}, {'no': 396530990, 'last_modified': 1510449547}, {'no': 396533910, 'last_modified': 1510449544}, {'no': 396533697, 'last_modified': 1510449538}, {'no': 396536889, 'last_modified': 1510449539}, {'no': 396538462, 'last_modified': 1510449537}, {'no': 396538951, 'last_modified': 1510449535}, {'no': 396535714, 'last_modified': 1510449565}, {'no': 396530997, 'last_modified': 1510449530}, {'no': 396522293, 'last_modified': 1510449526}, {'no': 396518802, 'last_modified': 1510449527}, {'no': 396523194, 'last_modified': 1510449526}, {'no': 396492838, 'last_modified': 1510449523}, {'no': 396533631, 'last_modified': 1510449521}, {'no': 396537931, 'last_modified': 1510449513}]}, {'page': 6, 'threads': [{'no': 396507216, 'last_modified': 1510449509}, {'no': 396536249, 'last_modified': 1510449503}, {'no': 396536678, 'last_modified': 1510449503}, {'no': 396535251, 'last_modified': 1510449503}, {'no': 396538876, 'last_modified': 1510449593}, {'no': 396534326, 'last_modified': 1510449491}, {'no': 396537345, 'last_modified': 1510449484}, {'no': 396527181, 'last_modified': 1510449483}, {'no': 396532240, 'last_modified': 1510449478}, {'no': 396538848, 'last_modified': 1510449478}, {'no': 396538173, 'last_modified': 1510449473}, {'no': 396538834, 'last_modified': 1510449467}, {'no': 396529812, 'last_modified': 1510449455}, {'no': 396532489, 'last_modified': 1510449453}, {'no': 396486865, 'last_modified': 1510449446}]}, {'page': 7, 'threads': [{'no': 396532903, 'last_modified': 1510449445}, {'no': 396538389, 'last_modified': 1510449442}, {'no': 396538090, 'last_modified': 1510449428}, {'no': 396538096, 'last_modified': 1510449424}, {'no': 396536668, 'last_modified': 1510449421}, {'no': 396523334, 'last_modified': 1510449411}, {'no': 396494476, 'last_modified': 1510449410}, {'no': 396534708, 'last_modified': 1510449397}, {'no': 396529078, 'last_modified': 1510449391}, {'no': 396536612, 'last_modified': 1510449388}, {'no': 396504987, 'last_modified': 1510449374}, {'no': 396529606, 'last_modified': 1510449368}, {'no': 396538589, 'last_modified': 1510449332}, {'no': 396533079, 'last_modified': 1510449325}, {'no': 396537443, 'last_modified': 1510449322}]}, {'page': 8, 'threads': [{'no': 396521085, 'last_modified': 1510449320}, {'no': 396538559, 'last_modified': 1510449317}, {'no': 396535247, 'last_modified': 1510449311}, {'no': 396482759, 'last_modified': 1510449616}, {'no': 396538506, 'last_modified': 1510449277}, {'no': 396534251, 'last_modified': 1510449272}, {'no': 396538459, 'last_modified': 1510449522}, {'no': 396532136, 'last_modified': 1510449250}, {'no': 396538445, 'last_modified': 1510449243}, {'no': 396536967, 'last_modified': 1510449223}, {'no': 396538223, 'last_modified': 1510449304}, {'no': 396538356, 'last_modified': 1510449193}, {'no': 396538349, 'last_modified': 1510449358}, {'no': 396526597, 'last_modified': 1510449177}, {'no': 396506997, 'last_modified': 1510449154}]}, {'page': 9, 'threads': [{'no': 396505229, 'last_modified': 1510449120}, {'no': 396523632, 'last_modified': 1510449113}, {'no': 396536216, 'last_modified': 1510449089}, {'no': 396537985, 'last_modified': 1510449075}, {'no': 396537165, 'last_modified': 1510449073}, {'no': 396533015, 'last_modified': 1510449016}, {'no': 396537930, 'last_modified': 1510449422}, {'no': 396525035, 'last_modified': 1510448960}, {'no': 396535491, 'last_modified': 1510448985}, {'no': 396536415, 'last_modified': 1510448929}, {'no': 396537895, 'last_modified': 1510448904}, {'no': 396537887, 'last_modified':1510448902}, {'no': 396537605, 'last_modified': 1510448899}, {'no': 396537175, 'last_modified': 1510448895}, {'no': 396536008, 'last_modified': 1510448871}]}, {'page': 10, 'threads': [{'no': 396534793, 'last_modified': 1510448867}, {'no': 396533968, 'last_modified': 1510448829}, {'no': 396537332,'last_modified': 1510448821}, {'no': 396535968, 'last_modified': 1510448784}, {'no': 396537431, 'last_modified': 1510448760}, {'no': 396520920, 'last_modified': 1510448743}, {'no': 396537606, 'last_modified': 1510448723}, {'no': 396535791, 'last_modified': 1510448647}, {'no': 396537475, 'last_modified': 1510449164}, {'no': 396500595, 'last_modified': 1510448639}, {'no': 396532980, 'last_modified': 1510448599}, {'no': 396492556, 'last_modified': 1510448585}, {'no': 396537207, 'last_modified': 1510448656}, {'no': 396536134, 'last_modified': 1510448445}, {'no': 396535831, 'last_modified': 1510448435}]}] 
        
    def parseThreadList(self, thread_list_r):
        for i in thread_list_r:
            for j in i['threads']:
                last_modified = j["last_modified"]
                if last_modified >= last_time:
                    no = j["no"]
                    get_thread = ApiThread(self.board, no)
                    get_thread.getThread()
                #else:
                    #last_time = last_modified
                    #continue

class ApiThread:
    def __init__(self, board, no):
        self.board = board
        self.no = no

    def getThread(self):
        request = "https://a.4cdn.org/{}/thread/{}.json".format(self.board, self.no)
        thread = requests.get(request)
        self.parseThread(thread.json())

    def parseThread(self, thread_r):
        for i in reversed(thread_r['posts']):
            if 'filename' in i:
                tim = i['tim']
                ext = i['ext']
                w = i['w']
                h = i['h']
                tn_w = i['tn_w']
                tn_h = i['tn_h']
                time = i['time']
                fsize = i['fsize']
                # if time <= last_time:
                #     break
                get_image = ApiImage(self.board, self.no, tim, ext, w, h, tn_w, tn_h, time, fsize)
                get_image.getImage()

class ApiImage:
    def __init__(self, board, no, tim, ext, w, h, tn_w, tn_h, time, fsize):
        self.board = board
        self.no = no
        self.tim = tim
        self.ext = ext
        self.w = w
        self.h = h
        self.tn_w = tn_w
        self.tn_h = tn_h
        self.time = time
        self.fsize = fsize

    def getImage(self):
        request = "https://i.4cdn.org/{}/{}{}".format(self.board, self.tim, self.ext)
        print(self.time)
        img_data = requests.get(request).content
        file_name = "./api/static/api/img/{}{}".format(self.tim, self.ext)
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        self.databaseInsert()
        
    def databaseInsert(self):
        image_instance = Image(image=self.no, w=self.w, h=self.h)
        image_instance.save()
        post_instance = Post(imagefk=image_instance, tim=self.tim, ext=self.ext, time=self.time, fsize=self.fsize)
        post_instance.save()

get_thread_list = ApiThreadList(board)
thread_list = get_thread_list.getThreadList()