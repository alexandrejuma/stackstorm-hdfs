from lib.base_action import HDFSAction


class HDFSSetPermission(HDFSAction):

    def __init__(self, config):
        super(HDFSSetPermission, self).__init__(config=config)
        self.config = config

    def run(self, path, permission, **kwargs):
        client = self.connect(**kwargs)
        return client.set_permission(path, permission)
