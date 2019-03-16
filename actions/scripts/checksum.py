from lib.base_action import HDFSAction


class HDFSFileChecksum(HDFSAction):

    def __init__(self, config):
        super(HDFSFileChecksum, self).__init__(config=config)
        self.config = config

    def run(self, file_path, **kwargs):
        client = self.connect(**kwargs)
        return client.checksum(file_path)
