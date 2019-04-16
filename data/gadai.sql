create database gadai;
use gadai

create table usuarios(
    id_usuario integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_u varchar(30) NOT NULL,
    email_u varchar(50) not null,
    telefono_u char(10) not null,
    password char(10) not null,
    municipio_u varchar(50) not null,
    colonia_u varchar(50) not null,
    tipo_u varchar(50) not null,
    imagen text null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into usuarios(id_usuario,nombre_u,email_u,telefono_u,password,municipio_u,colonia_u,tipo_u,imagen)values
    ('1','DejandoHuella','dejandohuella@gmail.com','7751347695','12345','Tulancingo','Arboledas','Asocicion','c:/jgdkja.png');

create table denuncia(
    id_denuncia integer not null PRIMARY KEY AUTO_INCREMENT,
    nombre_d varchar(30) not null,
    descripcion_d text not null,
    municipio
    _d varchar(30) not null,
    colonia_d varchar(30) not null,
    imagen text null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into denuncia(id_denuncia,nombre_d,descripcion_d,municipio_d,colonia_d,imagen) values
    ('1','Francisco Monrroy','Se encontro a una señora golpeando a su mascota, la mascota esta muy erida y queria reportarlo','Santiago Tulantepec','Habitacional','c:/jahjdbhb.jpg');
    
create table desaparecidos(
    id_desaparecidos integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_p varchar(30) not null,
    email_p varchar(50) not null,
    telefono_p char(10) not null,
    municipio_p varchar(30) not null,
    colonia_p varchar(30) not null,
    fecha_p  varchar(25) NOT NULL,
    nombre_m varchar(30) not null,
    edad_m char(10) not null,
    sexo_m varchar(10) not null,
    tipo_m varchar(10) not null,
    descripcion_m text not null,
    id_usuario integer,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    imagen text not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into desaparecidos(id_desaparecidos,nombre_p,email_p,telefono_p,municipio_p,colonia_p,fecha_p,nombre_m,edad_m,sexo_m,tipo_m,descripcion_m,id_usuario,imagen)values
    ('1','Gabriela Curiel Garca', 'gabriela@gmail.com', '7751347695', 'Santiago','Habitacional','2019-05-05','Dante', '1año', 'Hembra', 'Perro', 'Es muy cariñoso', '1', 'c:/dhfghgekfgke');

create table adoptar(
    id_publicar integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_persona varchar(30) not null,
    email varchar(50) not null,
    telefono char(10) not null,
    municipio varchar(30) not null,
    colonia varchar(30) not null,
    fecha varchar(24) NOT NULL,
    nom_mascota varchar(20) not null,
    edad_mascota char(10) not null,
    sexo_mascota varchar(10) not null,
    tipo_mascota varchar(10) not null,
    descripcion_mascota text not null,
    id_usuario integer,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    imagen text not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into adoptar(id_publicar,nom_persona,email,telefono,municipio,colonia,fecha,nom_mascota,edad_mascota,sexo_mascota,tipo_mascota,descripcion_mascota,id_usuario,imagen)values
    ('1','Gabriela Curiel Garca', 'gabriela@gmail.com', '7751347695', 'Santiago','Paxtepec','2019-05-05','Dante', '1año', 'Hembra', 'Perro', 'Es muy cariñoso', '1','c:/dhfghgekfgke');


create table comentarios(
    id_comentario integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(30) not null,
    email varchar(30) not null,
    comentario text not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into comentarios(id_comentario,nombre,email,comentario)values
    ('1','Daniela Rubiales Marquez', 'dani@gmail.com', 'Bien');

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create user 'c2410og4t3mifdju'@'localhost' identified by 'obq28rtba4cgb8dv';
grant all privileges on s3icpvk5swtsrx6f.* to 'z1ntn1zv0f1qbh8u.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'@'localhost';
flush privileges; 

