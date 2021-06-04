import discord
import sys
import requests

API_KEY = '149e444b12e4ebf2798a60be88c47c6ce31cc687'
API_URL = 'https://api.esv.org/v3/passage/text/'

TOKEN = 'ODUwMDE0ODg0Mjc5MDkxMjQx.YLjkDA.mRQiEG_PMdYeUUhXV9zaH8Gkuzo'

client = discord.Client()

def get_esv_text(passage):
    params = {
        'q': passage,
        'include-headings': True,
        'include-footnotes': False,
        'include-verse-numbers': True,
        'include-short-copyright': False,
        'include-passage-references': True
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)

    passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'


if __name__ == '__main__':
    passage = ' '.join(sys.argv[1:])

    if passage:
        print(get_esv_text(passage))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #Print verse/passage
    if message.content.startswith('!verse'):
        reference = message.content.replace('!verse','')
        await message.channel.send(get_esv_text(reference))
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

