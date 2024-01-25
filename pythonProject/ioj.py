from yandex_music import Client
client = Client("y0_AgAAAABk0xPPAAG8XgAAAAD45Ntf5Gmgg8K_Sw2TUefClukvbJJygh4")
client.init()

client.users_likes_tracks()[0].fetch_track().download('example.mp3')
print (client.users_likes_tracks()[0].fetch_track())


def  search(trak_name):
    search_result=client.search(trak_name)

    if search_result.best:
        type_ = search_result.best.type
        best = search_result.best.result
        if type_ != "track":
            return None
        else:
            return best

def trakc_like(track_name):
    if search(track_name)!=None:
        client.userslikesTracksRemove(search(track_name)['id'])
        print('hkgkfgk')


def trakc_dislike(track_name):
    if search(track_name)!=None:
        client.usersLikesTracksAdd(search(track_name)['id'])
        print('hkgkfgk')
