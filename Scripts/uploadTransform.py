"""
ONLY RUN THIS FILE IF YOU ARE RAW UPLOADING ALL THE PICTURES TO CLOUDINARY - WARNED BY WILL
"""

from dotenv import load_dotenv, find_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

import os
from os import listdir
from os.path import isfile, join
import time

import json


load_dotenv(find_dotenv())

config = cloudinary.config(secure=True)

#To check if imported SDK correctly!
#print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

def upload_butterfly():

    print("starting butterflies")


    #the folder file for all butterfly pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/butterfly") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/butterfly", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/butterfly/{picture}', public_id = f"butterfly_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with Butterflies!")

def upload_cat():

    print("starting cats")

    #the folder file for all cat pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cat") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cat", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cat/{picture}', public_id = f"cat_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1

    return print("Done with Cats!")

def upload_chicken():
    
    print("starting chicken")

    #the folder file for all chicken pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/chicken") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/chicken", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/chicken/{picture}', public_id = f"chicken_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with Chicken!")

def upload_cow():

    print("starting cow")


    #the folder file for all cow pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cow") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cow", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/cow/{picture}', public_id = f"cow_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with cow!")



def upload_dog():

    print("starting dog")


    #the folder file for all dog pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/dog") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/dog", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/dog/{picture}', public_id = f"dog_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with dog!")

def upload_elephant():

    print("starting elephant")


    #the folder file for all elephant pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/elephant") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/elephant", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/elephant/{picture}', public_id = f"elephant_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with elephant!")

def upload_horse():

    print("starting horse")


    #the folder file for all horse pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/horse") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/horse", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/horse/{picture}', public_id = f"horse_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with horse!")

def upload_sheep():

    print("starting sheep")


    #the folder file for all sheep pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/sheep") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/sheep", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/sheep/{picture}', public_id = f"sheep_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with sheep!")

def upload_spider():

    print("starting spider")


    #the folder file for all sheep pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/spider") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/spider", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/spider/{picture}', public_id = f"spider_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with spider!")

def upload_squirrel():

    print("starting squirrel")


    #the folder file for all squirrel pictures
    onlyfiles = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/squirrel") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/squirrel", f))]

    n = 0
    
    for picture in onlyfiles:
        cloudinary.uploader.upload(f'e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/squirrel/{picture}', public_id = f"squirrel_upload{n}", unique_filename=True, transformation=[
        {'height': 32, 'width' : 32, 'crop': "scale"}
        ])
        n += 1


    return print("Done with squirrel!")



def pullDatabrickButterflies():
    

    #set up list variables
    asset_id = []
    public_id = []
    created_at = []
    url = []
    counter = 0
    setC = 0
    record = 0

    onlyButterflies = [f for f in listdir("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/butterfly") if isfile(join("e:\HomeWorks_camp\Final-Project-Group-5/Resources/Animals-10/butterfly", f))]

    print("start of data retrival")

    #loop will retrieve data from API and append to lists
    for picture in onlyButterflies:
        pictureData = cloudinary.api.resource(f"butterfly_upload{counter}")
        print(f"Processing Record {record} of Set {setC} // {picture}")

        #slow API 10 seconds after every 60 seconds

        if record < 499:
            try: 
                asset_id.append(pictureData['asset_id'])
                public_id.append(pictureData['public_id'])
                created_at.append(pictureData['created_at'])
                url.append(pictureData['url'])
            except:
                print(f"failed somehow")
            
            record +=1
        else:
            time.sleep(3600)
            record = 1
            setC+=1







#set up as a flask app
#if __name__ == "__main__":
    #upload_butterfly()
    #upload_cat()
    #upload_chicken()
    #upload_cow()
    #upload_dog()
    #upload_elephant()
    #upload_horse()
    #upload_sheep()
    #upload_spider()
    #upload_squirrel()
    #pullDatabrickButterflies()

##This flask script made the uplaod process split into different parts, uncomment on each upload funciton for it to wor