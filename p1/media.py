import requests


class Movie:
    ''' A movie class with some basic attributes of movies like:
    name, duration_time, movie_stars, post, trailer_url, release_time
    < ---- we can get the information from the GET request as following line
    http://m.maoyan.com/movie/249898.json
    '''

    def __init__(self, id):
        '''
        id: movie id in douban ; name: movie name
        '''
        self.id = id
        self.name = ''
        self.duration_time = 0
        self.poster_image_url = ''
        self.trailer_url = ''
        self.release_time = ''
        # get the all information now
        self.get_information()

    def get_information(self):
        '''get the movie info from moyan API'''
        info_url = "http://m.maoyan.com/movie/%d.json" % self.id
        info = requests.get(info_url)
        info_dict = info.json()['data']['MovieDetailModel']
        #set the attr
        self.name = info_dict['nm']
        self.duration_time = info_dict['dur']
        self.poster_image_url = info_dict['img']
        self.trailer_url = info_dict['vd']
        self.release_time = info_dict['rt']
