
import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = 'xoxb-2218612794309-2221859854627-0A7IXYYuBRwhFDOrKMzaOtv4'
 
post_message(myToken,"#stock","Success")
