import json
from envelopes import Envelope
from fortune import get_horoscope
import sys

with open('config.json', 'r') as infile:
	conf = json.load(infile)

ipt = sys.argv[1].upper()
text = get_horoscope(ipt)
#html = "<div style='background-color:purple;color:yellow;font-size:20px'>" + txt + "</div>"
html = text

message = Envelope(
	from_addr=("dtw.yeonhee@gmail.com", "Fortune Teller"),
	to_addr=("signup.yeonhee.lee@gmail.com", "Yeonhee"),
	subject="Today's Horoscope",
	html_body=html
)

# print conf['myEmail']
# print conf['myPassword']

message.send('smtp.googlemail.com', login=conf['myEmail'], password=conf['myPassword'], tls='true')