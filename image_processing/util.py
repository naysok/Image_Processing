#########################################################
### Utilities                                         ###
###                                                   ###
###                                                   ###
#########################################################


import math


class UTIL():


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def split_list(self, l, n):

        # https://www.python.ambitious-engineer.com/archives/1843 
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]

        return l


    def list_to_2d_array(self, l):

        num = int(math.sqrt(len(l)))
        # print("sqrt : {}".format(num))

        array_2d = list(self.split_list(l, num))
        # print("i_count : {}".format(len(array_2d)))
        # print("j_count : {}".format(len(array_2d[0])))

        return array_2d
