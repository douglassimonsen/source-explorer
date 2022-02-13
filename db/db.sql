drop table if exists databases;
create table databases (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(20),
  credentials varchar(500),
  last_updated datetime
);
drop table if exists objects;
create table objects (  // include report queries in here
  id integer PRIMARY KEY AUTOINCREMENT,
  database_id references databases,
  schema varchar(100),
  name varchar(100),
  obj_type varchar(100),
  sample_data varchar(65535),
  definition varchar(65535),
  last_updated datetime
);
drop table if exists dependencies;
create table dependencies (
  parent integer references objects,
  child integer references objects,
  last_updated datetime
);
drop table if exists reports;
create table reports (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(100),
  report_type varchar(100),
  last_updated datetime
);
drop table if exists report_dependencies;
create table report_dependencies (
  obj_id integer references objects,
  report_id integer references reports,
  last_updated datetime
);