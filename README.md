# RPB

## ISO OSI - statnice otazky
1. definuju el. vlast media a prvku na siti. zajisti ze se po spojeni neznici
2. linkova  - aby to doslo kablem
3. sitova - smerovani packetu. routery atd.
4. transportni vrstva - poskladani dat ve spravnem poradi UDP
5. relacni - otevirani spoju, TCP konec. ssh
6. prezentacni - transformace dat do aplikaci citelneho tvaru
7. aplikacni/sluzby - poskytnout app pristup ke komun systemu, protokoly.

## topologie
sbernice - bus, ethernet, hub
hvezda - switch
.....

## IEEE 802.xx

definuje standarty LAN a WAN, podivej se.

broadcast

#install python from scratch
[this thread](https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get)

## test
filtracni tabulka
flags   - communication
        - read/write
        - transmit

# GPIO on beaglebone
[hello world](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/gpio) run as superuser!
ponentiometer as "AIN0"

# add-apt-repository not command
```
sudo apt-get install -y software-properties-common
```
[flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

# next step: play snake from beaglebone!

[link](https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/)

```python
#!/usr/local/bin/python3.5

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('api/potentiometer', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True, host='158.196.21.78')
```
