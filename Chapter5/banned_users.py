banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
#检查特定值是否不包含于列表
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
