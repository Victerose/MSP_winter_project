import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '861366de4321419f890f3a846162aaa4'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://southcentralus.api.cognitive.microsoft.com'

# Request headers.
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

input1 = input();
input2 = input();


# Body. The URL of a JPEG image to analyze.
body1 = {'url': input1}
body2 = {'url': input2}
#body1 = {'url': 'https://scontent-ort2-2.xx.fbcdn.net/v/t34.0-12/26943619_1353930981383484_1213390003_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=dc6d6f70eee7f332c9fecaf85b294732&oe=5A654B59'}
#body2 = {'url': 'https://scontent-ort2-2.xx.fbcdn.net/v/t34.0-12/26995207_1353907708052478_1686892688_n.jpg?_nc_ad=z-m&_nc_cid=0&oh=ccfd107bffa44cb3e082dbbac97b718e&oe=5A6565EF'}


try:
    # Execute the REST API call and get the response.
    response1 = requests.request('POST', uri_base + '/face/v1.0/detect', json=body1, data=None, headers=headers, params=params)
    response2 = requests.request('POST', uri_base + '/face/v1.0/detect', json=body2, data=None, headers=headers, params=params)

    #print ('Response:')
    parsed1 = json.loads(response1.text)
    parsed2 = json.loads(response2.text)

    body = {"faceId1":parsed1[0]['faceId'], "faceId2":parsed2[0]['faceId']}

    response = requests.request('POST', uri_base + '/face/v1.0/verify', json=body, data=None, headers=headers, params=params)

    print ('Response:')
    parsed = json.loads(response.text)
    print (json.dumps(parsed, sort_keys=True, indent=2))
    #print (json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e:
    print('Error:')
    print(e)

####################################  