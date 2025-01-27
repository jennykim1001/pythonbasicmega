# albums=[]
# def singer(name, album):
#     albums.append(album)
#     return albums

# palbums=[]
# def singer1(name, album):
#     palbums.append(album)
#     return palbums

# bts = singer('BTS','1집')
# print(bts)
# bts = singer('BTS','2집')
# print(bts)
# bts = singer('BTS','3집')
# print(bts)

# bpink = singer1('BP','1집')
# print(bpink)

# 클래스 설계
class album_of_singer():
    # 속성, 변수
    def __init__(self,name):
        self.name = name
        self.albums=[]

    # 기능, 메서드
    def add_album(self,album):
        self.albums.append(album)
        return self.albums
    
bts = album_of_singer('BTS')
bts.add_album('1집')
bts.add_album('2집')
bts.add_album('3집')
print('BTS:',bts.albums)

bp = album_of_singer('BP')
bp.add_album('1집')
bp.add_album('2집')
print('BP:',bp.albums)

