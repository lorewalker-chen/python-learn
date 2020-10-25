#字典用{'键':'值'}表示
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#添加键值对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#修改值
alien_0['color']='yellow'
print(alien_0)
#删除键值对
del alien_0['x_position']
print(alien_0)