# smart_lock

Update packages

```sh
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo rpi-update -y
```

Enable ssh

```sh
touch /Volumes/boot/ssh
```

Enable Wi-Fi

```sh
# Edit /Volumes/boot/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}
```

https://howchoo.com/g/mzgzy2mwowj/how-to-set-up-raspberry-pi-without-keyboard-monitor-mouse

```sh
sudo apt-get install -y supervisor
```

```sh
# Edit /etc/supervisor/conf.d/smart_lock.conf
[program:smart_lock]
command=[project root]/nfc.py ;
numprocs=1           ;
redirect_stderr=true ;
stdout_logfile=[project root]/nfc.log ;
user=root ;
```

```sh
sudo systemctl start supervisor
sudo supervisorctl reload
sudo supervisorctl start smart_lock
```




