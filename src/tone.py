from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput
from pprint import pprint


# If service instance provides API key authentication
# service = ToneAnalyzerV3(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/tone-analyzer/api',
#     version='2017-09-21',
#     iam_apikey='your_apikey')

service = ToneAnalyzerV3(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/tone-analyzer/api',
    username='f0ec47cc-5191-4421-8fca-2395917e1640',
    password='q7JOpjOabiY5',
    version='2017-09-21')

# print("\ntone_chat() example 1:\n")
# utterances = [{
#     'text': 'I am very happy.',
#     'user': 'glenn'
# }, {
#     'text': 'It is a good day.',
#     'user': 'glenn'
# }]
# tone_chat = service.tone_chat(utterances).get_result()
# print(json.dumps(tone_chat, indent=2))

# print("\ntone() example 1:\n")
# print(
#     json.dumps(
#         service.tone(
#             tone_input='I am very happy. It is a good day.',
#             content_type="text/plain").get_result(),
#         indent=2))

# print("\ntone() example 2:\n")
# with open(join(dirname(__file__),
#                '../resources/tone-example.json')) as tone_json:
#     tone = service.tone(json.load(tone_json)['text'], "text/plain").get_result()
# print(json.dumps(tone, indent=2))

# print("\ntone() example 3:\n")
# with open(join(dirname(__file__),
#                '../resources/tone-example.json')) as tone_json:
#     tone = service.tone(
#         tone_input=json.load(tone_json)['text'],
#         content_type='text/plain',
#         sentences=True).get_result()
# print(json.dumps(tone, indent=2))

# print("\ntone() example 4:\n")
# with open(join(dirname(__file__),
#                '../resources/tone-example.json')) as tone_json:
#     tone = service.tone(
#         tone_input=json.load(tone_json),
#         content_type='application/json').get_result()
# print(json.dumps(tone, indent=2))

# print("\ntone() example 5:\n")
# with open(join(dirname(__file__),
#                '../resources/tone-example-html.json')) as tone_html:
#     tone = service.tone(
#         json.load(tone_html)['text'], content_type='text/html').get_result()
# print(json.dumps(tone, indent=2))

# print("\ntone() example 6 with GDPR support:\n")
# service.set_detailed_response(True)
# with open(join(dirname(__file__),
#                '../resources/tone-example-html.json')) as tone_html:
#     tone = service.tone(
#         json.load(tone_html)['text'],
#         content_type='text/html',
#         headers={
#             'Custom-Header': 'custom_value'
#         })

# print(tone)
# print(tone.get_headers())
# print(tone.get_result())
# print(tone.get_status_code())
# service.set_detailed_response(False)

# print("\ntone() example 7:\n")

test_tone="Hi Team, The times are difficult! Our sales have been disappointing for the past three quarters for our data analytics product suite. We have a competitive data analytics product suite in the industry. However, we are not doing a good job at selling it, and this is really frustrating.We are missing critical sales opportunities. We cannot blame the economy for our lack of execution. Our clients need analytical tools to change their current business outcomes. In fact, it is in times such as this, our clients want to get the insights they need to turn their businesses around. It is disheartening to see that we are failing at closing deals, in such a hungry market. Let's buckle up and execute.Jennifer BakerSales Leader, North-East region"
tone_input = ToneInput(test_tone)
result = service.tone(tone_input=tone_input, content_type="application/json").get_result()
# print(type(json.dumps(tone, indent=2)))
pprint(result)