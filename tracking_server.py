from flask import Flask, request

app = Flask(__name__)


@app.route('/tracking_image.jpg')
def tracking_image():
    # Capture information from the request
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Log the captured information
    with open('tracking_logs.txt', 'a') as f:
        f.write(f'IP Address: {ip_address}, User-Agent: {user_agent}\n')

    # Respond with a transparent 1x1 pixel image
    transparent_pixel = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
    return transparent_pixel, 200, {'Content-Type': 'image/gif'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
