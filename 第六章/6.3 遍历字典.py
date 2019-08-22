user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
#.items分离键值
for key,value in user_0.items():
    print(key.title()+" "+value.title())

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'reward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys():
    print("参与调查的人有："+name.title())
if 'erin' not in name:
    print("为啥不参加调查呢? "+name.title())
#按照顺序列出键
for name in sorted(favorite_languages.keys()):
    print(name)


print("大家喜欢的编程语言有以下几种：")
for language in set(favorite_languages.values()):
    print(language)