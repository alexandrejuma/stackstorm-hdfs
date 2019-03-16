from lib.base_action import HDFSAction


class HDFSWalk(HDFSAction):

    def __init__(self, config):
        super(HDFSWalk, self).__init__(config=config)
        self.config = config

    def run(self, path, depth=0, status=False, **kwargs):
        client = self.connect(**kwargs)
        return client.walk(path, depth, status)
