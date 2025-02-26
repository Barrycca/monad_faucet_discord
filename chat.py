import requests
import json
import random
import time

# Proxy test function
def test_proxy(proxy):
    test_url = "https://httpbin.org/ip"  # Using httpbin.org to test proxy
    proxies = {
        "http": proxy,
        "https": proxy,
    }

    try:
        # Test the proxy
        res = requests.get(test_url, proxies=proxies)
        if res.status_code == 200:
            print(f"Proxy successful! Response: {res.json()}")
            return True
        else:
            print(f"Failed to connect using proxy: {res.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Proxy test failed: {e}")
        return False

def get_context(wallet_address):
    # Format the message as your text
    return f"{wallet_address}"

def send_message(channel_id, authorization, proxy, wallet_address):
    # Check if the proxy is valid before sending the message
    if proxy and not test_proxy(proxy):  # Only test proxy if it's provided
        print(f"Skipping message for wallet {wallet_address} due to proxy failure.")
        return

    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    msg = {
        "content": get_context(wallet_address),
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
        "tts": False,
    }

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    # Set up proxy for the request, if provided
    proxies = None
    if proxy:
        proxies = {
            "http": proxy,
            "https": proxy,
        }

    try:
        # Send the request with proxy, if provided
        res = requests.post(url=url, headers=header, data=json.dumps(msg), proxies=proxies)

        # Print out the response status and content for debugging
        if res.status_code == 200:
            print(f"Message sent to channel {channel_id} successfully for wallet: {wallet_address}")
        else:
            print(f"Failed to send message for wallet {wallet_address}: {res.status_code}, {res.content}")
    except requests.exceptions.RequestException as e:
        print(f"Request error while sending message for wallet {wallet_address}: {e}")
    except Exception as e:
        print(f"Unexpected error for wallet {wallet_address}: {e}")

def load_credentials(auth_file, proxy_file):
    auth_data = []
    proxy_data = []

    # Load auth credentials
    with open(auth_file, 'r') as f:
        for line in f.readlines():
            auth_info = line.strip().split('|')
            if len(auth_info) == 2:
                auth_data.append({'auth': auth_info[0], 'wallet_address': auth_info[1]})

    # Load proxy information (if provided)
    if proxy_file:
        with open(proxy_file, 'r') as f:
            for line in f.readlines():
                proxy_data.append(line.strip())

    return auth_data, proxy_data

def chat(channel_id, auth_data, proxy_data):
    while True:
        for auth_info, proxy in zip(auth_data, proxy_data):
            authorization = auth_info['auth']
            wallet_address = auth_info['wallet_address']

            # Send the message
            send_message(channel_id, authorization, proxy, wallet_address)

            # Wait for a few seconds before sending the next message (per account)
            sleep_time = random.randint(3, 5)  # 3 to 5 seconds delay between each account
            print(f"Sleeping for {sleep_time} seconds before sending the next message.")
            time.sleep(sleep_time)

        # After all accounts have sent their messages, wait 2 hours before the next round
        print("Waiting 2 hours before sending the next round of messages.")
        time.sleep(2 * 3600)  # Sleep for 2 hours

if __name__ == "__main__":
    channel_id = "1342142136778489876"  # Set your desired channel ID here

    # Load credentials and proxy information from files
    auth_file = 'auth.txt'
    proxy_file = 'proxy.txt'
    auth_data, proxy_data = load_credentials(auth_file, proxy_file)

    # Start the chat loop
    chat(channel_id, auth_data, proxy_data)
