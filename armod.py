## -- Decryptor for AR Mod VPN Configuration files.--

## -- Decryption Script -- Made With Love By Project SSLaB LK 🇱🇰 using the Hc Tools Codebase --

## -- Dev : Master ShayCormac --

from Crypto.Cipher import AES
from base64 import b64decode
from urllib.parse import unquote
print('')
print('')
print('      ███████╗███████╗██╗      █████╗ ██████╗     ██╗     ██╗  ██╗')
print('      ██╔════╝██╔════╝██║     ██╔══██╗██╔══██╗    ██║     ██║ ██╔╝')
print('      ███████╗███████╗██║     ███████║██████╔╝    ██║     █████╔╝ ')
print('      ╚════██║╚════██║██║     ██╔══██║██╔══██╗    ██║     ██╔═██╗ ')
print('      ███████║███████║███████╗██║  ██║██████╔╝    ███████╗██║  ██╗')
print('      ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═╝')
print('')
print ('              =============== ꜱʜᴀʏ ᴄᴏʀᴍᴀᴄ ===============')
print('')
def armodvpn(key:str|bytes='artunnel57122611'):
    key = key.encode('utf-8')
    config_encrypt = str(input('[•] Enter encryption config:'))
    
    if config_encrypt.find('ar-ssh://') or config_encrypt.find('ar-vmess://') != -1:
        try:ciphertext = b64decode(config_encrypt.split('ar-ssh://')[1])
        except:ciphertext = b64decode(config_encrypt.split('ar-vmess://')[1])
        cipher = AES.new(key, AES.MODE_ECB)
        
        plain_encoded = cipher.decrypt(ciphertext).decode()
        full_decoded = unquote(plain_encoded)
        print('')
        print(' =============== ʙʏ ᴘʀᴏᴊᴇᴄᴛ ꜱꜱʟᴀʙ ʟᴋ ===============')
        print('\n ',full_decoded)
        print('')
        print(' =============== ʙʏ ᴘʀᴏᴊᴇᴄᴛ ꜱꜱʟᴀʙ ʟᴋ ===============')
    else:
        print('[ * ] Invalid config.')

if __name__ == '__main__':
    armodvpn()
