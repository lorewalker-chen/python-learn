def print_models(unprinted_designs, completed_models):
    # 模拟打印每个设计，直到没有未打印的设计为止
    # 打印每个设计后，都将其移到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计打印的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # 显示打印好的所有模型
    print("\nThe following models have been printed:")
    for completed_models in completed_models:
        print(completed_models)


# 创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 禁止函数修改列表，利用切片
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)