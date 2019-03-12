# HDFS Integration Pack

Interact with HDFS (Hadoop Distributed File System) via the WebHDFS REST API

* Tested with Hortonworks Data Platform (HDP) 2.6.4 (HDFS 2.7.3)
* Using [pywhdfs](https://github.com/yassineazzouz/pywhdfs) library for all interaction with WebHDFS and HTTFS Rest API

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

If you have unsecured access to HDFS, you only need to setup **nameservices_url**, **mounts** and **user** parameters. 

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
* ``download`` - Download a file or folder from HDFS and save it locally.
* ``upload`` - Upload a local file or directory to HDFS.
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
* ``cancel_delegation_token`` - Cancel an existing delegation token.
* ``renew_delegation_token`` - Renew an existing delegation token.
* ``list_delegation_token`` - Get one or more delegation tokens associated with the filesystem.
* ``get_delegation_token`` - Get a new delegation token for this file system.
* ``check_access_to_path`` - Checks if the user can access a path. The mode specifies which access checks to perform.
* ``get_acl_status`` - Get getAclStatus return the ACLS for a file or folder on HDFS.
* ``set_acl`` - Fully replaces ACL of files and directories, discarding all existing entries.
* ``remove_acl`` - Removes all but the base ACL entries of files and directories. The entries for user, group, and others are retained for compatibility with permission bits.
* ``remove_default_acl`` - Removes all default ACL entries from files and directories.
* ``remove_acl_entries`` - Removes ACL entries from files and directories. Other ACL entries are retained.
* ``modify_acl_entries`` - Modifies ACL entries of files and directories. This method can add new ACL entries or modify the permissions on existing ACL entries. All existing ACL entries that are not specified in this call are retained without changes.

## Notes

* Most methods and parameter descriptions were directly taken from the docstring of [pywhdfs](https://github.com/yassineazzouz/pywhdfs) project
* Apache®, Apache Hadoop, Hadoop®, and the yellow elephant logo are either registered trademarks or trademarks of the Apache Software Foundation in the United States and/or other countries.