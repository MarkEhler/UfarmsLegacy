CREATE TABLE IF NOT EXISTS locations (
	id varchar(36) primary key not null,
	group_guid varchar(36) not null,
	name varchar(200) not null,
	description text,
	location json,
	type varchar(200),
	datetime_ordered timestamp,
	eta timestamp,
	arrived boolean default false
);