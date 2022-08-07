import requests
import emoji

def add_reaction(emoji):
    headers = {
        'authorization' : 'token'
        #replace 'token' with authorization token taken from developer console - Library > Headers once you have logged in
    }
    r = requests.put(
        f'https://discord.com/api/v8/channels/CHANNELID/messages/MESSAGEID/reactions/{emoji}/%40me',
        headers=headers                  
        #message ID - right click on message in Discord > copy link
        )

add_reaction(emoji.emojize(':thumbs_up:'))
#only works with standard emoji as the "emoji" module does not contain the custom ones