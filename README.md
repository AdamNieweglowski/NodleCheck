# NodleCheck

Skrypt sprawdza kiedy ostatni raz pojawiła się nagroda dla zdefiniowanych portfeli. Jeśli jest większa niż wartość określona w alert_time (domyślnie 12h) przychodzi alert na telegram.

Wymagane ustawienia w konffiguracji:
subscan_token - należy zarestrowac się na https://pro.subscan.io/login i wygenerować token api
telegram_chatid - wysłanie do bota http://t.me/Nodle_Wallet_Checker_bot komendy /start, następnie otworzenie https://api.telegram.org/bot5578491077:AAG4dWtmcdE2bCyCxULHP_xCRAgQraISMJE/getUpdates i pobranie wartości chat[id] (lub stworzenie własnego bota - https://core.telegram.org/bots#6-botfather)

W pliku wallets.txt umieszamy opis koparki oddzielony średnikiem od klucza publicznego (przykładowe adresy znalezione w sieci:P)

Wszelakie sugestie i uwagi mile widziane - https://discord.com/channels/783056826618216498/887572254987288606 

W celu zutomatyzacji skrypt odpalamy w cronie (tu co 4h)
0 */4 * * * /usr/bin/python3 /opt/nodle/nodle_check.py


Sponsor / Support 
NODLE address: 4mfeRtTcRtaguaq7swCbDKdEzm4ELeJPmW2M9aifpDHbVk9C
