# monad_faucet_discord
monad faucet by discord
# Chat Bot for Discord

This is an automated chat bot script that sends messages to a Discord channel using multiple accounts, with optional proxy support. The bot can send formatted messages based on wallet addresses and is designed for periodic use.

## Features

- **Multi-account support**: The bot can handle multiple Discord accounts.
- **Proxy support**: Optionally use HTTP/SOCKS proxies to send requests.
- **Periodic message sending**: Automatically sends messages in intervals.
- **Customizable message format**: Format the message content based on wallet addresses.
- **Error handling**: Includes error handling for proxy and request failures.
- **Time delay**: The bot waits between sending messages to avoid rate limiting.

## Prerequisites

Before running the bot, ensure you have the following installed:

- **Python 3.x**: Make sure Python is installed on your system.
- **Requests Library**: Install the Python `requests` library if you don't have it yet. You can install it via pip:
  
  ```bash
  pip install requests
  ```


Configuration
1. Create auth.txt
This file should contain the Discord authorization token and wallet address for each account. Each entry should be on a new line, formatted like this:
```
authorization_token_1|!faucet wallet_address
authorization_token_2|What you want to send
authorization_token_3|What you want to send
```
2. (Optional) Create proxy.txt
If you wish to use proxies, create a proxy.txt file. This file should contain one proxy per line in the format:
```
http://ip1:port1
socks5://ip2:port2
http://ip3:port3
```
For example:
http://username:password@proxy_ip:proxy_port

3. Set Channel ID
In the script (chat.py), update the channel_id variable with the Discord channel ID where the messages will be sent.
channel_id = "your_channel_id_here"

4. Run the Script
After setting up the files, run the bot with:
```bash
python chat.py
```
5.Guide
For finding the Discord Channel ID image:

![Image 1](channelid_guide.png)

For finding the Discord Authorization (Auth) Token:

![Image 2](auth_guide.jpg)

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Disclaimer
This script is for educational and personal use only. Use it responsibly and make sure to comply with Discord's terms of service.

If you find this script useful, consider supporting with a small donation or test tokens:

```bash
Tron: TULRqnTVMhUmn9Hc1Q4KM5z8pDbdy9gm4J

EVM: 0xa4515c3b085d6d29894a14cad7b17c6b5ace1674

Solana: 2BUyFvoKDF4MZX4WwDBbvz9Uh744MuE7db5c75LzdrFT

Sui: 0x06cdd1deaad5ac0bb37b6f8c85ad2db8719fde0ba5322541ae2dd8d964e3dfdb

Ton: UQC1nd1isqiEvajVgJZpgTszM-Npry5zSiy4RcJBtnhI1-j_

BTC: bc1p7xfdxnle7kpdamz8h5ss3y02r4cvh5rh540e3d4fuqrlpnjulv9q600vza
```

