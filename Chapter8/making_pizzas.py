# 利用import导入模块
# 导入整个模块，使用时要加模块名
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定函数，使用时不需要加模块名
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 使用as给模块指定别命，import pizza as p
# 使用as给函数指定别名，from pizza import make_pizza as p
# 导入模块中所有函数，from pizza import *
