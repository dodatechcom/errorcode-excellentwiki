---
title: "Windows NTSTATUS Error Codes — Complete Reference"
description: "Complete reference table of Windows NTSTATUS error codes from Microsoft MS-ERREF. Find error code meanings and quick fixes."
platforms: ["windows"]
severities: ["error"]
weight: 5
---

# Windows NTSTATUS Error Codes — Complete Reference

NTSTATUS is a 32-bit numbering space used by the Windows NT kernel to represent error, warning, and informational conditions. Error codes follow the format `0xC000xxxx` (error) and `0x8000xxxx` (warning). This table covers the most commonly encountered codes from Microsoft's [MS-ERREF](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) documentation.

## Error Codes (0xC000xxxx)

| Code | Name | Description | Quick Fix |
|------|------|-------------|-----------|
| 0xC0000005 | STATUS_ACCESS_VIOLATION | The instruction referenced memory that could not be read, written, or executed. | Run SFC /scannow |
| 0xC0000008 | STATUS_INVALID_HANDLE | An invalid HANDLE was specified. | Restart the application |
| 0xC000000D | STATUS_INVALID_PARAMETER | An invalid parameter was passed to a service or function. | Verify input parameters |
| 0xC000000E | STATUS_NO_SUCH_DEVICE | A device that does not exist was specified. | Check hardware connections |
| 0xC000000F | STATUS_NO_SUCH_FILE | The file does not exist. | Verify file path |
| 0xC0000010 | STATUS_INVALID_DEVICE_REQUEST | The specified request is not a valid operation for the target device. | Update device driver |
| 0xC0000011 | STATUS_END_OF_FILE | The end-of-file marker has been reached. | Check file integrity |
| 0xC0000017 | STATUS_NO_MEMORY | Not enough virtual memory or paging file quota is available. | Increase virtual memory |
| 0xC000001D | STATUS_ILLEGAL_INSTRUCTION | An attempt was made to execute an illegal instruction. | Reinstall the application |
| 0xC0000022 | STATUS_ACCESS_DENIED | A process has requested access to an object but has not been granted those access rights. | Check file permissions |
| 0xC0000023 | STATUS_BUFFER_TOO_SMALL | The buffer is too small to contain the entry. | Increase buffer size |
| 0xC0000032 | STATUS_DISK_CORRUPT_ERROR | The file system structure on the disk is corrupt and unusable. | Run chkdsk /f /r |
| 0xC0000034 | STATUS_OBJECT_NAME_NOT_FOUND | The object name is not found. | Verify object path exists |
| 0xC0000035 | STATUS_OBJECT_NAME_COLLISION | The object name already exists. | Choose a different name |
| 0xC0000039 | STATUS_OBJECT_PATH_INVALID | The object path component was not a directory object. | Check directory structure |
| 0xC000003A | STATUS_OBJECT_PATH_NOT_FOUND | The path does not exist. | Verify path spelling |
| 0xC0000043 | STATUS_SHARING_VIOLATION | A file cannot be opened because the share access flags are incompatible. | Close other file handles |
| 0xC0000044 | STATUS_QUOTA_EXCEEDED | Insufficient quota exists to complete the operation. | Increase user quota |
| 0xC000005E | STATUS_NO_LOGON_SERVERS | No logon servers are currently available. | Check network connectivity |
| 0xC0000061 | STATUS_PRIVILEGE_NOT_HELD | A required privilege is not held by the client. | Run as administrator |
| 0xC0000064 | STATUS_NO_SUCH_USER | The specified account does not exist. | Verify username spelling |
| 0xC000006A | STATUS_WRONG_PASSWORD | The value provided as the current password is not correct. | Reset your password |
| 0xC000006C | STATUS_PASSWORD_RESTRICTION | Some password update rule has been violated. | Choose a stronger password |
| 0xC000006D | STATUS_LOGON_FAILURE | The attempted logon is invalid. This is either due to a bad username or authentication information. | Verify credentials |
| 0xC000006E | STATUS_ACCOUNT_RESTRICTION | Some user account restriction has prevented successful authentication. | Contact your administrator |
| 0xC000006F | STATUS_INVALID_LOGON_HOURS | The user account has time restrictions and cannot be logged onto at this time. | Log on during allowed hours |
| 0xC0000070 | STATUS_INVALID_WORKSTATION | The user account cannot be used to log on from the source workstation. | Log on from an allowed station |
| 0xC0000071 | STATUS_PASSWORD_EXPIRED | The user account password has expired. | Reset your password |
| 0xC0000072 | STATUS_ACCOUNT_DISABLED | The referenced account is currently disabled. | Enable the account |
| 0xC000007A | STATUS_PROCEDURE_NOT_FOUND | The specified procedure address cannot be found in the DLL. | Update or reinstall DLL |
| 0xC000007B | STATUS_INVALID_IMAGE_FORMAT | The image is either not designed to run on Windows or it contains an error. | Reinstall the application |
| 0xC000007F | STATUS_DISK_FULL | An operation failed because the disk was full. | Free up disk space |
| 0xC0000095 | STATUS_INTEGER_OVERFLOW | A signed integer operation resulted in an overflow. | Update the software |
| 0xC0000097 | STATUS_TOO_MANY_PAGING_FILES | An attempt was made to install more paging files than the system supports. | Reduce paging files |
| 0xC000009A | STATUS_INSUFFICIENT_RESOURCES | Insufficient system resources exist to complete the API. | Reboot the computer |
| 0xC000009C | STATUS_DEVICE_DATA_ERROR | There are bad blocks (sectors) on the hard disk. | Replace the hard drive |
| 0xC000009D | STATUS_DEVICE_NOT_CONNECTED | Bad cabling, non-termination, or controller cannot access the hard disk. | Check cable connections |
| 0xC00000A2 | STATUS_MEDIA_WRITE_PROTECTED | The disk cannot be written to because it is write-protected. | Remove write protection |
| 0xC00000A3 | STATUS_DEVICE_NOT_READY | The drive is not ready for use; its door might be open. | Check drive door and media |
| 0xC00000B5 | STATUS_IO_TIMEOUT | The specified I/O operation was not completed before the time-out period expired. | Check device connections |
| 0xC00000B6 | STATUS_FILE_FORCED_CLOSED | The specified file has been closed by another process. | Reopen the file |
| 0xC00000BA | STATUS_FILE_IS_A_DIRECTORY | The target file is a directory. | Specify a file, not a directory |
| 0xC00000BB | STATUS_NOT_SUPPORTED | The request is not supported. | Check feature compatibility |
| 0xC00000BC | STATUS_REMOTE_NOT_LISTENING | This remote computer is not listening. | Verify remote host is online |
| 0xC00000BF | STATUS_NETWORK_BUSY | The network is busy. | Retry after a short delay |
| 0xC00000C0 | STATUS_DEVICE_DOES_NOT_EXIST | This device does not exist. | Reinstall device driver |
| 0xC00000C4 | STATUS_UNEXPECTED_NETWORK_ERROR | An unexpected network error occurred. | Check network hardware |
| 0xC00000C9 | STATUS_NETWORK_NAME_DELETED | The network name was deleted. | Reconnect to the share |
| 0xC00000CA | STATUS_NETWORK_ACCESS_DENIED | Network access is denied. | Check share permissions |
| 0xC00000CC | STATUS_BAD_NETWORK_NAME | The specified share name cannot be found on the remote server. | Verify share name |
| 0xC00000CD | STATUS_TOO_MANY_NAMES | The name limit for the network adapter was exceeded. | Reduce network connections |
| 0xC00000CE | STATUS_TOO_MANY_SESSIONS | The network BIOS session limit was exceeded. | Disconnect other sessions |
| 0xC00000D0 | STATUS_REQUEST_NOT_ACCEPTED | The computer has already accepted the maximum number of connections. | Close existing connections |
| 0xC00000D4 | STATUS_NOT_SAME_DEVICE | The destination file is located on a different device than the source. | Move to the same volume |
| 0xC00000D6 | STATUS_VIRTUAL_CIRCUIT_CLOSED | The session with a remote server has been disconnected due to timeout. | Reconnect to the server |
| 0xC00000DA | STATUS_CANT_ACCESS_DOMAIN_INFO | Configuration information could not be read from the domain controller. | Verify domain connectivity |
| 0xC00000E5 | STATUS_INTERNAL_ERROR | An internal error occurred. | Restart the application |
| 0xC00000E9 | STATUS_UNEXPECTED_IO_ERROR | An unexpected I/O error occurred. | Check hardware status |
| 0xC00000FD | STATUS_STACK_OVERFLOW | A new guard page for the stack cannot be created. | Increase stack size |
| 0xC0000101 | STATUS_DIRECTORY_NOT_EMPTY | The directory trying to be deleted is not empty. | Remove directory contents first |
| 0xC0000102 | STATUS_FILE_CORRUPT_ERROR | The file or directory is corrupt and unreadable. | Run chkdsk or restore file |
| 0xC000010B | STATUS_FILES_OPEN | Cannot force close files on a redirected drive with open handles. | Close all handles first |
| 0xC000011F | STATUS_TOO_MANY_OPENED_FILES | Too many files are opened on a remote server. | Close unused file handles |
| 0xC0000120 | STATUS_CANCELLED | The I/O request was canceled. | Retry the operation |
| 0xC0000121 | STATUS_CANNOT_DELETE | An attempt has been made to remove a file or directory that cannot be deleted. | Check delete permissions |
| 0xC0000128 | STATUS_FILE_CLOSED | An I/O request was attempted on a file object that had already been closed. | Reopen the file |
| 0xC000012B | STATUS_TOKEN_ALREADY_IN_USE | The token is already in use as a primary token. | Terminate the other process |
| 0xC000012C | STATUS_PAGEFILE_QUOTA_EXCEEDED | The page file quota was exceeded. | Increase page file size |
| 0xC000012D | STATUS_COMMITMENT_LIMIT | Your system is low on virtual memory. | Increase virtual memory |
| 0xC0000135 | STATUS_DLL_NOT_FOUND | This application has failed to start because a DLL was not found. | Reinstall the application |
| 0xC0000138 | STATUS_ORDINAL_NOT_FOUND | The ordinal could not be located in the DLL. | Reinstall the application |
| 0xC0000139 | STATUS_ENTRYPOINT_NOT_FOUND | The procedure entry point could not be located in the DLL. | Update the DLL |
| 0xC000013A | STATUS_CONTROL_C_EXIT | The application terminated as a result of a CTRL+C. | Check for console input issues |
| 0xC0000142 | STATUS_DLL_INIT_FAILED | Initialization of the DLL failed. The process is terminating. | Reinstall the application |
| 0xC0000143 | STATUS_MISSING_SYSTEMFILE | The required system file is bad or missing. | Run SFC /scannow |
| 0xC0000144 | STATUS_UNHANDLED_EXCEPTION | An unhandled exception occurred in the application. | Update or reinstall app |
| 0xC0000145 | STATUS_APP_INIT_FAILURE | The application failed to initialize properly. | Reinstall the application |
| 0xC000014B | STATUS_PIPE_BROKEN | The pipe operation has failed because the other end has been closed. | Restart the service |
| 0xC000014C | STATUS_REGISTRY_CORRUPT | The structure of one of the files that contains registry data is corrupt. | Restore registry backup |
| 0xC000014D | STATUS_REGISTRY_IO_FAILED | An I/O operation initiated by the Registry failed. | Check disk and reboot |
| 0xC000014F | STATUS_UNRECOGNIZED_VOLUME | The volume does not contain a recognized file system. | Run chkdsk or reformat |
| 0xC0000154 | STATUS_ALIAS_EXISTS | The specified local group already exists. | Choose a different name |
| 0xC000017C | STATUS_KEY_DELETED | An illegal operation was attempted on a registry key marked for deletion. | Refresh the registry key |
| 0xC0000182 | STATUS_DEVICE_CONFIGURATION_ERROR | The I/O device is configured incorrectly. | Check device settings |
| 0xC0000185 | STATUS_IO_DEVICE_ERROR | The I/O device reported an I/O error. | Check device or replace cable |
| 0xC000018C | STATUS_TRUSTED_DOMAIN_FAILURE | The trust relationship between the primary domain and trusted domain failed. | Reestablish trust |
| 0xC000018D | STATUS_TRUSTED_RELATIONSHIP_FAILURE | The trust relationship between this workstation and the primary domain failed. | Reset machine account |
| 0xC000018E | STATUS_EVENTLOG_FILE_CORRUPT | The Eventlog log file is corrupt. | Clear and rebuild event log |
| 0xC000018F | STATUS_EVENTLOG_CANT_START | No Eventlog log file could be opened. | Check event log service |
| 0xC0000190 | STATUS_TRUST_FAILURE | The network logon failed. | Verify trust relationship |
| 0xC0000193 | STATUS_ACCOUNT_EXPIRED | The user account has expired. | Contact your administrator |
| 0xC0000195 | STATUS_NETWORK_CREDENTIAL_CONFLICT | Multiple connections using different user names are not allowed. | Disconnect other connections |
| 0xC0000218 | STATUS_CANNOT_LOAD_REGISTRY_FILE | The registry cannot load the hive. It is corrupt, absent, or not writable. | Restore registry from backup |
| 0xC000021A | STATUS_SYSTEM_PROCESS_TERMINATED | The system process terminated unexpectedly with a fatal system error. | Check event logs, reboot |
| 0xC0000222 | STATUS_LOST_WRITEBEHIND_DATA | Windows was unable to save all the data for the file. Data has been lost. | Save file to different location |
| 0xC0000224 | STATUS_PASSWORD_MUST_CHANGE | The user password must be changed before logging on the first time. | Set a new password |
| 0xC0000225 | STATUS_NOT_FOUND | The object was not found. | Verify the object exists |
| 0xC0000234 | STATUS_ACCOUNT_LOCKED_OUT | The user account has been automatically locked due to too many invalid logon attempts. | Wait or reset password |
| 0xC0000236 | STATUS_CONNECTION_REFUSED | The transport-connection attempt was refused by the remote system. | Check if service is running |
| 0xC000023A | STATUS_CONNECTION_INVALID | An operation was attempted on a nonexistent transport connection. | Reestablish the connection |
| 0xC000023C | STATUS_NETWORK_UNREACHABLE | The remote network is not reachable by the transport. | Check network routing |
| 0xC000023D | STATUS_HOST_UNREACHABLE | The remote system is not reachable by the transport. | Ping the remote host |
| 0xC000023E | STATUS_PROTOCOL_UNREACHABLE | The remote system does not support the transport protocol. | Check protocol settings |
| 0xC000023F | STATUS_PORT_UNREACHABLE | No service is operating at the destination port. | Verify service is listening |
| 0xC0000241 | STATUS_CONNECTION_ABORTED | The transport connection was aborted by the local system. | Check application logs |
| 0xC0000244 | STATUS_AUDIT_FAILED | An attempt to generate a security audit failed. | Check audit policy settings |
| 0xC0000246 | STATUS_CONNECTION_COUNT_LIMIT | The limit on concurrent connections for this account has been reached. | Close existing connections |
| 0xC0000247 | STATUS_LOGIN_TIME_RESTRICTION | Attempting to log on during an unauthorized time of day. | Log on during allowed hours |
| 0xC0000248 | STATUS_LOGIN_WKSTA_RESTRICTION | The account is not authorized to log on from this station. | Log on from an allowed station |
| 0xC0000251 | STATUS_BAD_DLL_ENTRYPOINT | The DLL is not written correctly. The entry point should be WINAPI or STDCALL. | Reinstall the DLL |
| 0xC0000254 | STATUS_IP_ADDRESS_CONFLICT1 | There is an IP address conflict with another system on the network. | Change IP address |
| 0xC0000255 | STATUS_IP_ADDRESS_CONFLICT2 | There is an IP address conflict with another system on the network. | Release and renew IP |
| 0xC0000256 | STATUS_REGISTRY_QUOTA_LIMIT | The system has reached the maximum size allowed for the system part of the registry. | Clean up registry |
| 0xC0000467 | STATUS_FILE_NOT_AVAILABLE | The file is temporarily unavailable. | Retry after a short delay |
| 0xC0000480 | STATUS_SHARE_UNAVAILABLE | The share is temporarily unavailable. | Retry later |

## Warning Codes (0x8000xxxx)

| Code | Name | Description | Quick Fix |
|------|------|-------------|-----------|
| 0x80000005 | STATUS_BUFFER_OVERFLOW | The data was too large to fit into the specified buffer. | Increase buffer size |
| 0x80000006 | STATUS_NO_MORE_FILES | No more files were found which match the file specification. | Verify search criteria |
| 0x8000000A | STATUS_HANDLES_CLOSED | Handles to objects have been automatically closed. | Check handle management |
| 0x80000013 | STATUS_INVALID_EA_NAME | The specified extended attribute name contains illegal characters. | Remove illegal characters |
| 0x80000017 | STATUS_EXTRANEOUS_INFORMATION | The ACL contained more information than was expected. | Verify ACL structure |
| 0x8000001A | STATUS_NO_MORE_ENTRIES | No more entries are available from an enumeration operation. | Reset enumeration |
| 0x8000001D | STATUS_BUS_RESET | An I/O bus reset was detected. | Check hardware connections |
| 0x8000002A | STATUS_REGISTRY_HIVE_RECOVERED | The registry hive was corrupted and has been recovered. Some data might be lost. | Backup registry regularly |
| 0x8000002B | STATUS_DLL_MIGHT_BE_INSECURE | The application is attempting to run executable code from a module that might be insecure. | Use the secure module |
| 0x8000002C | STATUS_DLL_MIGHT_BE_INCOMPATIBLE | The application is loading executable code that might be incompatible with earlier OS versions. | Use the secure module |
| 0x8000002D | STATUS_STOPPED_ON_SYMLINK | The create operation stopped after reaching a symbolic link. | Check symlink targets |
| 0x80000803 | STATUS_DATA_LOST_REPAIR | Windows discovered a corruption in the file and has repaired it. Check for data loss. | Verify file contents |
| 0x801B00EB | STATUS_VIDEO_HUNG_DISPLAY_DRIVER_THREAD_RECOVERED | The display driver stopped working and recovered. Some graphical operations might have failed. | Update display driver |
| 0x80210001 | STATUS_FVE_PARTIAL_METADATA | Volume metadata read or write is incomplete. | Run manage-bde status |
| 0x80210002 | STATUS_FVE_TRANSIENT_STATE | BitLocker encryption keys were ignored because the volume was in a transient state. | Restart and unlock volume |

## How to Use This Reference

1. **Find the code** — Search the table by hex code or name.
2. **Read the description** — Understand what the error means.
3. **Try the quick fix** — Start with the suggested remediation.
4. **Check Event Viewer** — Open `eventvwr.msc` for additional context around the error.
5. **Search Microsoft Docs** — Use the code name as a search term on [learn.microsoft.com](https://learn.microsoft.com) for full documentation.

## Related

- [0xC0000005 — STATUS_ACCESS_VIOLATION](/os/windows/0xc0000005)
- [0xC000021A — STATUS_SYSTEM_PROCESS_TERMINATED](/os/windows/0xc000021a)
- [BSOD: DPC Watchdog Violation](/os/windows/bsod-dpc-watchdog-violation)
- [BSOD: IRQL_NOT_LESS_OR_EQUAL](/os/windows/bsod-irql-not-less-or-equal)
