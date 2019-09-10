#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:28:21 2019

@author: Lucas A. Fagundes

Example: ipython baixa_cemaden_v01.py maceio 400km /home/lucas/maceio/

"""
      
import requests
import bs4
import os
from urllib.request import urlopen,HTTPError,URLError,urlretrieve
import sys

def locall(local):
    import os
    os.chdir(str(local))
    return local

def exist_local(local):
    try:  
        os.mkdir(local)
    except OSError:  
        pass
#            print ("Creation of the directory %s failed", str(local))
    else:  
        print ("Successfully created the directory %s ", str(local))            
    return local

        
#def links_radar(radar,cobertura='400km'):
#    if radar == 'all':
#        for radar in ['maceio','jaraguari','almenara','natal','petrolina','salvador','santa_teresa','sao_francisco','tres_marias']:
#            print(radar)
def links_radar_baixar(radar,cobertura):
    if radar == 'jaraguari':
       if cobertura == '400km':
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=jaraguari&produto=azi_400km_05gr.azi')
       else:
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=jaraguari&produto=vol_250km_12steps.vol')
#                        http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=jaraguari&produto=azi_400km_05gr.azi
    elif radar == 'maceio':
       if cobertura == '400km':
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=maceio&produto=vol_400km_3steps.vol')
       else:
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=maceio&produto=vol_250km_13steps.vol')
    elif radar == 'almenara':
       if cobertura == '400km':
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=almenara&produto=vol_400km_3steps.vol')
       else:
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=almenara&produto=vol_250km_13steps.vol')
    elif radar == 'natal':
       if cobertura == '400km':
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=natal&produto=vol_400km_3steps.vol')
       else:
           radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=natal&produto=vol_250km_13steps.vol')
    elif radar == 'petrolina':
        if cobertura == '400km':
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=petrolina&produto=vol_400km_3steps.vol')
        else:
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=petrolina&produto=vol_250km_13steps.vol')
    elif radar == 'salvador':
        if cobertura == '400km':
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=salvador&produto=vol_400km_3steps.vol')
        else:
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=salvador&produto=vol_250km_13steps.vol')
    elif radar == 'santa_teresa':
        if cobertura == '400km':
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=santa_teresa&produto=vol_400km_3steps.vol')
        else:
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=santa_teresa&produto=vol_250km_13steps.vol')
    elif radar == 'sao_francisco':
        if cobertura == '400km':
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=sao_francisco&produto=vol_400km_3steps.vol')
        else:
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=sao_francisco&produto=vol_250km_13steps.vol')
    elif radar == 'tres_marias':
        if cobertura == '400km':
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=tres_marias&produto=vol_400km_3steps.vol')
        else:
            radar_data = requests.get('http://www.cemaden.gov.br/mapainterativo/download/downradares.php?radar=tres_marias&produto=vol_250km_13steps.vol')
    return radar_data


def fc_baixa(radar,local,cobertura):
    
#    print('')
#    print('#  @autor: Lucas A. Fagundes #')
#    print('##  Created on Thu Jan 31 09:28 2019 ##')
#    print('##  Last modified July 29 14:00 2019 ##')
#    print('')
    
    radar_data = links_radar_baixar(radar,cobertura)
    radar_data.text
    soup = bs4.BeautifulSoup(radar_data.text,'lxml')

    exist_local(local)
    locall(local)
    for link in soup.find_all('a',href=True):
#        print(link['href'])
        url = link['href']
        try:
#            print (url)
            uk = url.split('=')
            uk = uk[-1]
            path = local+uk
            pto = url.split('.')
            pto = pto[-1]
            if pto == 'h5':
#                if os.path.isfile(path) == False:
#                    urlretrieve(url, uk)
                pass
            else:
                if os.path.isfile(path) == False:
                    urlretrieve(url, uk)
                    print("downloaded file ", str(uk))
        except:
            print('')
    return local

def main():
    radar = sys.argv[1]
    cobertura = sys.argv[2]
    local = sys.argv[3]
    fc_baixa(radar,local,cobertura)
    
main()

'''    

ipython baixa_cemaden_v01.py maceio 400km /home/lucas/maceio/

'''

        #esse é o erro de nao encontrar            
#fc_baixa(radar='maceio',local='/home/lucas/maceio/',cobertura='400km')
#fc_baixa(radar='almenara',local='/home/lucas/teste/almenara/',cobertura='400km')
#fc_baixa(radar='salvador',local='/home/lucas/teste/salvador/',cobertura='400km')
#fc_baixa(radar='santa_teresa',local='/home/lucas/teste/santa_teresa/',cobertura='400km')
#fc_baixa(radar='sao_francisco',local='/home/lucas/teste/sao_francisco/',cobertura='400km')
#fc_baixa(radar='tres_marias',local='/home/lucas/teste/tres_marias/',cobertura='400km')
#fc_baixa(radar='jaraguari',local='/home/lucas/teste/jaraguari/',cobertura='400km')
#fc_baixa(radar='petrolina',local='/home/lucas/teste/petrolina/',cobertura='400km')
#fc_baixa(radar='natal',local='/home/lucas/teste/natal/',cobertura='400km')
#
#fc_baixa(radar='maceio',local='/home/lucas/teste/maceio/250/',cobertura='250km')
#fc_baixa(radar='salvador',local='/home/lucas/teste/salvador/250/',cobertura='250km')
#fc_baixa(radar='santa_teresa',local='/home/lucas/teste/santa_teresa/250/',cobertura='250km')
#fc_baixa(radar='sao_francisco',local='/home/lucas/teste/sao_francisco/250/',cobertura='250km')
#fc_baixa(radar='tres_marias',local='/home/lucas/teste/tres_marias/250/',cobertura='250km')
#fc_baixa(radar='jaraguari',local='/home/lucas/teste/jaraguari/250/',cobertura='250km')
#fc_baixa(radar='petrolina',local='/home/lucas/teste/petrolina/250/',cobertura='250km')
#fc_baixa(radar='natal',local='/home/lucas/teste/natal/250/',cobertura='250km')
#fc_baixa(radar='almenara',local='/home/lucas/teste/almenara/250/',cobertura='250km')
