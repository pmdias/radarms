# radarms

Web Map Service for the IPMA radar images.

## Configuration

The following is a brief explanation of the environment variables
that are used by the stack:

* `DATA_DIR`: directory where the `vrt` files will be stored. Needs to be mounted
into the `mapserver` container;
* `MAPSERVER_CONFIG`: the `mapfile` that tells `mapserver` how to serve the images;
* `POSTGRES_INIT`: `SQL` script that is used to initialize the database on startup;
* `POSTGRES_USER`: The user that will be used for the database;
* `POSTGRES_PASS`: The password that will be used for the database user;
* `POSTGRES_DBNAME`: The name of the database;

If any of these values is changed you'll also need to edit the `mapfile` so
that `mapserver` can connect to the database.

## Samples

I'm including a sample `vrt` that includes everything that is needed to serve the
images via `WMS`. The sample is ready to be used, only the `sourceFilename` needs
to be changed if you want it.

## Scripts

We include two scripts to allow the generation of both the `vrt` files and the
insertion to the database of the required data.

### VRT creation

Run the provided script `create_vrt.py` to create a `vrt` for a specific date and time.
The script expects a timestamp in the format `%Y-%m-%dT%H:%M` and a template string for
the output `vrt` that can use datetime format arguments. An example of the execution of
the script:

```
$ ./create_vrt.py --timestamp 2019-12-11T12:23 pcr-%Y-%m-%dT%H%M.vrt
```

> Please note that the `output` path must include the mounted directory that was indicated
> on the `DATA_DIR` environment variable during the stack deployment.

If no timestamp is passed to the script, it assumes the current date and time and proceeds
from here. For more information, run the script with the `--help` flag

```
$ ./create_vrt.py --help
usage: create_vrt.py [-h] [--timestamp T] [--template TEMPLATE] output

Create a new VRT file

positional arguments:
  output               Output filename, can use format strings to use the
                       timestamp of the file

optional arguments:
  -h, --help           show this help message and exit
  --timestamp T        Timestamp of the target radar image, defaults to the
                       current date and time
  --template TEMPLATE  Template VRT file used to create the new VRT
```
