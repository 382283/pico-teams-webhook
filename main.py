import network
import urequests
import time
import config

print("Connecting to Wi-Fi...")

# WiFi接続
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.SSID, config.PASSWORD)

# 接続を待つ
while not wlan.isconnected():
    time.sleep(1)

print("Connected!!")
print(wlan.ifconfig())

# Teamに送る用のデータ
data = {
    "text" : "Pico Wから送信テスト"
}

print("Sending webhook...")

#webhook送信
response = urequests.post(config.WEBHOOK_URL,
 json = data)

print("Status:", response.status_code)

print("Done!!")