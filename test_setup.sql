drop schema if exists test cascade; 
CREATE SCHEMA test;
create table test.source1 (name varchar(10), cnt int);
create table test.source2 (name varchar(10), cnt int);

insert into test.source1 (name, cnt)
values ('a', 1), 
       ('b', 2),
       ('c', 3);

insert into test.source2 (name, cnt)
values ('a', 1), 
       ('b', 2),
       ('b', 3);
       
create view test.view1 as (select * from test.source1);
create view test.view2 as (
	select s1.name, sum(s2.cnt) as cnt
	from test.source1 s1
	left join test.source2 s2
	on s1.name = s2.name
	group by s1.name
);