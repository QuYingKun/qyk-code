import http.server as hs
import sys, os
# encoding: utf-8

class ServerException(Exception):
    pass

class RequestHandler(hs.BaseHTTPRequestHandler):

    def send_CONTENT(self,page,status=200):

        self.send_response(status)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def send_CSS(self, page, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/css")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def send_PNG(self, page, status=200):
        self.send_response(status)
        self.send_header("Content-type", "image/png")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def do_GET(self):
            full_path = os.getcwd() + self.path

            if os.path.isfile(full_path):

             self.handle_file(full_path)

    def handle_file(self,full_path):
            with open(full_path,'rb') as f:
                content = f.read()
            if full_path[-3:] == "css":
                self.send_CSS(content, 200)
            if full_path[-3:] == "png":
                self.send_PNG(content, 200)
            else:
                self.send_CONTENT(content, 200)



if __name__ == '__main__':
 httpAddress = ('',6699)
 httpd = hs.HTTPServer(httpAddress,RequestHandler)
 httpd.serve_forever()

