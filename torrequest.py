import requests


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    response = requests.get("https://listado.mercadolibre.com.ar", proxies=session.proxies)
    print(response)
    return session


# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("https://listado.mercadolibre.com.ar").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)