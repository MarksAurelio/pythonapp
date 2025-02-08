create table todolist(
"_lineNumber" serial primary key,
item varchar(250),
status varchar(100)
);

select * from todolist;


insert into todolist(item, status) values('Comprar Pão', 'Iniciado');

select * from todolist;

INSERT INTO todolist(item, status) VALUES('Comprar','Em Fila') RETURNING "_lineNumber";


