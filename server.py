from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
import joblib
import ssl


clf = joblib.load('model.joblib')

class echoHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		if self.path == '/predict':
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length)
			print(post_data)
			# test_data=[1,1,1]
			test_data = post_data.decode().strip('}{').split(':')[1]
			test_data = test_data.strip('[]').split(',')
			test_data = [int(x) for x in test_data]
			print(test_data)
			prediction = clf.predict([test_data])
			print(prediction)
			prediction_json = json.dumps(str(prediction[0]))
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()
			self.wfile.write(prediction_json.encode())
		else:
			self.send_error(404)
		
	def do_GET(self):
		if self.path == '/':
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(b'<html><head><title>Simple Server</title></head>')
			self.wfile.write(b'<body><h1>Hello, world!</h1></body></html>')
		else:
			self.send_error(404)
			
def run_server():
	server_address = ('192.168.116.41', 8000)
	httpd = HTTPServer(server_address, echoHandler)
	print('Starting server on port 8000...')
	httpd.serve_forever()

if __name__ == '__main__':
	run_server()
