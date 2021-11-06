-- this is used by Dockerfile to create necessary table schema in the PostgreSQL database

BEGIN;

CREATE SCHEMA sales;

CREATE TABLE sales.manufacturer (
	id bigint PRIMARY KEY,
	name varchar[255]
);

CREATE TABLE sales.car_model (
	id bigint PRIMARY KEY,
	name varchar[255],
	weight_kg float8,
	manufacturer_id bigint,
	CONSTRAINT fk_manufacturer FOREIGN KEY(manufacturer_id) REFERENCES sales.manufacturer(id)
);

CREATE TABLE sales.car (
	id bigint PRIMARY KEY,
	serial_number varchar[255],
	original_price float8,
	model_id bigint,
	CONSTRAINT fk_car_model FOREIGN KEY(model_id) REFERENCES sales.car_model(id)
);

CREATE TABLE sales.salesperson (
	id bigint PRIMARY KEY,
	name varchar[255]
);

CREATE TABLE sales.customer (
	id bigint PRIMARY KEY,
	name varchar[255],
	phone bigint
);

CREATE TABLE sales.sales (
	id bigint PRIMARY KEY,
	final_price float8,
	datetime timestamp,
	car_id bigint,
	salesperson_id bigint,
	customer_id bigint,
	CONSTRAINT fk_car FOREIGN KEY(car_id) REFERENCES sales.car(id),
	CONSTRAINT fk_salesperson FOREIGN KEY(salesperson_id) REFERENCES sales.salesperson(id),
	CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES sales.customer(id)
);

COMMIT;