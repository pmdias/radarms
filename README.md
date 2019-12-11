# radarms

## Configuration

The following is a brief explanation of the environment variables
that are used by the stack:

* `DATA_DIR`: directory where the `vrt` files will be stored. Needs to be mounted
into the `mapserver` container;
* `POSTGRES_INIT`: `SQL` script that is used to initialize the database on startup;
* `POSTGRES_USER`: The user that will be used for the database;
* `POSTGRES_PASS`: The password that will be used for the database user;
* `POSTGRES_DBNAME`: The name of the database;

If any of these values is changed you'll also need to edit the `mapfile` so
that `mapserver` can connect to the database.
