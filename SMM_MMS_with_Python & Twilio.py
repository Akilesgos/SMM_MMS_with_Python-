import requests
from twilio.rest import Client

# sudo virtualenv -p python3 sms
account_sid = 'AC94505d002df1d9467c6028dbb47c0117'  # auth_sid
auth_token = '2ed09a15c3e81673508b015e3b312757'  # auth_token
client = Client(account_sid, auth_token)
message_body = '11Hi there'
number_to_text = '+380970568565'
twilio_number = '+19724401750'
mediaUrl = 'http://weknowyourdreams.com/beach.html'
post_data = {
    'From': twilio_number,
    'To': number_to_text,
    'Body': message_body,
    'MediaUrl': ''
    }

"""

Create / Send  --- POST METHOD

"""

message = client.messages.create(
    to=number_to_text,
    from_=twilio_number,
    body=message_body)
print(message.sid)
print(message.media_list.list())

message_data = client.messages.get(sid='MM84e7ab9fd6af47a6a7e4012703ba317c')

print(message_data)
print(dir(message_data))

image_list = [i.uri for i in message_data.media_list.list()]
print(image_list)


"""

Optional
status_callback = website
message = client.messages.create(
    to = number_to_text,
    from_ = twilio_number,
    body = message_body,
    media_url = media_url,
    status_callback = ''
)
"""

url = 'https://api.twilio.com/2010-04-01/Accounts'
message_url = url + '/' + user + '/Messages.json'


def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)


auth_cred = (user, password)

r = requests.get(url, auth=auth)
r2 = requests.post(message_url, date=post_data, auth=auth_cred)

print(r.status_code)

xml_pretty(r.text)

message_url_id = message_url + '/AC94505d002df1d9467c6028dbb47c0117'
get_r = requests.get(message_url_id, auth=auth_cred)
print(r.status_code)

xml_pretty(get_r.text)

get_r.text()
