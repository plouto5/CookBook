import discord
import asyncio
import os
import secrets
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!coin'):
        arg = message.content.split()
        if arg[1] == 'help':
            await client.send_message(message.channel, 'Use !coin followed by the ticker symbol you would like to get the price of.')
        try:
            if arg[1][3] == '<':
                coin1 = arg[1][0:3]
                coin2 = arg[1][4:7]
                price = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={coin1.upper()}&tsyms={coin2.upper()}&extraParams=your_app_name')
                answer = str(price.json()[f'{coin2.upper()}'])
                await client.send_message(message.channel, f'{coin2.upper()} {answer}')
        except IndexError:
            ticker = arg[1]
            print(ticker)
            api = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={ticker.upper()}&tsyms=USD')
            print(type(api))
            price = str(api.json()['USD'])
            print(price)
            await client.send_message(message.channel, f'{ticker.upper()} ${price}')

    else:
        pass

client.run(secrets.client_token)
