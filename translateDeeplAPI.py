import pycurl
from io import BytesIO
import urllib.parse
import json

def translateDeeplAPI(text):
	b_obj = BytesIO()

	crl = pycurl.Curl()
	crl.setopt(crl.URL, "https://api-free.deepl.com/v2/translate")
	crl.setopt(crl.WRITEDATA, b_obj)

	post_data = {"auth_key" : "c29c6eb6-c616-e46c-afd1-713f5a46ce77:fx",
	     	     "text" : text,
	     	     "source_lang" : "EN",
	     	     "target_lang" : "FR"}

	postfields = urllib.parse.urlencode(post_data)

	crl.setopt(crl.POSTFIELDS, postfields)

	crl.perform()
	crl.close()

	res_json = json.loads(b_obj.getvalue().decode("utf8"))
	return res_json["translations"][0]["text"]
