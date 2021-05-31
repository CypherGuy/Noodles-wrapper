#!/usr/bin/env python3

import discord #To make a discord file
from os import write #To write to sample.png
import requests #To request an image

baseurl = 'https://frenchnoodles.xyz/api/endpoints/'
headers = {"APIKEY": SAMPLE}#At some point, headers, aka authentication, will come back. When it does, I'll update the code here.

def writeFile(res):
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close

def worthless(text):
    try:
        url = f'{baseurl}worthless?text={text}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'#Returns string  
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile#Returns image

def drake(text1, text2):
    try:
        url = f'{baseurl}drake?text={text1}&text2={text2}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def presidential(text):
    try:
        url = f'{baseurl}presidentialalert?text={text}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def spongebobburn(text):
    try:
        url = f'{baseurl}spongebobburnpaper?text={text}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def lisastage(text):
    try:
        url = f'{baseurl}lisastage?text={text}'
        res = requests.get(url)
        response = res.json()
        print(1)
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

past = lisastage('text')
print(past)

def changemind(text):
    try:
        url = f'{baseurl}changemymind?text={text}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def awkwardmonkey(text):
    try:
        url = f'{baseurl}awkwardmonkey?text={text}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def blur(link):
    try:
        url = f'{baseurl}blur?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def invert(link):
    try:
        url = f'{baseurl}invert?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def edge(link):
    try:
        url = f'{baseurl}edge?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def circle(link):
    try:
        url = f'{baseurl}circle?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def wide(link):
    try:
        url = f'{baseurl}wide?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def uglyupclose(link):
    try:
        url = f'{baseurl}uglyupclose?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def clown(link):
    try:
        url = f'{baseurl}clown?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def restpeace(link):
    try:
        url = f'{baseurl}rip?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def affectbaby(link):
    try:
        url = f'{baseurl}affectbaby?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def trash(link):
    try:
        url = f'{baseurl}trash?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def welcomebanner(background, avatar, title, subtitle, textcolor):
    try:
        url = f'{baseurl}welcomebanner?background={background}&avatar={avatar}&title={title}&subtitle={subtitle}&textcolor={textcolor}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def boostercard(link):
    try:
        url = f'{baseurl}boostercard?image={link}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile

def balancecard(background, avatar, title, top, bottom, textcolor):
    try:
        url = f'{baseurl}balancecard?background={background}&avatar={avatar}&title={title}&text1={top}&text2={bottom}&textcolor={textcolor}'
        res = requests.get(url)
        response = res.json()
        limit = response['You have passed your default quota!']
        return f'You have passed your default quota of {limit}.'   
    except:
        file = open("sample.png", "wb")
        file.write(res.content)
        file.close
        imageFile = discord.File(fp="sample.png",filename="picture.png")
        return imageFile
