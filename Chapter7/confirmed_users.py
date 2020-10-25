# 创建一个待验证用户列表和一个存储已验证用户列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，知道没有未验证用户为止
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证用户
print("\nThe following userss have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())