#!/usr/bin/env python3

import discord
from discord.ext import commands
import requests
from importlib import resources
from importlib.resources import open_text
import io
from PIL import Image

headers = {"APIKEY": 'Ef0mZCsxSCKuXuHuJOMargwvZtyk2XaiHdGOmXzK'}

#class noodle_wrapper(commands.Cog):
 #   """Image-modifying commands."""

def worthless(text):
    url = f'https://frenchnoodles.xyz/api/endpoints/worthless?&text={text}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close   
    imageFile = discord.File(fp="sample.png",filename="worthless.png")
    return imageFile


def drake(text1, text2):
    url = f'https://frenchnoodles.xyz/api/endpoints/drake?text1={text1}&text2={text2}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="drake.png")
    return imageFile

def presidential(text1):
    url = f'https://frenchnoodles.xyz/api/endpoints/presidentialalert?text={text1}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close
    imageFile = discord.File(fp="sample.png",filename="presidential.png")
    return imageFile

def spongebobburn(text1):
    url = f'https://frenchnoodles.xyz/api/endpoints/spongebobburnpaper?text={text1}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="spongebobburn.png")
    return imageFile

def lisastage(text1):
    url = f'https://frenchnoodles.xyz/api/endpoints/lisastage?text={text1}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="lisastage.png")
    return imageFile

def changemind(text1):
    url = f'https://frenchnoodles.xyz/api/endpoints/changemymind?text={text1}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="changemind.png")
    return imageFile

def awkwardmonkey(text1):
    url = f'https://frenchnoodles.xyz/api/endpoints/awkwardmonkey?text={text1}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="awkwardmonkey.png")
    return imageFile

def blur(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/blur?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="blur.png")
    return imageFile

def invert(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/invert?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="invert.png")
    return imageFile

def edge(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/edges?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="edge.png")
    return imageFile

def circle(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/circle?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="circle.png")
    return imageFile

def wide(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/wide?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="wide.png")
    return imageFile

def uglyupclose(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/uglyupclose?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="uglyupclose.png")
    return imageFile

def clown(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/clown?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="clown.png")
    return imageFile

def restpeace(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/rip?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="restpeace.png")
    return imageFile

def affectbaby(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/acceftbaby?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="acceftbaby.png")
    return imageFile

def trash(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/trash?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="trash.png")
    return imageFile

def welcomebanner(background, avatar, title, subtitle, textcolor):
    url = f'https://frenchnoodles.xyz/api/endpoints/welcomebanner?background={background}&avatar={avatar}&title={title}&subtitle={subtitle}&textcolor={textcolor}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="welcomebanner.png")
    return imageFile

def boostercard(link):
    url = f'https://frenchnoodles.xyz/api/endpoints/boostercard?image={link}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="boostercard.png")
    return imageFile

def balancecard(background, avatar, title, top, bottom, textcolor):
    url = f'https://frenchnoodles.xyz/api/endpoints/balancecard?background={background}&avatar={avatar}&title={title}&text1={top}&text2={bottom}&textcolor={textcolor}'
    res = requests.get(url, headers=headers)
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close       
    imageFile = discord.File(fp="sample.png",filename="balancecard.png")
    return imageFile
