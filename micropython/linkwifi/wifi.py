import network  # 导入network包
import time

SSID="iphone4s"  #  WIFI名称
PASSWORD="20040104"  #  WIFI密码

def connectWifi(ssid,passwd):
	global wlan
	wlan=network.WLAN(network.STA_IF)  #  生成wlan对象
	wlan.active(True)  #  开启wlan
	wlan.disconnect()
	wlan.connect(ssid,passwd)  #  连接wlan
	while(wlan.ifconfig()[0]=='0.0.0.0'):
		time.sleep(1)

connectWifi(SSID,PASSWORD)
