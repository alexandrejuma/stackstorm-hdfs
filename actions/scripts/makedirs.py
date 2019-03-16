from lib.base_action import HDFSAction


class HDFSMakeDirs(HDFSAction):

    def __init__(self, config):
        super(HDFSMakeDirs, self).__init__(config=config)
        self.config = config

    def run(self, path, permission=None, **kwargs):
        client = self.connect(**kwargs)
        return client.makedirs(path, permission)
