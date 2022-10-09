# Dashed

This project provides a simple setup for a Grafana installation, a PostgreSQL database and
a pluggable set of data loaders that load data in the db, which in turns is the main data source
for Grafana.

For example, [garmin-importer][garmin-importer] provides a way to export sports activities from Garmin Connect and into
an own storage of choice (in that case, dynamo-db), and **dashed** is where that data is put to good use.

The data loader concept and implementation should be generic enough that it should be easy to replicate, so that other
data can be imported from other sources. This will make it possible to extend the reach of our insights once we can
cross-reference data from multiple sources.


## Grafana

It is an industry standard, open-source, platform that gives users the possibility of crafting
their own dashboards.

We will run the latest stable release from its docker container, and find a way to persist
dashboards in a way that if we re-start this whole project on separate hardware, we get the
desired set of dashboards up and running.


## PostgreSQL database

This is also an open-source industry standard and Grafana has a stable plugin-integration with it

We will run a single instance docker container based on the latest stable release. Each data loader
will take care of making sure that the necessary tables are set up, that there are no migrations to
run, and each data loader should create its own dedicated user to insert data and to create and
manage its own table, so that different loaders won't be able to interfere with each other.


## Data Loaders

This is the component that at startup will check what data is in the database, make sure that the
tables it needs are there and with the correct schema, that all the db migrations have been carried
out, and import the necessary data.


[garmin-importer]: https://github.com/lancerinf/garmin-importer
