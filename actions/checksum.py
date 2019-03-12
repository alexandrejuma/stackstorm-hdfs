from lib.base_action import HDFSAction


class HDFSFileChecksum(HDFSAction):

    def __init__(self, config):
        super(HDFSFileChecksum, self).__init__(config=config)
        self.config = config

    def run(self, file_path, nameservices_url=None, mounts=None, user=None, auth_mechanism=None, mutual_auth=None,
            max_concurrency=None, token=None, proxy=None, root=None, call_timeout=None, verify=None, truststore=None):
        client = self.connect(nameservices_url, mounts, user, auth_mechanism, mutual_auth, max_concurrency, token,
                              proxy, root, call_timeout, verify, truststore)
        return client.checksum(file_path)
