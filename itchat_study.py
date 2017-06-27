# coding=utf-8

import itchat
from echarts import Echart, Legend, Pie

itchat.login()
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0

for friend in friends:
    sex = friend['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1


self = friends[0]
total = len(friends) - 1

male_rate = float(male) / total * 100
female_rate = float(female) / total * 100
other_rate = float(other) / total * 100

chart = Echart(u'{}的微信好友的性别比例'.format(self['NickName']), "from WeChat")
chart.use(Pie('WeChat', [
    {'value': male, 'name': u'男性 {:.2f}'.format(male_rate)},
    {'value': female, 'name': u'女性 {:.2f}'.format(female_rate)},
    {'value': other, 'name': u'其他 {:.2f}'.format(other_rate)}
]))
chart.use(Legend(['male', 'female', 'other']))
del chart.json['xAxis']
del chart.json['yAxis']
chart.plot()
