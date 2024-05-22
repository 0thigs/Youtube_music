-- Active: 1715737537685@@127.0.0.1@3307@youtube
use youtube

create table post (
    id int primary key auto_increment,
    titulo varchar(50) not null,
    description text not null,
    musicurl varchar(250) not null,
    musicimage VARCHAR(250) not null
)

INSERT INTO post(titulo, description ,musicurl, musicimage) VALUES ("Teste", "Neina é gay" ,"https://www.youtube.com/watch?v=lA2L6qHuBeg", "banana.png")

drop table post

SELECT * from post