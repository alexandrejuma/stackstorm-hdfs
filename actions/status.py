from lib.base_action import HDFSAction


class HDFSFileStatus(HDFSAction):

    def __init__(self, config):
        super(HDFSFileStatus, self).__init__(config=config)
        self.config = config

    def run(self, path, strict=True, **kwargs):
        client = self.connect(**kwargs)
        return client.status(path, strict)
