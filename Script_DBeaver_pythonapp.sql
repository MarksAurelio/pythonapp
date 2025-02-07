create table todolist(
"_likeNumber" serial primary key,
item varchar(250),
status varchar(100)
);

select * from todolist;

insert into todolist(item, status) values('Comprar Pão', 'Iniciado');

select * from todolist;

-- comando bash
-- curl -X POST http://127.0.0.1:5000/item -H "Content-Type: application/json" -d '{"item":"Comprar", "status":"EM Fila"}'