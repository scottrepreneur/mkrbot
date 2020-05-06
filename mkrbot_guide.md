# Getting Started with @mkr.bot

Mkr.Bot is a knowledge hound and query runner for MKR holders and the Maker Community. Making resources easily discoverable helps new users become acquainted with the new terminology. Bringing on-chain context into governance and risk discussions helps even non-technical community members to monitor and advocate for system vitals.

- [Invoking @mkr.bot](#invoking-comands)
- [Query Commands](#query-commands)
- [Resource Commands](#resource-commands)
- [Maker Tool Commands](#maker-tool-commands)
- [Scheduled Updates](#scheduled-updates)

There are many options for each command so this list just has the most likely reference while @mkr.bot will try to infer from many different options for the same command.
[*The Full Commands List - Google Sheet*](https://docs.google.com/spreadsheets/d/1apOxgKIeeCTUnisfSRS0TLxiXsIFFB0xvtYLoxSpYX0/edit?usp=sharing)

## Commands Overview

### Invoking Commands

Mkr.Bot can be triggered with any of the following names:
- mkrbot
- mkr.bot
- @mkr.bot
- @mkrbot

### Approved Channels

- [#chakachat](https://chat.makerdao.com/channel/chakachat)
- [#community-development](https://chat.makerdao.com/channel/community-development)
- [Available for Direct Message as well](https://chat.makerdao.com/direct/mkr.bot)

### Getting Started Commands

- `help` will get a short list of commands and point you back here
- some commands also have a `vault help`
- if [@mkr.bot](https://chat.makerdao.com/direct/mkr.bot) doesn't know what you're looking for, they'll give a few example commands

### Query Commands

- `overview` provides an overview of Dai, MKR, Collateral, and System Parameters
- `dai` provides an overview of the Dai supply
- `burned` provides an overview of the MKR supply and burned
- `sf` provides the current stability fees for each collateral type
- `dsr` provides the current Dai Savings Rate for each collateral type

- `vaults` provides an overview of vaults
- `{collateral} vaults` provids an overview of vaults for a specific collateral
- `vault {id}` returns information about a particular vault from DefiExplore

- `prices` provides an overview of collateral prices
- `{collateral} prices` provides prices for a specific collateral

- `gov` returns summary metrics for governance
- `spells` gets the current MKR weight on each spell in the governing Chief
- `spells help` elaborates on the emoji symbols' meaning

### Resource Commands

- Developer Documentation: `docs`

- List of FAQs: `faqs` or `faq list`
- Vault FAQs: `vault faq`
- Dai FAQs: `dai faqs`
- DSR FAQs: `dsr faq`
- Emergency Shutdown FAQs: `shutdown faqs`
- Governance FAQs: `governance faq`
- Keepers FAQs: `keeper faqs`
- Liquidation FAQs: `liquidation faq`
- MakerDAO FAQs: `maker faqs`
- Oracles FAQs: `oracle faq`
- Risk FAQs: `risk faqs`
- Stability Fee FAQs: `stability fee faq`
- Glossary: `glossary`

- Awesome MakerDAO: `amd` or `amd list`
- Official Channels: `amd channels`
- Spend Dai: `amd spend dai`
- Use Dai: `awesome use`
- Lend Dai: `amd lend dai`
- Watch Dai: `awesome watch`
- Hold Dai: `amd hold dai`
- Trade Dai: `awesome trade`
- Developer Resources: `amd dev`
- Audits & Security: `awesome audits`

### Maker Tool Commands

- Oasis Borrow: `oasis`
- Oasis Save: `oasis save`
- Oasis Trade: `oasis trade`
- Governance Portal: `gov` or `vote`

### Scheduled Updates

#### Hourly Updates

- Price feed updates in [#chakachat]() when price has moved at least 2%

#### Quarter Hourly Updates

In [#governance-and-risk](https://chat.makerdao.com/channel/governance-and-risk) currently:
- New Spell available in Chief
- New Poll available in PollingEmitter
- Spell cast
- [Pending] Poll Expiring
- [Pending] Spell Expiring
- [Pending] Spell Scheduled in Chief
