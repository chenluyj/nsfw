import asyncio

import tornado.web
import tornado.autoreload
from nsfwUtil import load_image,nsfw_predict

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ok")
class NsfwHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self, *args, **kwargs):
        ret = {"ret":0}
        try:
            data = tornado.escape.json_decode(self.request.body)
            imagedate = load_image(data['url'])
            predict = nsfw_predict(imagedate)
            predict['ret']=0
            ret = predict
        except Exception as e:
            ret = {"ret":-1}
        self.write(ret)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/nsfw", NsfwHandler),
    ],debug=True)


async def main():
    app = make_app()
    print ("Starting 8888 ......")
    app.listen(8888)
    await asyncio.Event().wait()
if __name__ == "__main__":
    asyncio.run(main())

