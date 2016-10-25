from errbot import BotPlugin, botcmd
from errbot.templating import tenv
import logging

log = logging.getLogger(name='errbot.plugins.hello')

class Hello(BotPlugin):

    def callback_connect(self):
        log.debug('[hello] >>>>>>>>>>>> invoke callback_connect.')
        pass

    def callback_message(self, message):
        log.debug('[hello] >>>>>>>>>>>> invoke callback_message. got [message = {0}]'.format(message))
        pass

    @botcmd
    def hi(self, msg, args):
        return 'hi, It *works* !'

    @botcmd(template="hello")
    def templ(self, msg, args):  
        response = tenv().get_template('hello.md').render(name=args)
        self.send(msg.frm, response) 