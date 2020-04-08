import os

MAKER_COMMUNITY_PORTAL = os.getenv('MAKER_COMMUNITY_PORTAL')
AMD_LINK = "https://awesome.makerdao.com"
DEV_DOCS_LINK = "https://developer.makerdao.com"
OASIS_LINK = "https://oasis.app"
MKRBOT_GUIDE_URL = "https://www.github.com/scottrepreneur/mkrbot/blob/master/mkrbot_guide.md"
CONTRIBUTING_URL = "https://www.github.com/scottrepreneur/mkrbot/blob/master/CONTRIBUTING.md"
CREATOR_DM_URL = "https://chat.makerdao.com/direct/scottrepreneur"
PENDING_MESSAGE = f"This is a pending command, please [contribute]({CONTRIBUTING_URL}) if you'd like to see this command added."

language_code = '/en'
faqs_url = '/makerdao-mcd-faqs/faqs'
scd_faqs_url = '/makerdao-scd-faqs/scd-faqs'
glossary_url = f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/glossary'

mkrbot_responses = {
    'faqs': {
        'cdp': f'Heads up! CDPs are called Vaults in Multi-Collateral Dai\n{MAKER_COMMUNITY_PORTAL}{faqs_url}/vault',
        'dai': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/dai',
        'dsr': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/dsr',
        'emergency_shutdown': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/emergency-shutdown',
        'governance': f'{MAKER_COMMUNITY_PORTAL}{scd_faqs_url}/governance',
        'glossary': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/glossary',
        'keepers': f'{MAKER_COMMUNITY_PORTAL}{scd_faqs_url}/keepers',
        'liquidation': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/liquidation',
        'makerdao': f'{MAKER_COMMUNITY_PORTAL}{scd_faqs_url}/makerdao',
        'oracles': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/oracles',
        'risk_management': f'{MAKER_COMMUNITY_PORTAL}{scd_faqs_url}/risk-management',
        'stability_fee': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/stability-fee',
        'vault': f'{MAKER_COMMUNITY_PORTAL}{faqs_url}/vault',
        'faqs_overview': f'''
Here's all the [FAQs]({MAKER_COMMUNITY_PORTAL}{faqs_url}) you can request
> We've got a glossary:  `glossary`
> Dai: `dai faq`
> Dai Savings Rate: `dsr faq`
> Emergency Shutdown: `shutdown faq`
> Governance: `governance faq`
> Liquidation: `liquidation faq`
> MakerDAO: `maker faq`
> Oracles: `oracle faq`
> Risk: `risk faq`
> Stability Fee: `stability fee faq`'''
    },
    'glossary': {
        'auction': f'{glossary_url}#auction',
        'bite': PENDING_MESSAGE, # removed from MCD? f'{glossary_url}#bite',
        'black_swan': f'{glossary_url}#black-swan',
        'burn': PENDING_MESSAGE, # removed from MCD? f'{glossary_url}#burn',
        'burner_address': PENDING_MESSAGE, # removed from MCD? f'{glossary_url}#burner-address',
        'collateral': f'{glossary_url}#collateral',
        'collateral_claims': f'{glossary_url}#collateral-claims',
        'collateralization_ratio': f'{glossary_url}#collateralization-ratio',
        'continuous_approval_voting': f'{glossary_url}#continuous-approval-voting',
        'dai_credit_system': PENDING_MESSAGE, # removed? f'{glossary_url}#dai-credit-system',
        'debt': PENDING_MESSAGE, # removed? f'{glossary_url}#debt',
        'debt_auction': f'{glossary_url}#debt-auction',
        'debt_ceiling': f'{glossary_url}#debt-ceiling',
        'decentralized_risk_management': f'{glossary_url}#decentralized-risk-management',
        'development_fund': f'{glossary_url}#development-fund',
        'dilution': f'{glossary_url}#dilution',
        'draw': PENDING_MESSAGE, # actions removed? f'{glossary_url}#draw',
        'executive_vote': f'{glossary_url}#executive-vote',
        'feed': f'{glossary_url}#feed',
        'free': PENDING_MESSAGE, # actions removed? f'{glossary_url}#free',
        'generated_dai': f'{glossary_url}#generated-dai',
        'give': PENDING_MESSAGE, # actions removed? f'{glossary_url}#give',
        'global_debt_ceiling': f'{glossary_url}#global-debt-ceiling',
        'governance_poll': f'{glossary_url}#governance-poll',
        'governance_portal': f'{glossary_url}#governance-portal',
        'hat': PENDING_MESSAGE, # f'{glossary_url}#hat',
        'liquidation_penalty': f'{glossary_url}#liquidation-penalty',
        'liquidation_price': f'{glossary_url}#liquidation-price',
        'liquidation_ratio': f'{glossary_url}#liquidation-ratio',
        'lock': PENDING_MESSAGE, # actions removed? f'{glossary_url}#lock',
        'maker_foundation': f'{glossary_url}#maker-foundation',
        'maker_protocol': f'{glossary_url}#maker-protocol',
        'market_maker': f'{glossary_url}#market-maker',
        'mcd': f'{glossary_url}#mcd',
        'medianizer': f'{glossary_url}#medianizer',
        'multi_collateral_dai': f'{glossary_url}#multi-collateral-dai',
        'osm': f'{glossary_url}#osm',
        'peg': f'{glossary_url}#peg',
        'price_feed_delay': f'{glossary_url}#price-feed-delay',
        'price_feed_provider': f'{glossary_url}#price-feed-provider',
        'proposal': f'{glossary_url}#proposal',
        'reference_price': f'{glossary_url}#reference-price',
        'risk_construct': f'{glossary_url}#risk-construct',
        'risk_parameters': f'{glossary_url}#risk-parameters',
        'risk_team': f'{glossary_url}#risk-team',
        'sai': f'{glossary_url}#sai',
        'scd': f'{glossary_url}#scd',
        'single_collateral_dai': f'{glossary_url}#single-collateral-dai',
        'shut': PENDING_MESSAGE, # actions removed? f'{glossary_url}#shut',
        'soft_peg': f'{glossary_url}#soft-peg',
        'spell': PENDING_MESSAGE, # f'{glossary_url}#spell',
        'time_based_voting': f'{glossary_url}#time-based-voting',
        'vote_proxy': f'{glossary_url}#vote-proxy-contract',
        'voting_contract': f'{glossary_url}#voting-contract',
        'weth': f'{glossary_url}#weth',
        'wipe': PENDING_MESSAGE, # actions removed? f'{glossary_url}#wipe',
    },
    'amd': {
        'awesome_makerdao': f'{AMD_LINK}',
        'awesome_channels': f'{AMD_LINK}official-channels',
        'awesome_spend_dai': f'{AMD_LINK}#spend-your-dai',
        'awesome_use_dai': f'{AMD_LINK}#use-your-dai',
        'awesome_lend_dai': f'{AMD_LINK}#lend-your-dai',
        'awesome_watch_dai': f'{AMD_LINK}#watch-your-dai',
        'awesome_hold_dai': f'{AMD_LINK}#hold-your-dai',
        'awesome_trade_dai': f'{AMD_LINK}#trade-your-dai',
        'awesome_dev_resoures': f'{AMD_LINK}#developer-resources',
        'awesome_audits_security': f'{AMD_LINK}#audits-and-security',
        'awesome_overview': f'''
Here are the [AMD]({AMD_LINK}) Resources you can request
> Official Channels: `amd channels`
> Spend Dai: `amd spend`
> Use Dai: `amd use`
> Lend Dai: `amd lend`
> Watch Dai: `amd watch`
> Hold Dai: `amd hodl`
> Trade Dai: `amd trade`
> Developer Resources: `amd dev`
> Audits & Security: `amd audit`'''
    },
    'resources': {
        'dev_docs': f'{DEV_DOCS_LINK}',
        'cdp_portal': f'Heads Up! CDPs are now called Vaults and the portal has moved to Oasis\n{OASIS_LINK}',
        'oasis_app': f'{OASIS_LINK}/borrow',
        'oasis_save': f'{OASIS_LINK}/save',
        'oasis_trade': f'{OASIS_LINK}/trade',
        'governance_dashboard': f'https://vote.makerdao.com',
        'dai_name': 'https://reddit.com/r/MakerDAO/comments/5q98b1/%E8%B2%B8_dai/',
        'mcd_contracts': 'https://changelog.makerdao.com'
    },
    'query_help': {
        'spells_help': f'''
Spells are proposals used to enact governance changes on the Maker Protocol.
The spells are listed by MKR weight, so the current "hat" will be at the top usually.
Symbols:
> :tophat: - the hat is the governing proposal with the most MKR
> :back: - the previously governing proposal
> :up: - a fresh proposal that could come to pass
> :heavy_check_mark: - a previous proposal that has already been passed
''',
        'vault_help': f'Enter a Vault ID to get an overview of the current lending status'
    },
    'easter_eggs': {
        'moon': f'''
#########################
#:new_moon::new_moon:###########:new_moon::new_moon:#
#:new_moon:##:new_moon:#######:new_moon:##:new_moon:#
#:new_moon:####:new_moon:###:new_moon:####:new_moon:#
#:new_moon:#####:new_moon:#:new_moon:#####:new_moon:#
#:new_moon:#####:new_moon:#:new_moon:#####:new_moon:#
#########################''',
        'number_go_up': 'https://youtu.be/e5nyQmaq4k4?t=24',
        'rick_roll': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    },
    'lost': {
        'help': f'''
Hey, I'm @mkr.bot. I can help you find resources or information about the Maker Protocol.
> *Commands*
> FAQs: `faqs {{governance | vaults | dai | stability fee}}`
> Spells Count: `spells`
> Vault Lookup: `vault {{ID}}`
> Awesome MakerDAO: `amd {{use | lend dai | spend | watch dai}}`
[mkr.bot Guide]({MKRBOT_GUIDE_URL}) | [Expand my commands!]({CONTRIBUTING_URL}) | Let [@scottrepreneur]({CREATOR_DM_URL}) know if you have any issues''',
        'no_commands': f'''
I didn\'t get you. Let me look up those Maker resources for you.
> *Commands*
> FAQs: `faqs {{governance | vaults | dai | stability fee}}`
> Spells Count: `spells`
> Vault Lookup: `vault {{ID}}`
> Awesome MakerDAO: `amd {{use | lend dai | spend | watch dai}}`
[mkr.bot Guide]({MKRBOT_GUIDE_URL}) | [Expand my commands!]({CONTRIBUTING_URL}) | Let [@scottrepreneur]({CREATOR_DM_URL}) know if you have any issues'''
    }
}
