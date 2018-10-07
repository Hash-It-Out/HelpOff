from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput
from pprint import pprint

class ToneAnalyze():

    def analyze(message):



        service = ToneAnalyzerV3(
            ## url is optional, and defaults to the URL below. Use the correct URL for your region.
            # url='https://gateway.watsonplatform.net/tone-analyzer/api',
            username='f0ec47cc-5191-4421-8fca-2395917e1640',
            password='q7JOpjOabiY5',
            version='2017-09-21')
        tone_input = ToneInput(message)
        result = service.tone(tone_input=tone_input, content_type="application/json").get_result()
        return result