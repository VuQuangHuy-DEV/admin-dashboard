import requests
from constants.sms_url import sms_url
from infobip_channels.sms.channel import SMSChannel


def send_otp_dev(phone_number, otp):
    if phone_number is None:
        return

    try:
        content = str(otp)

        data = {
            "phone_number": str(phone_number),
            "content": content
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(sms_url, json=data, headers=headers)

        return response

    except Exception as e:
        print(f"An error occurred: {e}")


def send_otp_beta(phone_number, otp):
    try:
        # BASE_URL = "https://w14l4y.api.infobip.com"
        BASE_URL = "https://k296xx.api.infobip.com"
        API_KEY = "997a261c95b749252ca11500a2aee0f1-17f27fbf-9e7f-4698-9e8e-4c97325f3189"
        # RECIPIENT = "84386426141"
        channel = SMSChannel.from_auth_params(
            {
                "base_url": BASE_URL,
                "api_key": API_KEY,
            }
        )

        # Send a message with the desired fields.
        response = channel.send_sms_message(
            {
                "messages": [
                    {
                        "from": "BIXSOVN",
                        "destinations": [{"to": phone_number}],
                        "text": f"Mã xác thực Xế ơi của bạn là: {otp}",
                    }
                ]
            }
        )

        # Get delivery reports for the message. It may take a few seconds show the just-sent message.
        # query_parameters = {"limit": 10}
        # delivery_reports = channel.get_outbound_sms_delivery_reports(query_parameters)

        # See the delivery reports.
        return response
    except Exception as e:
        print(f"An error occurred: {e}")


def process_send_otp(phone_number, otp):
    phone_number = str(phone_number)
    log = 'Begin send sms by send_otp_beta...\n'
    rep = send_otp_beta(phone_number, otp)
    if not rep or rep.status_code != 200:
        log += f"[BETA] Failed to send OTP to {phone_number}. Full: {rep}\n"

        rep2 = send_otp_dev(phone_number, otp)
        if not rep2 or rep2.status_code != 200:
            log += f"[DEV] Failed to send OTP to {phone_number}. Full: {rep2}\n"
        else:
            log += '[DEV] Sent successfully.'

    else:
        log += '[BETA] Sent successfully.'

    return log


