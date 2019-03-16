from lib.base_action import HDFSAction


class HDFSSetReplication(HDFSAction):

    def __init__(self, config):
        super(HDFSSetReplication, self).__init__(config=config)
        self.config = config

    def run(self, path, replication_factor, **kwargs):
        client = self.connect(**kwargs)
        return client.set_replication(path, replication_factor)
