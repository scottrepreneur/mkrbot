
mkrbot_triggers = {
    'queries': {                                #? trigger_group
        'spell_count': [                        #? query
            'spell',                            #? sub-query/command
            'spells',
            'spell count',
            'spells count',
            'chief spells',
            'chief spells count',
            'chief spell count',
            'what is the spell count',
            'what is the spell count?',
            'what is spell count',
            'what is spell count?',
            'mkr on spells',
            'mkr on spell',
            'mkr per spells',
            'mkr per spell'
        ],
        'check_cdp': [
            'cdp [0-9]'
        ],
        'check_vault': [
            'vault [0-9]'
        ],
        'mkr_burned': [
            'mkr burned',
            'burner',
            'burn',
            'burned',
        ],
        'dai_supply': [
            'dai',
            'dai supply',
            'supply',
            'outstanding dai',
            'outstanding dai supply',
            'outstanding supply',
            'supply dai'
        ]
    },
    'query_help': {
        'spells_help': [
            'spell help',
            'chief spells help',
            'spell count help',
            'spells count help',
            'spell counts help',
            'spells counts help'
        ],
        'vault_help': [
            'vault help',
            'vault'
        ]
    },
    'faqs': {
        'cdp': [
            'faqs cdp',
            'faq cdp',
            'cdp faqs',
            'cdp faq',
            'what is a cdp',
            'what is cdp',
            'what is a cdp?',
            'what is cdp?'
        ],
        'dai': [
            'faqs dai',
            'faq dai',
            'dai faqs',
            'dai faq',
            'what is dai',
            'what is dai?'
        ],
        'dsr': [
            'faqs dsr',
            'faq dsr',
            'dsr faqs',
            'dsr faq',
            'what is the dsr',
            'what is the dsr?',
            'what is dsr',
            'what is dsr?',
            'what is the dai savings rate',
            'what is the dai savings rate?',
            'what is dai savings rate',
            'what is dai savings rate?'
        ],
        'emergency_shutdown': [
            'faqs shutdown',
            'faq shutdown',
            'faq emergency shutdown',
            'shutdown faqs',
            'shutdown faq',
            'emergency shutdown faqs',
            'emergency shutdown faq',
            'what is emergency shutdown',
            'what is emergency shutdown?'
        ],
        'glossary': [
            'glossary',
            'terms',
            'faq glossary',
            'faq terms'
        ],
        'governance': [
            'faqs governance',
            'faq governance',
            'governance faqs',
            'governance faq',
            'what is governance',
            'what is governance?'
        ],
        'keepers': [
            'faqs keepers',
            'faqs keeper',
            'faq keepers',
            'faq keeper',
            'keepers faqs',
            'keeper faqs',
            'keepers faq',
            'keeper faq',
            'what is a keeper',
            'what is a keeper?',
            'what is keeper',
            'what is keeper?',
            'what is keepers',
            'what is keepers?'
        ],
        'liquidation': [
            'faqs liquidation',
            'faq liquidation',
            'liquidation faqs',
            'liquidation faq',
            'what is liquidation',
            'what is liquidation?'
        ],
        'makerdao': [
            'faqs maker',
            'faq maker',
            'maker faqs',
            'maker faq',
            'faq makerdao',
            'faqs makerdao',
            'makerdao faq',
            'makerdao faqs',
            'what is maker',
            'what is makerdao',
            'what is maker?',
            'what is makerdao?'
        ],
        'oracles': [
            'faqs oracles',
            'faqs oracle',
            'faq oracles',
            'faq oracle',
            'oracles faqs',
            'oracle faqs',
            'oracles faq',
            'oracle faq',
            'what is an oracle',
            'what is an oracle?'
        ],
        'risk_management': [
            'faqs risk',
            'faq risk',
            'risk faqs',
            'risk faq',
            'risk management faq',
            'risk management faqs',
            'faq risk management',
            'faqs risk management',
            'what is risk',
            'what is risk?',
            'what is risk management',
            'what is risk management?'
        ],
        'stability_fee': [
            'faqs stability',
            'faq stability',
            'faq stability fee',
            'faqs stability fee',
            'stability faqs',
            'stability fee faqs',
            'stability faq',
            'stability fee faq',
            'what is the stability fee',
            'what is the stability fee?',
            'what is stability fee',
            'what is stability fee?'
        ],
        'vault': [
            'faqs vaults',
            'faq vaults',
            'faq vault',
            'faqs vault'
            'vault faqs',
            'vault faq',
            'what is a vault',
            'what is a vault?',
            'what is vault',
            'what is vault?'
        ],
        'faqs_overview': [
            'faq',
            'faqs',
            'faqs list',
            'faqs overview',
            'faqs help',
            'faq list',
            'faq overview',
            'faq help'
        ]
    },
    'glossary': {
        'auction': [
            'what is an auction?',
            'auction',
            'what is an auction',
            'what is auction?',
            'what is auction'
        ],
        'bite': [
            'what is a bite?',
            'bite',
            'what bite',
            'what is bite',
            'what is bite?',
            'what is a bite'
        ],
        'black_swan': [
            'what is a black swan?',
            'black swan	black swan event',
            'what is a black swan',
            'what is black swan?',
            'what is black swan'
        ],
        'burn': [
            'what happens to burned MKR?',
            'burned mkr',
            'burn mkr',
            'mkr burn',
            'mkr burned',
            'what happens to burned mkr?',
            'what happens burned mkr?',
            'what happens to burned mkr',
            'what happens to burned mkr'
        ],
        'burner_address': [
            'what is the burner address?',
            'burner address',
            'burn address',
            'what is the burner address'
        ],
        'collateral': [
            'what is a collateral?',
            'what is collateral?',
            'collateral',
            'what is a collateral',
            'what is collateral'
        ],
        'collateral_claim': [
            'what is a collateral claim?',
            'collateral claim',
            'claim collateral',
            'what is a collateral claim'
        ],
        'collateralization_ratio': [
            'what is the collateralization ratio?',
            'collateralization ratio',
            'collateral ratio',
            'what is the collateralization ratio',
            'what is the collateral ratio?',
            'what is the collateral ratio'
        ],
        'continuous_approval_voting': [
            'what is continuous approval voting?',
            'continuous approval voting',
            'continuous approval',
            'what is continuous approval voting'
        ],
        'dai_credit_system': [
            'what is the dai credit system?',
            'dai credit system',
            'what is the dai credit system'
        ],
        'debt': [
            'what is vault debt?',
            'debt',
            'vault debt',
            'debt vault',
            'what is vault debt',
            'what is debt?',
            'what is debt'
        ],
        'debt_auction': [
            'what is a debt auction?',
            'debt auction',
            'what is a debt auction',
            'what is debt auction?',
            'what is debt auction'
        ],
        'debt_ceiling': [
            'what is the debt ceiling?',
            'debt ceiling',
            'dc',
            'what is the debt ceiling'
        ],
        'decentralized_risk_management': [
            'what is decentralized risk management?',
            'decentralized risk management',
            'risk management'
        ],
        'development_fund': [
            'what is the development fund?',
            'dev fund',
            'development fund',
            'what is the development fund'
        ],
        'dilution': [
            'what is dilution?',
            'what is dilution',
            'dilution'
        ],
        'draw': [
            'what is the draw action?',
            'draw',
            'draw action',
            'draw dai',
            'draw debt',
            'what is the draw action',
            'what is draw?',
            'what is draw'
        ],
        'executive_vote': [
            'what is an executive vote?',
            'executive vote',
            'executive',
            'what is an executive vote'
        ],
        'feed': [
            'what is a feed?',
            'feed',
            'oracle feed',
            'price feed',
            'what is a feed',
            'what is feed?',
            'what is feed'
        ],
        'free': [
            'what is the free action?',
            'free',
            'free action',
            'free collateral',
            'free eth',
            'what is the free action',
            'what is free?',
            'what is free'
        ],
        'generated_dai': [
            'what is generated dai?',
            'generated dai',
            'what is generated dai'
        ],
        'global_debt_ceiling': [
            'what is the global debt ceiling?',
            'global debt ceiling',
            'what is the global debt ceiling'
        ],
        'give': [
            'what is the give action?',
            'give',
            'give action',
            'give vault',
            'give cdp',
            'what is the give action',
            'what is give?',
            'what is give'
        ],
        'governance_poll': [
            'what is a governance poll?',
            'governance poll',
            'poll',
            'what is a governance poll'
        ],
        'governance_portal': [
            'what is the governance portal?',
            'what is the governance portal'
        ],
        'hat': [
            'what is the hat?',
            'hat',
            'what is the hat',
            'what is hat?',
            'what is hat'
        ],
        'liquidation_penalty': [
            'what is the liquidation penalty?',
            'liquidation penalty',
            'penalty',
            'what is the liquidation penalty'
        ],
        'liquidation_price': [
            'what is the liquidation price?',
            'liquidation price',
            'what is the liquidation price',
            'what is liquidation price?',
            'what is liquidation price'
        ],
        'liquidation_ratio': [
            'what is the liquidation ratio?',
            'liquidation ratio',
            'what is the liquidation ratio',
            'what is liquidation ratio?',
            'what is liquidation ratio'
        ],
        'lock': [
            'what is the lock action?',
            'lock',
            'lock action',
            'lock collateral',
            'lock eth',
            'what is the lock action',
            'what is lock?',
            'what is lock'
        ],
        'maker_foundation_interim_risk_team': [
            'what is the maker foundation interim risk team?',
            'interim risk team',
            'interim risk',
            'what is the maker foundation interim risk team',
            'what is maker foundation interim risk team?',
            'what is maker foundation interim risk team'
        ],
        'maker_foundation': [
            'what is the maker foundation?',
            'maker foundation',
            'foundation',
            'what is the maker foundation',
            'what is maker foundation?',
            'what is maker foundation'
        ],
        'maker_protocol': [
            'what is the maker protocol?',
            'maker protocol',
            'what is the maker protocol',
            'what is maker protocol?',
            'what is maker protocol'
        ],
        'market_maker': [
            'what is a market maker?',
            'market maker',
            'what is a market maker',
            'what is market maker'
        ],
        'mcd': [
            'what is mcd?',
            'mcd',
            'what is mcd'
        ],
        'medianizer': [
            'what is the medianizer?',
            'medianizer',
            'what is the medianizer',
            'what is medianizer?',
            'what is medianizer'
        ],
        'multi_collateral_dai': [
            'what is multi-collateral dai?',
            'multi collateral dai',
            'multi-collateral dai',
            'what is multi collateral dai?',
            'what is multi-collateral dai',
            'what is multi collateral dai'
        ],
        'osm': [
            'what is the osm?',
            'osm',
            'what is the osm',
            'what is osm?',
            'what is osm'
        ],
        'peg': [
            'what is the peg?',
            'peg',
            'what is the peg',
            'what is the dai peg?',
            'what is the dai peg',
            'dai peg',
            'what is the peg?',
            'what is peg'
        ],
        'price_feed_delay': [
            'what is the price-feed delay?',
            'price-feed delay',
            'price feed delay',
            'what is the price-feed delay',
            'what is price-feed delay?',
            'what is price feed delay'
        ],
        'price_feed_provider': [
            'what is a price-feed provider?',
            'price-feed provider',
            'price feed provider',
            'what is a price-feed provider',
            'what is a price feed provider?',
            'what is a price feed provider',
            'what is price-feed provider?',
            'what is price-feed provider',
            'what is price feed provider?',
            'what is price feed provider'
        ],
        'proposal': [
            'what is a proposal?',
            'proposal',
            'what is a proposal',
            'what is proposal?',
            'what is proposal'
        ],
        'reference_price': [
            'what is the reference price?',
            'reference price',
            'what is the reference price',
            'what is reference price?',
            'what is reference price'
        ],
        'risk_construct': [
            'what is a risk construct?',
            'risk construct',
            'what is a risk construct',
            'what is risk construct?',
            'what is risk construct'
        ],
        'risk_parameters': [
            'what are risk parameters?',
            'risk parameters',
            'what are risk parameters',
            'what is risk parameters?',
            'what is risk parameters'
        ],
        'risk_team': [
            'what is a risk team?',
            'risk team',
            'what is risk team?',
            'what is risk team'
        ],
        'sai': [
            'what is sai?',
            'sai',
            'what is sai'
        ],
        'scd': [
            'what is scd?',
            'scd',
            'what is scd'
        ],
        'single_collateral_dai': [
            'what is single-collateral dai?',
            'single collateral dai',
            'single-collateral dai',
            'what is single collateral dai?',
            'what is single-collateral dai',
            'what is single collateral dai'
        ],
        'shut': [
            'what is the shut action?',
            'shut',
            'shut action',
            'shut cdp',
            'shut vault',
            'what is the shut action',
            'what is shut?',
            'what is shut'
        ],
        'soft_peg': [
            'what is a soft peg?',
            'soft peg',
            'what is a soft peg',
            'what is soft peg?',
            'what is soft peg'
        ],
        'spell': [
            'what is a spell?',
            'spell',
            'what is a spell',
            'what is spell?',
            'what is spell'
        ],
        'time_based_voting': [
            'what is time-based voting?',
            'time based voting',
            'time-based voting',
            'what is time-based voting',
            'what is time based voting?',
            'what is time based voting'
        ],
        'vote_proxy': [
            'what is a voting proxy?',
            'voting proxy',
            'what is a voting proxy',
            'what is voting proxy?',
            'what is voting proxy'
        ],
        'voting_contract': [
            'what is the voting contract?',
            'voting contract',
            'what is the voting contract'
        ],
        'weth': [
            'what is weth?',
            'weth',
            'what is weth'
        ],
        'wipe': [
            'what is the wipe action?',
            'wipe',
            'wipe action',
            'wipe dai',
            'wipe debt',
            'what is the wipe action',
            'what is wipe action?',
            'what is wipe action'
        ]
    },
    'amd': {
        'awesome_makerdao': [
            'awesome',
            'awemkr',
            'am',
            'amd',
            'awesome makerdao',
            'awesomemakerdao',
            'awesomemaker'
        ],
        'awesome_channels': [
            'awesome channels',
            'awesome channel',
            'awesome maker channels',
            'awesome official channels',
            'awesome official maker channels',
            'amd channels',
            'amd maker channels',
            'amd official channels'
        ],
        'awesome_spend_dai': [
            'awesome spend',
            'awesome spend dai',
            'awesome dai spend',
            'amd spend',
            'amd spend dai',
            'amd dai spend'
        ],
        'awesome_use_dai': [
            'awesome use',
            'awesome use dai',
            'awesome dai use',
            'amd use',
            'amd use dai',
            'amd dai use'
        ],
        'awesome_lend_dai': [
            'awesome lend',
            'awesome lend dai',
            'awesome dai lend',
            'amd lend',
            'amd lend dai',
            'amd dai lend'
        ],
        'awesome_watch_dai': [
            'awesome watch',
            'awesome watch dai',
            'awesome dai watch',
            'amd watch',
            'amd watch dai',
            'amd dai watch'
        ],
        'awesome_hold_dai': [
            'awesome hold',
            'awesome hold dai',
            'awesome dai hold',
            'amd hold',
            'amd hold dai',
            'amd dai hold'
        ],
        'awesome_trade_dai': [
            'awesome trade',
            'awesome trade dai',
            'awesome dai trade',
            'amd trade',
            'amd trade dai',
            'amd dai trade'
        ],
        'awesome_dev_resoures': [
            'awesome dev',
            'awesome dev resources',
            'awesome dev resource',
            'awesome developer',
            'awesome developer resources',
            'awesome developer resource',
            'amd dev',
            'amd dev resources',
            'amd developer',
            'amd developer resources'
        ],
        'awesome_audits_security': [
            'awesome audit',
            'awesome audits',
            'amd audit',
            'amd audits'
        ],
        'awesome_overview': [
            'amd list',
            'amd overview',
            'amd help'
        ]
    },
    'resources': {
        'dev_docs': [
            'docs',
            'dev docs',
            'documentation',
            'dev documentation',
            'developer documentation',
            'developer docs'
        ],
        'cdp_portal': [
            'portal',
            'cdp portal',
            'cdps portal',
            'portal cdp',
            'portal cdps'
        ],
        'oasis_app': [
            'oasis',
            'vault portal',
            'vaults portal',
            'portal vault',
            'portal vaults'
        ],
        'oasis_save': [
            'oasis save',
            'save'
        ],
        'oasis_trade': [
            'oasis trade',
            'trade'
        ],
        'governance_dashboard': [
            'governance',
            'gov',
            'vote',
            'gov dashboard',
            'governance dashboard',
            'governance portal',
            'portal governance',
        ],
        'dai_name': [
            'dai name',
            'where is dai name from?',
            'where is dai name from	what is dai name?',
            'what is dai name',
            'what does dai mean?',
            'what does dai mean',
            'what does dai name mean?',
            'what does dai name mean'
        ],
        'mcd_contracts': [
            'contracts',
            'where are the contracts?',
            'where are the contracts',
            'show me the contracts',
            'contracts?',
            'where are contracts?',
            'where are contracts'
        ]
    },
    'easter_eggs': {
        'moon': [
            'moon',
            'when moon',
            'wen moon'
        ],
        'number_go_up': [
            'up',
            'number up'
        ],
        'rick_roll': [
            'rich',
            'rick',
            'roll',
            'roll me baby one more time'
        ]
    },
    'lost': {
        'help': [
            'help',
            'i need help',
            'help me'
        ]
    }
}
