-- Active: 1715737537685@@127.0.0.1@3307@youtube
create database youtube

create table user(
    id int primary key auto_increment,
    nome varchar(50) not null,
    email varchar(50) not null,
    senha varchar(50) not null
)

SHOW TABLES