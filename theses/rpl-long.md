# Rocketpool thesis

Long RPL. 'high beta ETH with downside protection and asymmetric upside'.  
- [Twitter thread](https://twitter.com/nmorlock42/status/1551236059580735489)
- [reddit thesis](https://www.reddit.com/r/ethfinance/comments/m3pug8/the_rocket_pool_investment_thesis/)
- [reddit v2](https://www.reddit.com/r/ethfinance/comments/qwbb8w/rocket_pool_investment_thesis_20/)

## About RocketPool
- Validator: ethereum address with 32 ETH doing 'staking for consensus'
- Staking pool: 'normal' stakers deposit for rETH
- Minipool: Validator, but with 16 ETH from staking pool. Looks identical to a validator from Ethereum's perspective. Requires 1.6 ETH worth of RPL as collateral. 
- RocketPool Node: computer with ETH1 address + registered with RP smart contracts. Each RP node can run many minipools. 
- Node operators: people who run RP nodes
- [Deposit pool](https://docs.rocketpool.net/overview/glossary.html#deposit-pool): ETH waiting to be paired with node operators, deposited by regular users. Currented capped at 2k ETH, proposal to raise to 5k

### General
- Very small team, large community with community roles [[1](https://youtu.be/bQK9Yr1BpQw?t=300)]

### General reasons to hold rETH
- rETH holders 100% insured, no 'haircut' possibility or run on the banks
- no counterparty risk (excluding trusting the smart contracts)
- neutral, aligned with Ethereum, decentralized 
- [[1](https://youtu.be/bQK9Yr1BpQw?t=1200)]

### Smoothing pool [[Bankless](https://youtu.be/bQK9Yr1BpQw?t=3614)]
- Launched with Redstone upgrade 
- Gives access to MEV. Misleading that 10% of staking rewards come from MEV because most blocks have little to none, but a few have massive amounts of MEV. Smoothing pool allows everyone to have an equal and predictable share of that MEV else validators are just playing the lottery
    - Lottery may not last long, there are talks about disabling ordering transactions, etc. Possibly only a finite time can validators take advantage of the status-quo. Proposer-builder seperation
- Opt-in for node operators, 30% as of Sept 2 have opted in

### RPL
- Helps make RP non-rent-seeking, else would have to take commission. Instead can inflate RPL to fund team
- Designed to have favourable tokenomics

### rETH
- A reason to hold rETH over stETH is because less tax events: stETH value is equal ETH and you accrue rewards by recieving more stETH. So by holding stETH you're recieving stETH and will need to pay income tax. With rETH, the value grows with respect to ETH proportional to the staking rewards instead of recieving additional rETH. So your only tax event is when you sell your rETH, which means you can take advantage if traditional tax minimization strategies like simply holding for a year to qualify for long term capital gains tax treatment. [[1](https://youtu.be/bQK9Yr1BpQw?t=1987), [2](https://twitter.com/marceaueth/status/1566508002886156288)]
- Supposedly rETH would be more adopted by apps but curretly stETH is in the lead. No major lending protocals I know of uses rETH yet. But both RP and AAVE [have interest](https://snapshot.org/#/aave.eth/proposal/0xf593f2df83cc0b5bdc3920ef2c782f6b2a6f87a6603c26a5d778e3ede4d40021) in adding rETH, though no current progress. 
- Institutional demand for 'internet-bond' as staking ETH for rETH, shorting ETH on lending platforms will create insane liquidity for ETH/rETH pair to harvest the yield --> leading to large amounts of ETH being staked for rETH
- With rETH, you are getting the highest yield when staking with RP as you get 15% from the other 16 ETH and RPL rewards

### Links
- [docs](https://docs.rocketpool.net/guides/node/responsibilities.html#how-eth2-staking-works)
- [discord rETH liquidity brainstorming](https://discord.com/channels/405159462932971535/929890788551323678)

## Time horizens and expectations
- long-term (a few years)
- possible catalysts for short-term pumps that I may swing-trade:
    - ETH merge. Pump may be before/during/after
    - Staked ETH withdrawal: potentially many stakers from Lido and other staking providers can move to RP, increasing demand for RPL

## Bull theses
### 🐂 Downside protection
- it is tied by design to the value of ETH. If ETH goes up new stakers need to [buy more RPL](https://docs.rocketpool.net/guides/node/create-validator.html#staking-rpl) to meet 10% min, and (2) existing stakers need to buy more RPL to collect RPL rewards [source](https://docs.rocketpool.net/guides/node/rewards.html#rewards-and-checkpoints)
- Downside protection: RPL has real utility. As long as new node operators want to stake with Rocketpool, they need to buy RPL. Reasons to stake with Rocketpool: (1) decentralized, (2) <32 ETH, (3) greater staking commission by between 5% and 20% depending on when minipool set up. 
    - if the value of ETH goes up, then the amount of RPL that a new node operator would have to purchase also goes up by the same amount
    - any node operator who fell below 10% collateralization but who wanted to collect RPL rewards would need to buy more RPL to top up back to 10%

### 🐂 Increase in staking yield
- The Merge will create influx of stakers due to staking rate [14%->7%](https://youtu.be/bQK9Yr1BpQw?t=1009) which will lead to new node operators. Also expected over 2 years ETH will go from 12% staked to [30-50% staked](https://youtu.be/bQK9Yr1BpQw?t=1100)

### 🐂 New features
- avalanche of integrations coming [[1](https://youtu.be/bQK9Yr1BpQw?t=1366), [2](https://youtu.be/bQK9Yr1BpQw?t=1396)]
    - Maker around second week of September
    - Collateral usage is coming (with Maker) and others
    - Liquidity incentives are coming. Starting ~Sept 2, Rocketpool committee will incentivize rETH paired pools. Will be pushing quite hard on this
- Staking as a service [[1](https://youtu.be/bQK9Yr1BpQw?t=3200)]. 
    - Geared towards institutions and small companies to do the marketing
- Soon will be able to run minipool with 8 (then 4) eth, allowing leverage for earned yield on counterpart's ETH while also reducing counterpart's commission 

### 🐂 ETH withdrawals seemless integration
- After staked ETH withdrawals are enabled, people can seemlessly transition their solo-staked ETH to RP minipools and RP does all the setting up/etc automatically. [[1](https://youtu.be/bQK9Yr1BpQw?t=3459)]
    - [Smoothing pool](#smoothing-pool)
    - Potentially a lot of solo-stakers would want to do this. Benefits include:
    - Using RP software apparently has some benefits, see [1]
- Ethereum community. Most of the people staking ETH care about the health of Ethereum, and it is known that using centralizing staking providers is a safety risk, many people may wish to exit staking out of LDO, etc, and move to RPL after withdrawals are enabled 1/2 year after the merge. For alignment with the Ethereum ethos, RP is second only to solo-staking, and if stakers care about Ethereum, many may change when given the opportunity after staking withdrawals are enabled. 
- [#new-features](#🐂-new-features)

### 🐂 Bankless thesis [[1](https://youtu.be/bQK9Yr1BpQw?t=4590)]
- Assumptions:
    - within 2 years will go from 30m ETH staked to 60m (expecting 50% of total supply staked within decade from 11% Sept 2)
    - RP 5% of the share of the pie (?), getting to 8-10% is justifiable
    - Collateralizating for node operators is 80%, assume trend down to 60%
- 0.12 ratio with ETH (8.18 ratio, 12x current ETH price)

## Bear theses
### 🐻 Shrinking marketshare
- Rocketpool starts to become a less popular staking solution (then what?). 
    - Currently Rocket Pool is growing and growing in minipool size and RPL staked (currently 34%) [dune](https://dune.com/NDGcrypto/Rocket-Pool-rETH-and-Nodes)
- Lots of headwind for this to be the case. Most of these will have to be false: [[#yield increase](#🐂-increase-in-staking-yield), [#new features](#🐂-new-features), [#eth withdrawals](#🐂-eth-withdrawals-seemless-integration)]

### 🐻 Technical risk
- Rocketpool gets hacked/drained
- So far seems very unlikely any funds would be lost, RP community has high confidence [bankless]

## Supply and demand
### Current supply and demand
Buyers:
- Node operators who want to stake with Rocketpool (main driver)
- speculators

Sellers:
- [5%](https://docs.rocketpool.net/guides/node/rewards.html#rewards-and-checkpoints) inflation rewards

### Expected change in supply and demand
🟩 Buyers (Increase):
- Increase in ETH staking rewards following merge will lead to more people who want to stake but don't meet 32 ETH requirement, or want extra [15% commission](https://docs.rocketpool.net/overview/glossary.html#node-commission)
- A lot more speculators once the Merge has completed and people flock to staking after realizing rate and RPL thesis

🟩Sellers (Decrease):
- Buyers likely using RPL as collateral, thus locking it and reducing the liquid supply

## Plan and risk tolerance
- Looking to take advantage of catalysts if they appear: [[#merge staking rewards](#🐂-increase-in-staking-yield), [#eth withdrawals](#🐂-eth-withdrawals-seemless-integration)]
- Accumulate short-term and long-term positions

