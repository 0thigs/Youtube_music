-- Active: 1715783627262@@localhost@3307
use youtube

create table user(
    id int primary key auto_increment,
    nome varchar(50) not null,
    email varchar(50) not null,
    senha varchar(50) not null
)

create table post (
    id int primary key auto_increment,
    titulo varchar(50) not null,
    musicurl varchar(250) not null,
    image varchar(50) not null
)

drop table post

drop table user

SHOW TABLES