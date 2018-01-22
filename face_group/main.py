import cognitive_face as CF
from config import DevConfig
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json
# import numpy as np
KEY = '861366de4321419f890f3a846162aaa4'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.

######################################################
# building dataset (每個人上傳一張照片當資料庫)
img_url = list()
for i in range(21):
	img_url.append('')
# print(img_url)
img_url[0] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27043323_1355346157908633_2064780505_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=ca7a722220d07112bedc0e511ae6f1b0&oe=5A6782C5' #JADE
img_url[1] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t35.0-12/27267392_1355346267908622_1898503042_o.jpg?_nc_ad=z-m&_nc_cid=0&oh=903c9900b3acffddb22053800fc70485&oe=5A675520' #余柏續
img_url[2] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/26996926_1355347631241819_1601843455_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=67ff31c7f5a9ecb564a2436519f83b65&oe=5A6765D5' #周一
img_url[3] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27042827_1355347641241818_1355861062_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=59777f5238bac071479f7aeb124f07a7&oe=5A676FB3' #林宗一
img_url[4] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27044447_1355349461241636_1209697459_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=2353d637853d9b30db5dc9432cd633e2&oe=5A679954' #林恆紹
img_url[5] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27157304_1355350824574833_1689159736_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=6b0052f96c894a14e6a36d79601a4155&oe=5A677275' #EP
img_url[6] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t35.0-12/27330004_1355350891241493_1291633704_o.jpg?_nc_ad=z-m&_nc_cid=0&oh=e163fd462afdb7706ebdc16f388489f6&oe=5A68751D' #修炎
img_url[7] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27152699_1355353997907849_1212475215_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=0ee160c2dd7ff5270411f09d272d9e7b&oe=5A686392' #孫凡雲
img_url[8] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27042954_1355354017907847_1298300211_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=cc5ad34da9cb6590d5735a5969443ed2&oe=5A678753' #徐嘉雲
img_url[9] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/26996668_1355354601241122_182821736_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=c7ccf1f7474e3ff942943f564b5e64ed&oe=5A6747F0' #徐應凱
img_url[10] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/26996462_1355354654574450_268448560_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=a1e9a2c9d2c33369348bf8afb13fa45a&oe=5A677293' #良舒翔
img_url[11] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27042909_1355355201241062_2135344390_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=e2b631e05f8b6650208606db304a985f&oe=5A678C63' #一涵
img_url[12] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27152884_1355355234574392_1322494018_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=4153cbaaacba7a878d4449f51b54e176&oe=5A685DA5' #陳於
img_url[13] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27042838_1355356027907646_289564853_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=4731a5d6fd8bc1a1b365dad4d9fa7bfe&oe=5A685B3D' #郵政驗
img_url[14] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/21641625_1355356071240975_2044136496_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=988e10fff3b2c2419ae862c6cad96bce&oe=5A672A91' #黃松仁
img_url[15] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/26996948_1355356674574248_623510786_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=e3d093e6b30e0708c97556c50e82f45a&oe=5A6730F3' #范如
img_url[16] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27043177_1355356731240909_1391950551_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=38e24c4e495c8c181abb9b23e23332d8&oe=5A67956A' #一恩
img_url[17] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/26996914_1355357667907482_1263654498_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=ae0eba87ffe36aa301a2129494846383&oe=5A685531' #聒聒
img_url[18] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27152848_1355357771240805_966127697_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=c7b77f6620d65e3f5bf46f84ab81adf7&oe=5A6729F7' #消擎軒
img_url[19] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27043177_1355356731240909_1391950551_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=38e24c4e495c8c181abb9b23e23332d8&oe=5A67956A' #一恩
img_url[20] = 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27044449_1355358361240746_373685910_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=4890147650db41043614bf69915d9823&oe=5A677656' #俊平


dataset_list = list()
for i in range(len(img_url)):
	face_id = (CF.face.detect(img_url[i]))
	dataset_list.append(face_id[0]["faceId"])

#print(dataset_list)	

######################################################
# 上傳一團體照，並切分出每個人的臉
img_allmsp= 'https://scontent-atl3-1.xx.fbcdn.net/v/t34.0-12/27042904_1355372177906031_1493537724_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=5eb3a1426d44ec49efc0bb5ef4989fc9&oe=5A67623D'	
faces = [CF.face.detect(img_allmsp)[i]['faceId'] for i in range(12)]
#print(faces)

######################################################
# 將資料庫及團體照整理出來的 faceId 合併
alllist = dataset_list + faces
#print(alllist)

######################################################
# 將合併完的 faceId 丟進 face API 的 group
subscription_key = '861366de4321419f890f3a846162aaa4'

uri_base = 'https://southcentralus.api.cognitive.microsoft.com'

body = {"faceIds":alllist}

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}
response = requests.request('POST', uri_base + '/face/v1.0/group', json=body, data=None, headers=headers, params=params)

print ('Response:')
parsed = json.loads(response.text)
print (json.dumps(parsed, sort_keys=True, indent=2))
