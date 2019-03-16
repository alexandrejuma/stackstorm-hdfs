from lib.base_action import HDFSAction


class HDFSSetOwner(HDFSAction):

    def __init__(self, config):
        super(HDFSSetOwner, self).__init__(config=config)
        self.config = config

    def run(self, path, owner=None, group=None, **kwargs):
        client = self.connect(**kwargs)
        return client.set_owner(path, owner, group)
