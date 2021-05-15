import re
regex = '>.{0,}</h1>'
str = "<h1 class=\"title-article\" id=\"articleContentId\">ahhhhhh--哈哈</h1>"
ans = re.compile(regex).search(str)
ans = ans.__str__()
len = len(ans)
begin = ans.index("match")+8
print(ans[begin:len-7])
print(ans.strip().count("a"))