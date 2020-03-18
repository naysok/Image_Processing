#########################################################
### Utilities                                         ###
###                                                   ###
###                                                   ###
#########################################################


import math
import datetime



class UTIL():


    def get_current_time(self):

        now = datetime.datetime.now()
        # print("Current Time : {}".format(now))

        ### format
        f_year = "%04d"%now.year
        f_month = "%02d"%now.month
        f_day = "%02d"%now.day
        f_hour = "%02d"%now.hour
        f_min = "%02d"%now.minute
        f_sec = "%02d"%now.second

        return f_year, f_month, f_day, f_hour, f_min, f_sec


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
