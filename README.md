# HDFS Integration Pack

Interact with HDFS via WebHDFS interface

## Configuration

Copy the example configuration in [hdfs.yaml.example](./hdfs.yaml.example)
to `/opt/stackstorm/configs/hdfs.yaml` and edit as required.

All config parameters can be either configured in the configuration file or passed as action arguments (the latter has precedence).

* ``nameservices_url`` (mandatory): List of namenodes URL addresses to connect to. 
* ``mounts`` (mandatory): Mount point for it
* ``user`` (mandatory): The username used to connect to the cluster, valid only with NONE authentication.
* ``auth_mechanism`` (optional): Authentication Method to use, one of "NONE", "GSSAPI", "TOKEN". Defaults to "NONE".
* ``mutual_auth`` (optional): One of "OPTIONAL", "REQUIRED", "DISABLED". Defaults to "OPTIONAL"
* ``max_concurrency`` (optional): Max threads to allow for concurent jobs. Defaults to 10.
* ``token`` (optional): The tocken to use to authenticate when using token authentication.
* ``proxy`` (optional): User to proxy as.
* ``root`` (optional): Root path, this will be prefixed to all HDFS paths passed to the client. If the root is relative, the path will be assumed relative to the user's home directory.
* ``call_timeout`` (optional): Connection timeouts, forwarded to the request handler.
* ``verify`` (optional): If the Namenode certificate should be verified or not when using SSL. Defaults to False.
* ``truststore`` (optional): Path to a Truststore file.

If you have unsecured access to HDFS, you only need to setup **nameservices_url** and **mounts** parameters. 

Configuration example:

```yaml
---
nameservices_url:
- "http://namenode1:50070"
- "http://namenode2:50070"
mounts: "/"
user: "username"
auth_mechanism: "NONE"
verify: False
mutual_auth: "OPTIONAL"
max_concurrency: 10
token: "YOURTOKEN"
proxy: "proxieduser"
root: "/home/username"
timeout: 5
truststore: "/path/to/truststore.jks"
```

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* ``get_content_summary`` - Get ContentSummary_ for a file or folder on HDFS.
* ``status`` - Get FileStatus_ for a file or folder on HDFS.
* ``delete`` - Remove a file or directory from HDFS.
* ``rename`` - Move a file or folder.
* ``set_owner`` - Change the owner of file.
* ``set_permission`` - Change the permissions of file.
* ``set_times`` - Change remote timestamps.
* ``set_replication`` - Set file replication.
* ``makedirs`` - Create a remote directory, recursively if necessary.
* ``checksum`` - Get a remote file's checksum.
* ``list`` - Return names of files contained in a remote folder.
* ``makedirs`` - Create a remote directory, recursively if necessary.
* ``walk`` - Depth-first walk of remote filesystem.
* ``create_snapshot`` - Create a Snapshot on a particular HDFS directory.
* ``delete_snapshot`` - Delete a Snapshot on a particular HDFS directory.
* ``rename_snapshot`` - Rename a Snapshot on a particular HDFS directory.
* ``list_snapshots`` - List snapshots on a particular HDFS directory.
* ``getxattrs`` - Get extended attributes on a particular path.
* ``listxattrs`` - List all existing extended attributes on a particular path.
* ``removexattr`` - Remove an extended attribute.
* ``setxattr`` - Set or update an extended attribute.
