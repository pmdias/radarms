#!/usr/bin/env python3
import os
import argparse
import datetime
from xml.etree import ElementTree


DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
RADAR_IMAGE_TEMPLATE = '/vsicurl/http://www.ipma.pt/resources.www/transf/radar/por/pcr-%Y-%m-%dT%H%M.png'


parser = argparse.ArgumentParser(description='Create a new VRT file')
parser.add_argument('output',
    type=str,
    help='Output filename, can use format strings to use the timestamp of the file',)
parser.add_argument('--timestamp',
    metavar='T',
    type=lambda x: datetime.datetime.strptime(x, DATETIME_FORMAT),
    default=datetime.datetime.utcnow().strftime(DATETIME_FORMAT),
    help='Timestamp of the target radar image, defaults to the current date and time',)
parser.add_argument('--template',
    type=str,
    default=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates/template.vrt'),
    help='Template VRT file used to create the new VRT',)


def clean_timestamp(timestamp):
    """
    Moves the timestamp to the previous minute that is a multiple
    of 5.
    """
    value = timestamp.minute % 5
    return timestamp - datetime.timedelta(minutes=value)


if __name__ == '__main__':
    args = parser.parse_args()
    timestamp = clean_timestamp(args.timestamp)
    template = ElementTree.parse(args.template)

    for source in template.getroot().findall('VRTRasterBand/SimpleSource/SourceFilename'):
        source.text = timestamp.strftime(RADAR_IMAGE_TEMPLATE)

    template.write(timestamp.strftime(args.output))
