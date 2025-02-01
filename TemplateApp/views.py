from django.shortcuts import render

class Member:
    def __init__(self,id,name,join_at,picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Member(0,'Taro','2021/01/01','img/taro.jpg'),
    Member(1,'Jiro','2021/02/02','img/jiro.jpg'),
    Member(2,'Hanako','2021/03/03','img/hanako.jpg'),
    Member(3,'Yoshiko','2021/04/04','img/yoshiko.jpg'),
]

# ホーム画面
def home(request):
    return render(request, "home.html")

# メンバー一覧
def members(request):
    return render(request, "members.html",context={
        'members':member_list
    })

# メンバーの画面詳細
def member(request,id):
    return render(request, "member_detail.html",context={
        'member':member_list[id]
    })

