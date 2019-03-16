from lib.base_action import HDFSAction


class HDFSFileContentSummary(HDFSAction):

    def __init__(self, config):
        super(HDFSFileContentSummary, self).__init__(config=config)
        self.config = config

    def run(self, path, strict=True, **kwargs):
        client = self.connect(**kwargs)
        return client.content(path, strict)
