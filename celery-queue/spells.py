### 
#   FROM @lix on Rocket Chat
#   REPO https://github.com/lixwhi/check_vote_counts
###

import os
import json
import time
from web3 import Web3
import asyncio

MAINNET_URL = os.getenv('MAINNET_URL')

web3 = Web3(Web3.HTTPProvider(MAINNET_URL))

ETH_SCALE = 1000000000000000000

CHIEF = '0x9eF05f7F6deB616fd37aC3c959a2dDD25A54E4F5'

CHIEF_ABI = json.loads('[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]')

spells = [
	{'id': '185', 'description': '18.5', 'active': False, 'address': '0x1f42fd789e1fb5d34f365215219111a9335ed0911da620de3fd9992f9e5900bf'},
	{'id': '205', 'description': '20.5', 'active': False, 'address': '0xf55ab75f9089ec31ac3e2fd408a16fe9ddd50e8d8bfcb7aa7e97eaa8377e0792'},
	{'id': '225', 'description': '22.5', 'active': True, 'address': '0x079ea8688746ca3c039cc6de83b7c3e9df4c124fea469195aabdd2fea424b500'},
	{'id': '205_2', 'description': '20.5', 'active': True, 'address': '0x0046bdd073d32cf493f29ea4ba521cee6bc0b69a95a421858c63673bfcc728cc'},
	{'id': '185_2', 'description': '18.5', 'active': True, 'address': '0x4b9ba0f07c934da097d0ec612d9a376d17fc679d69b2d3d42d99c14d4e567c44'},
	{'id': '165', 'description': '16.5', 'active': True, 'address': '0xd18793a9cf093b47b9f75519e4bb2eeea28aaecbb3cc3433cd3e524417707cf5'},
	{'id': '145', 'description': '14.5', 'active': True, 'address': '0xac37e5a50d5e68c5c43515709d42e3a685dae5012e13e0ae350c161cc639f093'},
	{'id': '125', 'description': '12.5', 'active': True, 'address': '0xac37e5a50d5e68c5c43515709d42e3a685dae5012e13e0ae350c161cc639f093'},
	{'id': '105', 'description': '10.5', 'active': True, 'address': '0x210a49d694d555987a17563881a3308d8340bb0c211155c36824502dfdf96ea1'},
	{'id': '085', 'description': '08.5', 'active': True,  'address': '0x90113e0968cfaec39ca650108d1ec56b7e6c69807c85234783656d4b51c5e07b'},
	{'id': '095', 'description': '09.5', 'active': True, 'address': '0xf77c58966018b73304e3ca12619387209c5176aa9db117e9d8676d27aa101a4e'},
]

chief_contract = web3.eth.contract(address=CHIEF, abi=CHIEF_ABI)

def check_spells():
	block_number = web3.eth.blockNumber

	# get the counts for each spell
	for spell in spells:
		if spell['active'] == True:
			spell['count'] = round(int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=spell['address']))))[2:66].lstrip('0'), 16)/ETH_SCALE, 3)
		
		time.sleep(0.25)

	spells_message = 'The *spells count* at block _#{block_number}_ is:\n```'.format(block_number=block_number)
	
	# print the counts
	for spell in spells:
		if spell['active'] == True:
			spells_message = spells_message + '{description} count:'.format(description=spell['description']) + str(spell['count']).rjust(10) + ' \n' 
	
	return spells_message + '```'
