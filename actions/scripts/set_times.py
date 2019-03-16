from lib.base_action import HDFSAction


class HDFSSetTimes(HDFSAction):

    def __init__(self, config):
        super(HDFSSetTimes, self).__init__(config=config)
        self.config = config

    def run(self, path, access_time=None, modification_time=None, **kwargs):
        client = self.connect(**kwargs)
        return client.set_times(path, access_time, modification_time)
