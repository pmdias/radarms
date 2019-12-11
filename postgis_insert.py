#!/usr/bin/env python3
import argparse
import datetime
import subprocess
import shlex
import tempfile


DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
INSERT_TEMPLATE = "INSERT INTO radar_index VALUES (DEFAULT, \'{timestamp_string}\', \'{filename_path}\', ST_GeometryFromText(\'POLYGON((-1386461.4373346097 5433442.856652737, -483734.95105999254 5433442.856652737, -483734.95105999254 4030348.045529727, -1386461.4373346097 4030348.045529727, -1386461.4373346097 5433442.856652737))\', 3857));"


parser = argparse.ArgumentParser(description='Update the time dimension database')
parser.add_argument('--timestamp',
    required=True,
    type=lambda x: datetime.datetime.strptime(x, DATETIME_FORMAT),
    help='Timestamp of the target radar image, defaults to the current date and time',)
parser.add_argument('--filename',
    required=True,
    type=str,
    help='Absolute filename for the respective VRT for the passed timestamp',)
parser.add_argument('--container',
    required=True,
    type=str,
    help='Container name where we will run the psql command',)
parser.add_argument('--connection',
    type=str,
    default='postgresql://radar:radar@localhost',
    help='Connection string for the psql command',)


def clean_timestamp(timestamp):
    """
    Moves the timestamp to the previous minute that is a multiple
    of 5.
    """
    value = timestamp.minute % 5
    return timestamp - datetime.timedelta(minutes=value)


if __name__ == '__main__':
    args = parser.parse_args()
    command = INSERT_TEMPLATE.format(
        timestamp_string=clean_timestamp(args.timestamp).strftime('%Y-%m-%dT%H:%M:00'),
        filename_path=args.filename
    )

    full_cmd = "docker exec {container} psql {connection} -c \"{command}\"".format(
        container=args.container,
        connection=args.connection,
        command=command,
    )

    subprocess.run(shlex.split(full_cmd))
