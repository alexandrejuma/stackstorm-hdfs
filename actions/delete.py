from lib.base_action import HDFSAction


class HDFSDelete(HDFSAction):

    def __init__(self, config):
        super(HDFSDelete, self).__init__(config=config)
        self.config = config

    def run(self, path, recursive=False, **kwargs):
        client = self.connect(**kwargs)
        return client.delete(path, recursive)
