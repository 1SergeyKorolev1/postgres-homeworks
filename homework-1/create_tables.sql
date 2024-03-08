-- SQL-команды для создания таблиц
create table emploees(
	employee_id int UNIQUE primary key,
	first_name text,
	last_name text,
	title text,
	birth_dat date,
	notes text);

create table customers(
	customer_id varchar(10) primary key,
	company_name text,
	contact_name text);

create table orders(
	order_id int UNIQUE primary key,
	customer_id varchar(10) references customers(customer_id),
	employee_id int references emploees(employee_id),
	order_date date,
	ship_city text);
