# -*- coding: utf-8 -*-
from intelmq.lib.bot import Bot


class ExampleExpertBot(Bot):

    def init(self):
        self.logger.info('test')
        self.logger.info('test2')

    def process(self):
        pass


BOT = ExampleExpertBot
