drop table if exists weather;
create table weather (
  id integer primary key autoincrement,
  lat text not null,
  long text not null,
  te text not null
);
