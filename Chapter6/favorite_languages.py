favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          favorite_languages['sarah'].title() + ".")

#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
print("\n")
#遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())
print("\n")
#利用 集合set 获取不重复的列表
for language in set(favorite_languages.values()):
    print(language.title())